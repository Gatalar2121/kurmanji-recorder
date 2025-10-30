#!/usr/bin/env python3
"""
Kurmancî Whisper Fine-tuning Script
Bu script, kaydedilmiş Kurmancî dataset ile Whisper modelini fine-tune eder.
"""

import os
import json
import torch
from datasets import Dataset, Audio
from transformers import (
    WhisperProcessor,
    WhisperForConditionalGeneration,
    WhisperTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    WhisperFeatureExtractor
)
from dataclasses import dataclass
from typing import Dict, List, Union
import librosa
import soundfile as sf

# Dataset yolu - Bu scripti kurmanji_dataset klasörüne koyun
DATASET_PATH = "."
AUDIO_PATH = "audio"
MANIFEST_FILE = "whisper_manifest.jsonl"

class KurmanjiWhisperDataset:
    def __init__(self, manifest_path, audio_path):
        self.manifest_path = manifest_path
        self.audio_path = audio_path
        self.data = self.load_manifest()
    
    def load_manifest(self):
        """Manifest dosyasını yükle"""
        data = []
        with open(self.manifest_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line.strip())
                    data.append(entry)
        return data
    
    def create_hf_dataset(self):
        """Hugging Face Dataset oluştur"""
        # Veri hazırlığı
        audio_paths = []
        transcripts = []
        
        for entry in self.data:
            audio_file = os.path.join(self.audio_path, entry['audio_filepath'].replace('audio/', ''))
            if os.path.exists(audio_file):
                audio_paths.append(audio_file)
                transcripts.append(entry['text'])
        
        # Dataset oluştur
        dataset = Dataset.from_dict({
            "audio": audio_paths,
            "transcription": transcripts
        })
        
        # Audio özelliğini ekle
        dataset = dataset.cast_column("audio", Audio(sampling_rate=22050))
        
        return dataset

@dataclass
class DataCollatorSpeechSeq2SeqWithPadding:
    """Whisper için özel data collator"""
    processor: any
    decoder_start_token_id: int

    def __call__(self, features: List[Dict[str, Union[List[int], torch.Tensor]]]) -> Dict[str, torch.Tensor]:
        # Audio özelliklerini ayır
        input_features = [{"input_features": feature["input_features"]} for feature in features]
        batch = self.processor.feature_extractor.pad(input_features, return_tensors="pt")

        # Etiketleri ayır  
        label_features = [{"input_ids": feature["labels"]} for feature in features]
        labels_batch = self.processor.tokenizer.pad(label_features, return_tensors="pt")

        # -100 ile replace et (ignore index)
        labels = labels_batch["input_ids"].masked_fill(labels_batch.attention_mask.ne(1), -100)

        # bos token kaldır
        if (labels[:, 0] == self.decoder_start_token_id).all().cpu().item():
            labels = labels[:, 1:]

        batch["labels"] = labels
        return batch

def prepare_dataset(batch, processor):
    """Dataset hazırlama fonksiyonu"""
    # Audio'yu yükle ve özellik çıkar
    audio = batch["audio"]
    
    # Input features
    input_features = processor.feature_extractor(
        audio["array"], 
        sampling_rate=audio["sampling_rate"], 
        return_tensors="pt"
    ).input_features[0]
    
    # Labels (tokenize)
    labels = processor.tokenizer(batch["transcription"]).input_ids
    
    return {
        "input_features": input_features,
        "labels": labels,
    }

def main():
    """Ana eğitim fonksiyonu"""
    print("🚀 Kurmancî Whisper Fine-tuning başlatılıyor...")
    
    # Model ve processor yükle
    model_name = "openai/whisper-small"  # Küçük model ile başla
    processor = WhisperProcessor.from_pretrained(model_name, language="ku", task="transcribe")
    model = WhisperForConditionalGeneration.from_pretrained(model_name)
    
    # Tokenizer ayarları
    tokenizer = WhisperTokenizer.from_pretrained(model_name, language="ku", task="transcribe")
    
    # Dataset yükle
    dataset_loader = KurmanjiWhisperDataset(MANIFEST_FILE, AUDIO_PATH)
    dataset = dataset_loader.create_hf_dataset()
    
    print(f"📊 Toplam örnek sayısı: {len(dataset)}")
    
    # Dataset'i hazırla
    dataset = dataset.map(
        lambda batch: prepare_dataset(batch, processor),
        remove_columns=dataset.column_names,
        desc="Dataset hazırlanıyor"
    )
    
    # Train/test split
    train_test = dataset.train_test_split(test_size=0.1)
    train_dataset = train_test["train"]
    eval_dataset = train_test["test"]
    
    print(f"📚 Eğitim örnekleri: {len(train_dataset)}")
    print(f"🧪 Test örnekleri: {len(eval_dataset)}")
    
    # Data collator
    data_collator = DataCollatorSpeechSeq2SeqWithPadding(
        processor=processor,
        decoder_start_token_id=model.generation_config.decoder_start_token_id,
    )
    
    # Eğitim parametreleri
    training_args = Seq2SeqTrainingArguments(
        output_dir="./whisper-kurdish-kurmanji",
        per_device_train_batch_size=8,
        gradient_accumulation_steps=2,
        learning_rate=1e-5,
        warmup_steps=500,
        max_steps=2000,
        gradient_checkpointing=True,
        fp16=True,
        evaluation_strategy="steps",
        per_device_eval_batch_size=8,
        predict_with_generate=True,
        generation_max_length=225,
        save_steps=500,
        eval_steps=500,
        logging_steps=25,
        report_to=["tensorboard"],
        load_best_model_at_end=True,
        metric_for_best_model="wer",
        greater_is_better=False,
        push_to_hub=False,
    )
    
    # Trainer oluştur
    trainer = Seq2SeqTrainer(
        args=training_args,
        model=model,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
        tokenizer=processor.feature_extractor,
    )
    
    # Eğitimi başlat
    print("🔥 Eğitim başlatılıyor...")
    trainer.train()
    
    # Modeli kaydet
    trainer.save_model("./whisper-kurdish-kurmanji-final")
    processor.save_pretrained("./whisper-kurdish-kurmanji-final")
    
    print("✅ Eğitim tamamlandı!")
    print("📁 Model kaydedildi: ./whisper-kurdish-kurmanji-final")
    
    # Test
    print("🧪 Model test ediliyor...")
    # Burada test kodu eklenebilir

if __name__ == "__main__":
    main()

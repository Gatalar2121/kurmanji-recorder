# Kurmancî Whisper Fine-tuning

Bu klasör, Kurmancî dili için Whisper model eğitimi içerir.

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

```bash
python whisper_training.py
```

## Dosyalar

- `whisper_training.py`: Ana eğitim scripti
- `whisper_manifest.jsonl`: Whisper dataset manifest
- `transcripts.txt`: Transkript dosyası
- `audio/`: Ses dosyaları klasörü
- `requirements.txt`: Gerekli Python paketleri

## Eğitim Sonrası

Eğitilmiş model `whisper-kurdish-kurmanji-final` klasöründe saklanır.

## Kullanım Örneği

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

# Modeli yükle
processor = WhisperProcessor.from_pretrained("./whisper-kurdish-kurmanji-final")
model = WhisperForConditionalGeneration.from_pretrained("./whisper-kurdish-kurmanji-final")

# Ses dosyasını yükle
audio, sr = librosa.load("test_audio.wav", sr=16000)

# Transkripsiyon
input_features = processor(audio, sampling_rate=sr, return_tensors="pt").input_features
predicted_ids = model.generate(input_features)
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

print(transcription[0])
```

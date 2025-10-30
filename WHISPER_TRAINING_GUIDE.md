# 🎯 Whisper Eğitimi için Kurmanji Word Recorder Kılavuzu

## 🎉 Harika Haber! 
Programınız artık **Whisper eğitimi için tamamen optimize edildi**! Kaydettiğiniz her ses dosyası otomatik olarak Whisper modelini eğitmek için hazır hale geliyor.

## 🔧 Yeni Özellikler

### 📁 Otomatik Whisper Dosya Formatı
- **Sıralı adlandırma**: `000001_merhaba.wav`, `000002_cawa_yi.wav` şeklinde
- **Manifest dosyası**: Her ses için otomatik `whisper_manifest.jsonl` 
- **Transkript dosyası**: Basit format `transcripts.txt`
- **Metadata**: JSON formatında her kaydın detayları

### 🎵 Ses Kalitesi Garantisi
- **22050 Hz** örnekleme oranı (Whisper için ideal)
- **Mono** kanal (daha az veri, daha hızlı eğitim)
- **Otomatik normalizasyon** ve gürültü azaltma
- **Süre hesaplama** (eğitim için ne kadar veri olduğunu görmek için)

## 📊 Whisper İstatistikleri

Program artık size şunları gösteriyor:
- ✅ Toplam kaydedilen süre (saat/dakika)
- ✅ Whisper eğitimi için hazırlık durumu
- ✅ Önerilen minimum süre (10 saat)
- ✅ Dataset kalitesi analizi

## 🚀 Nasıl Kullanılır

### 1. Kayıt Yapın
- Normal şekilde kelime/cümle kaydedin
- Program otomatik olarak Whisper formatında kayıt yapar
- Her kayıt sonrası otomatik metadata güncellenir

### 2. İlerlemenizi Takip Edin
- **📊 İstatistikler** butonuna tıklayın
- Whisper eğitimi için ne kadar veri topladığınızı görün
- Önerilen 10 saatlik hedefe ne kadar yakın olduğunuzu kontrol edin

### 3. Dataset'i Dışa Aktarın
- **📦 Dataset Dışa Aktar** butonunu kullanın
- Whisper eğitimi için hazır paket oluşur:
  ```
  whisper_kurmanci_20241004/
  ├── audio/              # Tüm ses dosyaları
  ├── manifest.jsonl      # Whisper eğitim dosyası
  ├── transcripts.txt     # Transkriptler
  └── README.md          # Kullanım kılavuzu
  ```

## 🎯 Whisper Eğitimi Öneriler

### Minimum Gereksinimler
- **100+ farklı cümle/kelime**
- **2-10 saniye arası kayıtlar**
- **Toplam 1+ saat ses** (başlangıç için)
- **10+ saat ses** (kaliteli model için)

### Kalite İpuçları
- 🎤 **Kaliteli mikrofon** kullanın
- 🔇 **Sessiz ortamda** kayıt yapın
- 🗣️ **Net telaffuz** ile konuşun
- ⏱️ **2-10 saniye** arası kayıtlar yapın
- 📝 **Çeşitli cümle yapıları** kaydedin

## 📋 Dosya Yapısı (Arka Plan)

Program şu dosyaları otomatik oluşturuyor:

```
kurmanji_dataset/
├── audio/
│   ├── 000001_merhaba.wav
│   ├── 000002_cawa_yi.wav
│   └── ...
├── whisper_manifest.jsonl  # Whisper için
├── transcripts.txt         # Basit format
├── metadata.json          # Program bilgileri
└── wordlist.json          # Kelime listesi
```

## 🎉 Sonuç

**Artık hiçbir şey yapmanıza gerek yok!** 

✅ Kaydettiğiniz her ses otomatik olarak Whisper eğitimi için hazır  
✅ Dosya adları ve formatlar tamamen optimize edildi  
✅ Metadata ve transkriptler otomatik oluşuyor  
✅ İstatistikler ile ilerlemenizi takip edebiliyorsunuz  
✅ Dışa aktarma ile Whisper eğitimine hazır paket alıyorsunuz  

**Sadece kayıt yapmaya devam edin, program gerisini hallediyor!** 🎤✨

---

*Bu optimizasyonlar sayesinde Kurdish/Kurmancî Whisper modeli eğitimi için mükemmel bir dataset hazırlayabileceksiniz.*
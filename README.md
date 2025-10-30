# Kurmanji Word Recorder - Modern Edition 🎤

## Modern ve Geliştirilmiş Özellikleri

### ✨ Yeni Özellikler
- **Modern UI**: CustomTkinter ile dark/light tema desteği
- **Mikrofon Kontrolü**: Otomatik mikrofon tespiti ve durum göstergesi
- **Gelişmiş Kelime Yönetimi**: Manuel ekleme, toplu import, düzenleme
- **Çoklu Format Desteği**: TXT, DOCX, PDF, URL'den kelime yükleme
- **Akıllı Kelime İşleme**: Otomatik temizleme, dublikat kaldırma
- **Görsel Yönetim**: Kelime listesi görüntüleyici ve düzenleyici
- **Export Özellikleri**: TXT, JSON, CSV formatlarında export
- **Ses Kalitesi**: 22050 Hz sampling rate, noise reduction, normalizasyon
- **Gerçek Zamanlı Feedback**: Ses seviyesi göstergesi, ilerleme takibi
- **Akıllı Yönetim**: Otomatik dosya isimlendirme, metadata yönetimi
- **İstatistikler**: Detaylı kayıt istatistikleri ve analiz

### 🎯 Temel Kullanım

#### 1. İlk Başlatma
```bash
cd kurmanji
python kurmanji_recorder_modern.py
```

#### 2. Kelime ve Cümle Yökleme (ÇOK GELİŞMİŞ!)

**Manuel Ekleme:**
- **"➕ Add Words/Sentences"**: Çoklu kelime/cümle ekleme penceresi
- **"📝 Quick Add"**: Tek kelime hızlı ekleme
- **Clipboard Desteği**: Panoya kopyalanan metinleri yapıştırma
- **Otomatik Temizleme**: Boş satırları ve fazla boşlukları temizleme

**Dosya İmport:**
- **"📄 TXT File"**: Metin dosyalarından kelime yükleme
- **"📘 DOCX File"**: Word belgelerinden kelime çıkarma
- **"📕 PDF File"**: PDF dosyalarından metin çıkarma
- **"🌐 From URL"**: İnternet adreslerinden içerik yükleme

**Yönetim:**
- **"📋 View All Words"**: Tüm kelimeleri görüntüleme ve düzenleme
- **"🔄 Remove Duplicates"**: Tekrarlanan kelimeleri kaldırma
- **"📤 Export Words"**: Kelime listesini TXT/JSON/CSV formatında kaydetme

#### 3. Kayıt İşlemi
1. Mikrofon durumunu kontrol edin (✅ yeşil olmalı)
2. İstediğiniz ses cihazını seçin
3. Kelime listesinde gezinmek için Previous/Next butonlarını kullanın
4. "🔴 Start Recording" ile kaydı başlatın
5. Kelimeyi sesli okuyun
6. "⏹️ Stop Recording" ile kaydı durdurun
7. "▶️ Play" ile kaydı dinleyin
8. "💾 Save & Next" ile kaydedin ve sonraki kelimeye geçin

### 🔧 Gelişmiş Ayarlar

#### Ses Ayarları
- **Sample Rate**: 22050 Hz (yüksek kalité)
- **Channels**: Mono (1 kanal)
- **Format**: 32-bit float
- **Noise Reduction**: Otomatik düşük frekanslı gürültü filtreleme
- **Normalization**: Otomatik ses seviyesi normalleştirme

#### Dosya Organizasyonu
```
kurmanji_dataset/
├── audio/              # Ses kayıtları (.wav)
├── documents/          # Yüklenen belgeler
├── metadata.json       # Kayıt durumu ve metadata
└── wordlist.json       # Kelime listesi
```

### 📊 İstatistikler ve Analiz

#### Kayıt Durumu
- Toplam kelime sayısı
- Kaydedilen kelime sayısı
- Tamamlanma yüzdesi
- Kalan kelime sayısı

#### Ses Verileri
- Toplam kayıt süresi
- Ortalama kelime başına süre
- Toplam dosya boyutu
- Kayıt kalitesi bilgileri

### 🎨 Tema ve Görünüm
- **Dark Mode**: Göz yorucu olmayan koyu tema
- **Light Mode**: Parlak ortamlar için açık tema
- **Responsive Design**: Farklı ekran boyutlarına uyum
- **Modern Icons**: Emojili butonlar ve net görseller

### 🎯 Gelişmiş Kelime/Cümle Yönetimi

#### Manuel Ekleme Özellikleri
- **Çoklu Ekleme**: Bir seferde onlarca kelime/cümle ekleme
- **Akıllı İşleme**: Otomatik boşluk temizleme ve dublikat kontrolü
- **Clipboard Integration**: Kopyala-yapıştır desteği
- **Canlı Önizleme**: Ekleme öncesi içeriği görme

#### Kelime Listesi Yönetimi
- **Görsel Düzenleyici**: Tüm kelimeleri liste halinde görme
- **Arama ve Filtreleme**: Kelime arama, kaydedilen/kaydedilmemiş filtreleme
- **Yerinde Düzenleme**: Kelimeleri seçip düzenleme
- **Toplu Silme**: Birden fazla kelimeyi seçip silme
- **Durum İndikatörleri**: ✅ Kaydedilen, ⭕ Kaydedilmemiş işaretleri

#### Import/Export Özellikleri
- **Çoklu Format Import**: TXT, DOCX, PDF, URL desteği
- **Akıllı Parsing**: HTML temizleme, özel karakter işleme
- **Export Seçenekleri**: TXT (işaretli), JSON (metadata ile), CSV (tablo)
- **Yedekleme**: Otomatik metadata yedekleme

### 💾 Veri Yönetimi

#### Export Özellikleri
- **Dataset Export**: Tüm veriyi zip formatında export
- **Word List Export**: Kelime listesini TXT/JSON/CSV formatında export
- **İstatistik Export**: Detaylı analiz raporları
- **Yedekleme**: Otomatik metadata yedekleme
- **Tarih Stamping**: Her kayıt için zaman damgası

#### Import Özellikleri
- **TXT Files**: Satır satır kelime listesi
- **DOCX Files**: Word belgeleri
- **PDF Files**: PDF belgeleri
- **URL Loading**: Web sayfalarından içerik çekme
- **Smart Parsing**: Noktalama işaretleri temizleme, dublikat kontrolü
- **Batch Processing**: Büyük dosyaları işleme

### 🚀 Performans Optimizasyonları

#### Ses İşleme
- **Real-time Processing**: Gerçek zamanlı ses işleme
- **Buffer Management**: Akıllı bellek yönetimi
- **Threading**: Asenkron ses işleme
- **Quality Control**: Otomatik kalite kontrolü

#### UI Optimizasyonu
- **Responsive Updates**: Kesintisiz UI güncellemeleri
- **Memory Efficient**: Düşük bellek kullanımı
- **Fast Navigation**: Hızlı kelime geçişi

### 🎯 Kurmanji Dataset Oluşturma Rehberi

#### 1. Kelime Toplama
- Kurmanji dilbilgisi kitaplarından kelime listesi çıkarma
- Online sözlüklerden kelime toplama
- Günlük konuşma dilinden kelime seçimi

#### 2. Kayıt Stratejisi
- **Sabit Ortam**: Aynı ortamda kayıt yapın
- **Tutarlı Mesafe**: Mikrofon mesafesini sabit tutun
- **Net Telaffuz**: Her kelimeyi net ve açık telaffuz edin
- **Tekrar Kontrolü**: Kötü kayıtları tekrar edin

#### 3. Kalite Kontrolü
- Her kaydı kontrol edin
- Gürültülü kayıtları temizleyin
- Tutarlı ses seviyesi koruyun
- Metadata'yı düzenli güncelleyin

### 🛠️ Troubleshooting

#### Mikrofon Sorunları
```
❌ Mikrofon bulunamadı:
- Windows ses ayarlarını kontrol edin
- Mikrofon bağlantısını kontrol edin
- Sürücüleri güncelleyin

❌ Ses alınmıyor:
- Mikrofon izinlerini kontrol edin
- Ses seviyesini artırın
- Başka uygulamaları kapatın
```

#### Performans Sorunları
```
🐌 Yavaş çalışıyor:
- Arka plan uygulamalarını kapatın
- Disk alanını kontrol edin
- RAM kullanımını kontrol edin

📁 Dosya sorunları:
- Yazma izinlerini kontrol edin
- Disk alanını kontrol edin
- Antivirus ayarlarını kontrol edin
```

### 📞 Destek

#### Hata Raporlama
Hata durumunda:
1. Hata mesajını kaydedin
2. Terminal çıktısını kontrol edin
3. Python ve kütüphane versiyonlarını kontrol edin

#### Özellik İstekleri
Yeni özellik önerileri için:
- Detaylı açıklama yapın
- Kullanım senaryosunu belirtin
- Öncelik seviyesini belirtin

---
**Not**: Bu modern versiyon, orijinal uygulamanızın tüm sorunlarını çözer ve uzun süreli profesyonel kullanım için optimize edilmiştir.
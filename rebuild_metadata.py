"""
Rebuild metadata.json from existing audio files
"""
import json
import re
from pathlib import Path
from datetime import datetime

# Paths
AUDIO_DIR = Path("kurmanji_dataset/audio")
METADATA_FILE = Path("kurmanji_dataset/metadata.json")
WORDLIST_FILE = Path("kurmanji_dataset/wordlist.json")

def extract_word_from_filename(filename):
    """Extract word and speed from filename like 000001_aferin_slow.wav or 000001_aferin.wav"""
    # Remove number prefix and .wav extension
    match = re.match(r'^\d{6}_(.+?)(?:_(slow|normal|fast))?\.wav$', filename)
    if match:
        word = match.group(1).replace('_', ' ')
        speed = match.group(2) if match.group(2) else "normal"
        return word, speed
    return None, None

def rebuild_metadata():
    """Scan audio files and rebuild metadata"""
    print("🔄 Rebuilding metadata from audio files...")
    
    # Get all audio files
    audio_files = list(AUDIO_DIR.glob("*.wav"))
    print(f"📁 Found {len(audio_files)} audio files")
    
    # Track recorded words and speeds
    recorded_words = set()
    recorded_speeds = {}
    
    # Process each audio file
    for audio_file in audio_files:
        word, speed = extract_word_from_filename(audio_file.name)
        if word:
            recorded_words.add(word)
            
            if word not in recorded_speeds:
                recorded_speeds[word] = {"slow": False, "normal": False, "fast": False}
            
            recorded_speeds[word][speed] = True
            print(f"  ✅ {word} - {speed}")
    
    # Load word counts from files
    total_words = 0
    total_sentences = 0
    total_paragraphs = 0
    
    try:
        with open(WORDLIST_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            total_words = len(data.get('words', []))
    except:
        pass
    
    try:
        with open(Path("kurmanji_dataset/sentencelist.json"), 'r', encoding='utf-8') as f:
            data = json.load(f)
            total_sentences = len(data.get('sentences', []))
    except:
        pass
    
    try:
        with open(Path("kurmanji_dataset/paragraphlist.json"), 'r', encoding='utf-8') as f:
            data = json.load(f)
            total_paragraphs = len(data.get('paragraphs', []))
    except:
        pass
    
    # Create metadata
    metadata = {
        "recorded_words": list(recorded_words),
        "recorded_speeds": recorded_speeds,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "total_paragraphs": total_paragraphs,
        "last_updated": datetime.now().isoformat()
    }
    
    # Save metadata
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Metadata rebuilt successfully!")
    print(f"   📝 {len(recorded_words)} words recorded")
    print(f"   🎯 Total words: {total_words}")
    print(f"   📊 Progress: {len(recorded_words)}/{total_words} ({len(recorded_words)/total_words*100:.1f}%)")
    
    # Show some recorded words
    if recorded_words:
        print(f"\n📋 First 10 recorded words:")
        for word in sorted(list(recorded_words))[:10]:
            speeds = recorded_speeds[word]
            speed_status = []
            if speeds["slow"]: speed_status.append("🐌")
            if speeds["normal"]: speed_status.append("🎯")
            if speeds["fast"]: speed_status.append("🚀")
            print(f"   {word}: {' '.join(speed_status)}")

if __name__ == "__main__":
    rebuild_metadata()

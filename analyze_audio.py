import numpy as np
import wave

# Compare two recordings
good_file = r"c:\Users\PyxSara\Desktop\kurmanji\kurmanji_dataset\audio\000230_Keç_normal.wav"
bad_file = r"c:\Users\PyxSara\Desktop\kurmanji\kurmanji_dataset\audio\000266_karibin_slow.wav"

for label, wav_path in [("GOOD (keç)", good_file), ("BAD (karibin)", bad_file)]:
    print(f"\n{'='*60}")
    print(f"Analyzing: {label}")
    print(f"{'='*60}")
    
    with wave.open(wav_path, 'rb') as wav_file:
        sample_rate = wav_file.getframerate()
        n_frames = wav_file.getnframes()
        audio_bytes = wav_file.readframes(n_frames)
        audio_data = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

    duration = len(audio_data) / sample_rate
    print(f"Duration: {duration:.3f} seconds")
    
    # Calculate energy in 100ms windows for clearer pattern
    window_size = int(sample_rate * 0.1)
    energy = []
    for i in range(0, len(audio_data), window_size):
        window = audio_data[i:i+window_size]
        energy.append(np.mean(np.abs(window)))
    
    max_energy = max(energy)
    print(f"Max energy: {max_energy:.4f}")
    print(f"Mean energy: {np.mean(energy):.4f}")
    
    # Find where speech likely ends
    threshold = max_energy * 0.2
    last_speech = 0
    for i in range(len(energy)-1, -1, -1):
        if energy[i] > threshold:
            last_speech = i
            break
    
    speech_end_time = last_speech * 0.1
    print(f"Estimated speech end: {speech_end_time:.2f}s")
    print(f"Excess audio after speech: {duration - speech_end_time:.2f}s")
    
    # Show last 10 windows (1 second)
    print(f"\nLast 1 second energy profile:")
    for i in range(max(0, len(energy)-10), len(energy)):
        t = i * 0.1
        e = energy[i]
        marker = "🔊" if e > threshold else "🔇"
        bar = "█" * int(e / max_energy * 50)
        print(f"  {t:.1f}s: {marker} {e:.4f} {bar}")




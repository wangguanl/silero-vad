from silero_vad import load_silero_vad, read_audio, get_speech_timestamps

model = load_silero_vad()
wav = read_audio("tests/data/test.wav")
ts = get_speech_timestamps(wav, model, return_seconds=True)
print("speech_timestamps:")
for seg in ts:
    print(f"  start={seg['start']:.3f}s  end={seg['end']:.3f}s")
print(f"segments={len(ts)}")

import whisper

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio (use WAV or MP3)
result = model.transcribe("harvard.wav")

# Print result
print("Transcribed text:", result["text"])

from flask import Flask, render_template, request
from pydub import AudioSegment
import os
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""
    if request.method == "POST":
        if "audio_file" in request.files:
            audio = request.files["audio_file"]
            ext = audio.filename.split('.')[-1].lower()
            audio_path = f"temp.{ext}"
            wav_path = "temp.wav"

            audio.save(audio_path)

            if ext == "mp3":
                sound = AudioSegment.from_mp3(audio_path)
                sound.export(wav_path, format="wav")
            elif ext == "wav":
                wav_path = audio_path
            else:
                return "Unsupported file format", 400

            # Use Whisper model
            result = model.transcribe(wav_path)
            transcription = result["text"]

            os.remove(audio_path)
            if os.path.exists("temp.wav"):
                os.remove("temp.wav")

    return render_template("index.html", transcription=transcription)

if __name__ == "__main__":
    app.run(debug=True)

# 🗣️ Speech Recognition System

This is a Flask-based web application that allows users to upload an audio file (MP3 or WAV) and receive the transcribed text using OpenAI’s **Whisper** model. The app features a clean, dark-themed UI with a loading spinner for smooth interaction.

---

## 🎯 Features

- Upload audio files (`.mp3` or `.wav`)
- Transcription powered by **OpenAI Whisper** (offline)
- Clean, responsive UI with dark theme
- CSS-only **loading animation** while processing
- Supports both desktop and mobile view

---

## 🚀 How It Works

1. The user uploads an audio file.
2. If the file is in MP3 format, it's converted to WAV using `pydub`.
3. The `whisper` model processes the audio and returns the transcription.
4. Transcribed text is displayed on the web page.

---

## 🧠 AI Model Used

- **OpenAI Whisper (base)** – Pretrained speech recognition model that works offline.
- Powered by **PyTorch**.
- No internet connection required during transcription.

---

## 💻 Tech Stack

- **Backend**: Python, Flask
- **AI/ML**: OpenAI Whisper, PyTorch
- **Frontend**: HTML, CSS
- **Audio Handling**: `pydub`, `ffmpeg`
- **Speech Processing**: `openai-whisper`

---

## 📁 Project Structure

```

speech\_to\_text\_app/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── (optional: CSS, JS files)
├── uploads/
│   └── (temporary audio files)
└── venv/
└── (not uploaded to GitHub; created locally)

````

> Add `venv/` to `.gitignore` to keep your repo clean.

---

## 🛠️ Setup Instructions (CMD Only)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/speech_to_text_app.git
cd speech_to_text_app
````

### Step 2: Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install flask openai-whisper pydub SpeechRecognition
```

---

## 🧪 Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📥 Output

After uploading your audio, the transcribed text will appear below the form. MP3s are automatically converted to WAV using `pydub`.

---

## ⚠️ Note on FFmpeg

FFmpeg is required for MP3-to-WAV conversion.

### How to set it up (Windows):

1. Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract the ZIP file.
3. Copy the full path to the `bin` folder (contains `ffmpeg.exe`).
4. Add this path to **Environment Variables > Path**.
5. Restart CMD and verify:

   ```bash
   ffmpeg -version
   ```


# 🌐 Multilingual Voice/Text Translator

A simple Python-based translator that supports both **text** and **voice input**. It translates between multiple languages and also speaks the translated result aloud using Google Text-to-Speech (`gTTS`).

---

## 🚀 Features

- 🎤 Voice input via microphone
- ⌨️ Text input via keyboard
- 🌍 Multilingual translation using `googletrans`
- 🔊 Text-to-speech output using `gTTS`
- 🖥️ Works directly from the terminal (console-based)
- 📢 Plays translated audio using your system's media player

---

## 🧱 Technologies Used

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [googletrans](https://pypi.org/project/googletrans/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- `asyncio` and `os` (Python built-in modules)

---

## 🛠️ Installation

1. **Clone this repository:**

```bash
git clone https://github.com/21Aditya-PY/your-repo-name.git
cd your-repo-name
```

2. **Install all dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run

> Make sure your microphone is connected and working.

### For Console Version (No UI):

```bash
python demo2.py
```

Then follow the on-screen prompts:
- Select input mode (voice or text)
- Enter source and target language codes
- Provide input text or speak when prompted

---

## 🌍 Supported Languages

Supported codes include:

| Code  | Language       |
|-------|----------------|
| en    | English        |
| hi    | Hindi          |
| fr    | French         |
| es    | Spanish        |
| de    | German         |
| zh-cn | Chinese (Simplified) |
| ja    | Japanese       |
| ru    | Russian        |
| ar    | Arabic         |
| pt    | Portuguese     |
| bn    | Bengali        |
| pa    | Punjabi        |

> All available options are listed when you run the app.

---

## ⚠️ Notes

- `os.system("start ...")` is Windows-specific. For macOS, use `afplay`; for Linux, use `xdg-open`.
- This project uses the free Google Translate API (`googletrans`). It may not be 100% reliable during high traffic or API rate limits.

---

## 👨‍💻 Author

Made with ❤️ by [Aditya Pathak](https://github.com/21Aditya-PY) 

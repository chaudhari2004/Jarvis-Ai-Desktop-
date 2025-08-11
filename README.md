
  
  # 🤖 **JARVIS – AI Desktop Personal Assistant**

  <sub>Voice-controlled • Smart • Powerful</sub>
  
  [![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  
  [![GitHub Stars](https://img.shields.io/github/stars/chaudhari2004/Jarvis-Ai-Desktop-?style=social)](https://github.com/chaudhari2004/Jarvis-Ai-Desktop-/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/chaudhari2004/Jarvis-Ai-Desktop-?style=social)](https://github.com/chaudhari2004/Jarvis-Ai-Desktop-/network/members)
</div>

---

## ✨ **What is JARVIS?**
JARVIS is a **Python-based voice assistant** that can execute commands, fetch information, open applications, control media, send emails, and more — all hands-free, just like Tony Stark’s AI in Iron Man 🦾.

---

## 🚀 **Key Features**

| Category              | What It Can Do |
|-----------------------|----------------|
| 🎙 **Voice Interaction** | Greet based on time ⏰, listen to commands 🎧, respond via TTS 🔊 |
| 🌤 **Weather Info** | Get real-time temperature & conditions ☀️🌧 |
| ⏰ **Alarms** | Set & trigger alarms ⏱ |
| 💻 **App Control** | Open Notepad 📝, Paint 🎨, type/draw automatically, close apps ❌ |
| 📺 **YouTube Control** | Search videos 🔍, play ▶️, pause ⏸, mute 🔇, adjust volume 🔊 |
| 📧 **Email Assistant** | Send 📤 & read 📥 emails |
| 📚 **Information** | Wikipedia summaries 📖, open ChatGPT 🌐 |
| 🖥 **System Control** | Quit JARVIS when told 📴 |

---

## 🛠 **Tech Stack**
- **Language:** Python 🐍
- **APIs:** OpenWeatherMap 🌦, Wikipedia API 📚
- **Libraries:**  
  `pyttsx3`, `SpeechRecognition`, `requests`, `wikipedia`, `pyautogui`,  
  `subprocess`, `smtplib`, `imaplib`, `email`, `datetime`, `os`, `time`, `webbrowser`

---

## ⚡ **Quick Start**

```bash
# 1️⃣ Clone the repository
git clone https://github.com/chaudhari2004/Jarvis-Ai-Desktop-.git
cd Jarvis-Ai-Desktop-

# 2️⃣ Create & activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# 3️⃣ Install dependencies
pip install pyttsx3 SpeechRecognition requests wikipedia-api pyautogui

# 4️⃣ Run the assistant
python jarvis.py

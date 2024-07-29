### Project: JARVIS Personal Assistant

#### Overview
This project involves creating a personal assistant named JARVIS using Python. JARVIS is capable of performing various tasks based on voice commands. The features include fetching weather information, setting alarms, opening applications, performing tasks in Notepad and Paint, controlling YouTube playback, sending and reading emails, and more.

#### Features
1. **Voice Interaction:**
   - JARVIS can interact with users using text-to-speech (TTS) and speech recognition.
   - It can greet the user based on the time of day.

2. **Weather Information:**
   - Fetches and announces the current temperature for a specified city using the OpenWeatherMap API.

3. **Alarm:**
   - Sets and rings an alarm at the specified time.

4. **Application Control:**
   - Opens and interacts with applications like Notepad and Paint.
   - Types text in Notepad and draws shapes in Paint.
   - Closes Notepad and Paint applications.

5. **YouTube Control:**
   - Searches for videos on YouTube.
   - Plays, pauses, mutes, and adjusts the volume of YouTube videos.
   - Closes YouTube tabs.

6. **Email:**
   - Sends emails using SMTP.
   - Reads the latest emails from the inbox using IMAP.

7. **Information Retrieval:**
   - Fetches summaries from Wikipedia.
   - Opens ChatGPT in a web browser and performs searches.

8. **System Control:**
   - Quits the program based on voice commands.

#### Required Libraries
- **pyttsx3:** Text-to-speech conversion library.
- **speech_recognition:** Library for recognizing speech input from the microphone.
- **datetime:** Module for working with date and time.
- **webbrowser:** Provides a high-level interface to allow displaying Web-based documents to users.
- **os:** Provides functions for interacting with the operating system.
- **time:** Time-related functions.
- **requests:** Library for making HTTP requests to interact with APIs.
- **wikipedia:** Python wrapper for the Wikipedia API.
- **pyautogui:** Allows for controlling the mouse and keyboard to automate tasks.
- **subprocess:** Allows for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.
- **smtplib:** Defines an SMTP client session object used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
- **imaplib:** Implements the client side of the IMAP4 protocol.
- **email:** Package for managing email messages, including MIME and other RFC 2822-based message documents.

#### Importing Libraries in VS Code
To use the required libraries in VS Code, follow these steps:

1. **Install VS Code Extensions:**
   - Open VS Code.
   - Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
   - Search for and install the following extensions:
     - **Python** by Microsoft: Provides IntelliSense (Pylance), linting, debugging, and other features for Python development.
     - **Pylance** by Microsoft: Provides rich Python editing features like IntelliSense and type checking.

2. **Install Python:**
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Create a Virtual Environment (Optional but Recommended):**
   - Open a terminal in VS Code (`Ctrl+``).
   - Navigate to your project directory.
   - Create a virtual environment using the following command:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Libraries:**
   - With the virtual environment activated, install the required libraries using pip:
     ```bash
     pip install pyttsx3 SpeechRecognition requests wikipedia-api pyautogui
     ```
   - For email functionality, the required libraries (smtplib, imaplib, email) are included in the Python standard library and do not need to be installed separately.

5. **Configure VS Code:**
   - Open the Command Palette (`Ctrl+Shift+P`).
   - Type `Python: Select Interpreter` and choose the interpreter from your virtual environment.
   - Optionally, you can create a `.vscode/settings.json` file in your project directory with the following content to automatically select the interpreter:
     ```json
     {
       "python.pythonPath": "venv/Scripts/python.exe"  // Adjust path based on your OS and virtual environment location
     }
     ```

6. **Import Libraries in Your Code:**
   - At the beginning of your Python script, import the required libraries:
     ```python
     import pyttsx3
     import speech_recognition as sr
     import datetime
     import webbrowser
     import os
     import time as time_module
     import requests
     import wikipedia
     import pyautogui
     import subprocess
     import smtplib
     import imaplib
     import email
     ```

7. **Run Your Code:**
   - You can run your Python script by opening the terminal in VS Code and using the command:
     ```bash
     python your_script_name.py
     ```
   - Alternatively, you can click the `Run` button in the top right corner of the editor or use the shortcut `F5`.


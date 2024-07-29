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

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

# Constants
OPENWEATHERMAP_API_KEY = 'e04887e20bd237b71dafd0668b09ca6b'  # Replace with your OpenWeatherMap API key

# Email credentials (example)
EMAIL_ADDRESS = 'chaudharivivek2004@gmail.com'
EMAIL_PASSWORD = 'Vivekc@2004'

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning, sir !")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir!")
    else:
        speak("Good Evening, sir!")
    speak("I am JARVIS. How can I assist you today?")

def take_command():
    """Listens for voice commands from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand the audio, please say that again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return query.lower()

def get_temperature(city_name):
    """Gets the temperature for a given city using OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        if "main" in data:
            main = data["main"]
            temperature = main["temp"]
            return temperature
        else:
            speak("Error: 'main' key not found in the API response.")
            return None
    elif response.status_code == 401:
        speak("Error: Unauthorized. Please check your API key.")
        return None
    else:
        speak(f"Error: API request failed with status code {response.status_code}.")
        return None

def ring(alarm_time):
    """Rings an alarm at the specified time."""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            break
        time_module.sleep(1)

def open_application(app_path):
    """Opens an application."""
    try:
        subprocess.Popen([app_path])
        return True
    except Exception as e:
        print(f"Error opening {app_path}: {e}")
        return False

def type_in_notepad(text):
    """Opens Notepad and types the provided text."""
    if open_application("notepad.exe"):
        time_module.sleep(2)  # Wait for Notepad to open
        pyautogui.write(text, interval=0.1)  # Type the text with a small delay between each keystroke
    else:
        speak("Sorry, I could not open Notepad.")

def close_notepad():
    """Closes the Notepad application."""
    os.system("taskkill /f /im notepad.exe")  # Forcefully terminates Notepad process

def draw_in_paint():
    """Opens Paint and draws a shape."""
    if open_application("mspaint.exe"):
        time_module.sleep(2)  # Wait for Paint to open
        speak("What should I draw? A line, circle, or rectangle?")
        shape = take_command()

        if shape == "line":
            speak("Drawing a line.")
            draw_line()
        elif shape == "circle":
            speak("Drawing a circle.")
            draw_circle()
        elif shape == "rectangle":
            speak("Drawing a rectangle.")
            draw_rectangle()
        else:
            speak("I didn't understand the shape. Please try again.")
    else:
        speak("Sorry, I could not open Paint.")

def draw_line():
    """Draws a line in Paint."""
    pyautogui.click(50, 50)  # Coordinates for the pencil tool
    time_module.sleep(1)
    pyautogui.moveTo(300, 300)
    pyautogui.dragTo(600, 300, duration=1)  # Adjust the coordinates as needed

def draw_circle():
    """Draws a circle in Paint."""
    pyautogui.click(80, 60)  # Coordinates for the ellipse tool (adjust accordingly)
    time_module.sleep(1)
    pyautogui.moveTo(300, 300)
    pyautogui.dragTo(500, 500, duration=1)  # Adjust the coordinates as needed

def draw_rectangle():
    """Draws a rectangle in Paint."""
    pyautogui.click(100, 60)  # Coordinates for the rectangle tool (adjust accordingly)
    time_module.sleep(1)
    pyautogui.moveTo(300, 300)
    pyautogui.dragTo(500, 400, duration=1)  # Adjust the coordinates as needed

def fill_color():
    """Fills color in the shape."""
    pyautogui.click(50, 150)  # Coordinates for the fill tool
    speak("Which color would you like to fill?")
    color = take_command()

    if color == "red":
        pyautogui.click(100, 200)  # Coordinates of the red color
    elif color == "blue":
        pyautogui.click(120, 200)  # Coordinates of the blue color
    elif color == "green":
        pyautogui.click(140, 200)  # Coordinates of the green color
    else:
        speak("Color not recognized. Please try again.")
        return

    # Fill the color
    pyautogui.click(250, 250)  # Coordinates to fill the shape

    

def close_paint():
    """Closes the Paint application."""
    os.system("taskkill /f /im mspaint.exe")  # Forcefully terminates Paint process

def close_youtube():
    """Closes the YouTube tab and switches back to the previous application."""
    pyautogui.hotkey('ctrl', 'w')  # Close the current tab in the browser
    pyautogui.hotkey('alt', 'tab')  # Switch back to the previous application

def search_youtube(query):
    """Searches for a query on YouTube."""
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def youtube_control(command):
    """Controls YouTube playback."""
    if 'play' in command or 'pause' in command:
        pyautogui.press('k')  # Play/pause the video
    elif 'volume up' in command:
        pyautogui.hotkey('ctrl', 'up')  # Increase volume
    elif 'volume down' in command:
        pyautogui.hotkey('ctrl', 'down')  # Decrease volume
    elif 'mute' in command:
        pyautogui.press('m')  # Mute/unmute video

def open_and_play_youtube(query):
    """Opens YouTube and plays a specific video if the command includes 'play'."""
    if 'play' in query:
        search_term = query.replace("play", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
        time_module.sleep(2)  # Give some time for the page to load
        pyautogui.press('enter')  # Press enter to play the first video
    else:
        webbrowser.open("https://www.youtube.com")

def open_chatgpt():
    """Opens ChatGPT in a web browser."""
    webbrowser.open("https://chatgpt.com")

def search_chatgpt(query):
    """Searches for a query in ChatGPT."""
    open_chatgpt()
    time_module.sleep(5)  # Wait for the page to load
    pyautogui.write(query)
    pyautogui.press('enter')

def send_email(recipient, subject, body):
    """Send an email using SMTP."""
    try:
        server = smtplib.SMTP('https://mail.google.com/mail/u/0/#inbox', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_ADDRESS, recipient, message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. Error: {e}")

def read_emails():
    """Reads the latest emails from the inbox."""
    try:
        mail = imaplib.IMAP4_SSL("https://mail.google.com/mail/u/0/#inbox")
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select("inbox")
        _, data = mail.search(None, "ALL")
        email_ids = data[0].split()
        latest_email_id = email_ids[-1]

        _, email_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        sender = email.utils.parseaddr(email_message['From'])[1]
        subject = email_message['Subject']
        speak(f"Latest email from {sender}. Subject: {subject}")
        mail.logout()
    except Exception as e:
        speak(f"Failed to retrieve emails. Error: {e}")

def quit_program():
    """Quits the program."""
    speak("Goodbye! Thank you. Have a nice day.")
    os._exit(0)

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query is None:
            continue

        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif 'set an alarm' in query:
            alarm_time = query.replace("set an alarm for", "").strip()
            speak(f"Setting an alarm for {alarm_time}")
            ring(alarm_time)

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            open_and_play_youtube(query)

        elif 'type in notepad' in query:
            speak("What should I type?")
            text = take_command()
            if text:
                type_in_notepad(text)

        elif 'close notepad' in query or 'close the notepad' in query:
            speak("Closing Notepad")
            close_notepad()

        elif 'draw in paint' in query:
            speak("Drawing in Paint")
            draw_in_paint()

        elif 'close paint' in query or 'close the paint' in query:
            speak("Closing Paint")
            close_paint()

        elif 'close youtube' in query or 'close the youtube' in query:
            speak("Closing YouTube")
            close_youtube()

        elif 'search on youtube' in query:
            speak("What should I search for?")
            search_query = take_command()
            if search_query:
                search_youtube(search_query)

        elif 'control youtube' in query:
            speak("What should I do? Play, pause, volume up, volume down or mute?")
            youtube_command = take_command()
            if youtube_command:
                youtube_control(youtube_command)

        elif 'temperature' in query:
            speak("Which city?")
            city_name = take_command()
            if city_name:
                temperature = get_temperature(city_name)
                if temperature is not None:
                    speak(f"The temperature in {city_name} is {temperature} degrees Celsius")
                else:
                    speak("Sorry, I couldn't find the temperature for that city.")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The term is ambiguous, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif 'send email' in query:
            speak("To whom should I send the email?")
            recipient = take_command()
            speak("What is the subject of the email?")
            subject = take_command()
            speak("What should I say in the email?")
            body = take_command()
            send_email(recipient, subject, body)

        elif 'read email' in query or 'check email' in query:
            read_emails()

        elif ' open chatgpt' in query:
            speak("Opening ChatGPT")
            open_chatgpt()

        elif 'search chatgpt' in query:
            speak("What should I search for?")
            chatgpt_query = take_command()
            if chatgpt_query:
                search_chatgpt(chatgpt_query)

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            quit_program()

        else:
            speak("I am not sure how to help with that. Please try asking something else.")

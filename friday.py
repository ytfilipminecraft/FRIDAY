import speech_recognition as sr
import pyttsx3
import subprocess
import datetime
import webbrowser
import os

# ===== HLAS =====
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    print("FRIDAY:", text)

    engine.stop()  # reset hlasu

    engine.say(text)
    engine.runAndWait()

# ===== POSLECH =====
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="cs-CZ")
        print("Ty:", text)
        return text.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak("Chyba připojení k hlasové službě.")
        return ""

# ===== PŘÍKAZY =====
def run_command(command):

    # DISCORD
    if "discord" in command:
        speak("Otevírám Discord.")
        try:
            subprocess.Popen([
                os.path.expandvars(
                    r"%LocalAppData%\Discord\Update.exe"
                ),
                "--processStart",
                "Discord.exe"
            ])
        except:
            speak("Discord se nepodařilo otevřít.")

    # CHROME
    elif "chrome" in command:
        speak("Otevírám Chrome.")
        try:
            subprocess.Popen(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
        except:
            webbrowser.open("https://google.com")

    # YOUTUBE
    elif "youtube" in command:
        speak("Otevírám YouTube.")
        webbrowser.open("https://youtube.com")

    # MINECRAFT
    elif "minecraft" in command:
        speak("Spouštím Minecraft.")
        try:
            os.startfile(
                r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"
            )
        except:
            speak("Minecraft se nepodařilo otevřít.")

    # OBS
    elif "obs" in command or "obs studio" in command:
        speak("Otevírám OBS Studio.")
        try:
            subprocess.Popen(
                r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
            )
        except:
            speak("OBS Studio se nepodařilo otevřít.")

    # ČAS
    elif "kolik je hodin" in command or "čas" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Aktuální čas je {now}")

    # POČASÍ (základ)
    elif "počasí" in command:
        speak("Otevírám počasí.")
        webbrowser.open("https://www.google.com/search?q=počasí")

    # UKONČENÍ
    elif "ukonči se" in command:
        speak("Vypínám se.")
        exit()

    else:
        speak("Příkaz nerozpoznán.")

# ===== START =====
speak("FRIDAY online.")

# ===== WAKE WORD LOOP =====
while True:

    text = listen()

    if "friday" in text:
        speak("Ano?")

        # malá pauza aby neslyšela sama sebe
        import time
        time.sleep(0.7)

        command = listen()
        run_command(command)

# import pyttsx3
import speech_recognition as sr
import subprocess
# import requests
# import json
# from weather import Speak
from timeParser import get_time, Speak
from quoteParser import Quotes
from ticketonParser import get_films
from gismeteoParser import get_weather

# TOKEN = '302cd93571f7e72c3dba77940967b189'

# def Speak(text):
#     engine = pyttsx3.init()
#     voice = engine.getProperty('voices')
#     engine.setProperty('voice', voice[1].id)
#     # rate = engine.getProperty('rate')
#     # engine.setProperty('rate', rate+10)
#     engine.say(text)
#     print(text)
#     engine.runAndWait()

def start_sr():
    while True:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                # recognizer.energy_threshold(mic,)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio, language='en-US')
                text = text.lower()

                print(text)
                
                if "stop" in text or "bye jarvis" in text:
                    break
                response(text)
        except sr.UnknownValueError:
            print("Didn't catch that..")
            recognizer = sr.Recognizer()
            continue


def response(text):
    if text == "jarvis" or text == "hey jarvis" or text == 'hey jarvis hey jarvis' or "hello jarvis" in text or text == "travis" or text == 'hello':
        Speak('What, sir!')
    if text == "how are you":
        Speak('Good, sir')
    elif "how are you doing" in text or 'how you doing' in text:
        Speak('I am doing well, sir!')
        # elif "tell me a joke" in text or "tell a joke" in text:
        # Speak('Why do programmers prefer dark mode? Because light attracts bugs, sir')
    elif "open the youtube" in text or "open youtube" in text or " okay open the youtube" in text or "jarvis open the youtube" in text or "jarvis opens youtube" in text:
        Speak('Yeap!')
        # subprocess.Popen(['C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\AutoHotkey Dash.lnk', 'C:\\Users\\Ernar\\Documents\\JarvisBot\\opp.exe'], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run('opp.exe')
    elif "study mode" in text or  "study mood" in text or  "jarvis study mode" in text:
        Speak('Yeap!')
        subprocess.run('studymode.exe')
    elif "jarvis check the marks" in text or "check the marks" in text or "jarvis check marks" in text:
        Speak('Yeap!')
        subprocess.run('markchecker.exe')
    elif "tell me the weather" in text or "weather in" in text or "weather" in text:
        # city_name = str(text.split()[-1])
        # print(city_name)
        # get_weather(city_name, TOKEN)
        get_weather()
    elif "tell me the time" in text or "time" in text:
        get_time()
    elif "tell me a joke" in text or "tell a joke" in text or 'tell joke me' in text or 'me joke tell' in text or 'joke tell me' in text or 'joke me' in text:
        Quotes('humor')
    # elif 'list of current films' in text or 'current films' in text:




# if __name__ == "__main__":
start_sr()

# Speak('Hello, sir!')







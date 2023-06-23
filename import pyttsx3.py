

from math import e
from typing import Pattern
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import features
import news_module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Warm Morning!")

    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    else:
        speak("good evening")

    speak("This is enigma at your service ,how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:

        print("pardon....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("as per wikipedia")
            print(results)
            speak(results)
        elif 'play youtube video' in query:
            webbrowser.open("https://youtu.be/2r19NAhhjRY?t=895")

        elif 'open google' in query:
            speak("how can i help you sir ")
            xr = takeCommand().lower()

            webbrowser.open(f"{xr}")
        elif 'play music' in query:
            music_directory = 'C:\\New folder'
            songs = os.listdir(music_directory)
            rdc = random.choice(songs)

            print(songs)
            os.startfile(os.path.join(music_directory, rdc))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send message' in query:
            pywhatkit.sendwhatmsg(
                "+917843023699", "Enigma at your service", 9, 6)

        elif 'pattern' in query:
            codePath = "C:\\New folder (2)\\pattern.py"
            os.startfile(codePath)

        elif 'yourself' in query:
            speak('my name    is enigma    my      creators      are Aryan    and   Tejas and    the libraries    used to     create me are     pyttsx3,   speech_recognition  DateTime,  wikipedia  ,webbrowser,   os,   random,pywhatkit,features')

        elif 'program' in query:
            codePath = "C:\\New folder (2)\\import turtle.py"
            os.startfile(codePath)

        elif 'examples' in query:
            codePath = "C:\\New folder (2)\\y.py"
            os.startfile(codePath)

        elif 'calculator' in query:
            codePath = "C:\\New folder (2)\\calculator.py"
            os.startfile(codePath)

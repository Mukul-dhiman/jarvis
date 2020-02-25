"""
Created on Fri Jan 17 13:22:58 2020

@author: Mukul
"""
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id) #1 for man 0 for girl

""" RATE"""
rate = engine.getProperty('rate')  
engine.setProperty('rate', 150)    


"""VOLUME"""
volume = engine.getProperty('volume')                           
engine.setProperty('volume',2.0)   

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecomment():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recongnizing")
        query = r.recognize_google(audio)
        print(f"you said: {query}\n")
    except Exception as e:
        print(e)
        print("Say again...")
        return "none"
    return query
def start_jarvis():
    speak("jarwis on your service sir")
    x=1
    while(x==1):
        query = takecomment().lower()
        if 'wikipedia' in query:
            query = query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=1)
            speak("accordin to wikipedia")
            print(results)
            speak(results)
        elif 'open' in query:
            query=query.replace('open',"")
            query=query.replace(' ',"")
            url=query+".com"
            webbrowser.open(url)
        elif 'google search' in query:
            query=query.replace(' google search ',"")
            query=query.replace('google search ',"")
            query=query.replace('google search ',"")
            query=query.replace(' ',"+")
            url="https://www.google.com/search?q="+query
            webbrowser.open(url)
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is {strtime}")
        if query == "stop":
            x=0
            speak("closing jarwis")
start_jarvis()
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id);


def speak(audio):
    engine.say(audio);
    engine.runAndWait();

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("Good Morning!");

    elif hour>=12 and hour<18:
        speak("Good Afternoon!");

    else:
        speak("Good evening!");

    speak("I am Stella, Please tell me how may I help you.")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......");
        r.pause_threshold = 1;
        audio = r.listen(source);

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in');
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please....");
        return "None"
    return query;

if __name__ == '__main__':
    wishMe();
    while True:
        query = takeCommand().lower();

        # Logic for executing the task based on the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia ")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Nikhil Gorule\\Music';
            songs = os.listdir(music_dir);
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


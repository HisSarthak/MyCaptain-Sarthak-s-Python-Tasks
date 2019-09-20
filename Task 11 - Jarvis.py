import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from selenium import webdriver

engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices');
##print(voices);
engine.setProperty('voice', voices[0].id);
engine.setProperty('volume', 100);
engine.setProperty('rate', 190);

def speak(audio):
    print(audio);
    engine.say(audio);
    engine.runAndWait();


def wishMe():
    hour = int(datetime.datetime.now().hour);
    if hour >=0 and hour <12:
        speak("Good Morining Sir");

    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir");

    else:
        speak("Good Evening Sir");

    speak("I am Kentil, How can I help you??")


def takeCommand():
    #It Takes Microphone Input
    r=sr.Recognizer();
    with sr.Microphone() as source:
        print("Listening...");
        r.pause_threshold = 0.5;
        audio = r.listen(source);

    try:
        print("Recognizing...");
        query = r.recognize_google(audio, language='en-in');
        print(f"User said: {query}\n");

    except Exception as e:
        print("ERROR:",e);

        print("Say that again please...");
        return "None";
    return query;

def OpenInChrome(url):
    chromedir = "C:\Program Files\Google\Chrome\Application\chrome.exe";
    webbrowser.Chrome(name=chromedir).open(url,2);

if __name__ == "__main__":
    wishMe();
    
    while True:
        query = takeCommand().lower();
    
        """ Logic for executin tasks based on query """
        if 'wikipedia' in query:
            speak('Searching wikipedia...');
            query = query.replace("wikipedia", "");
            results = wikipedia.summary(query, sentences=2);
            speak("According to Wikipedia");
            speak(results);

        elif 'open youtube' in query:
            speak('Opening Youtube...');
            OpenInChrome("youtube.com");

        elif 'open google' in query:
            speak('Opening Google...');
            OpenInChrome("google.com");

        #elif 'open spotify' in query:
            #speak('Opening Spotify...');
            #OpenInChrome("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fbrowse%2Ffeatured");
            
        elif 'open beautiful audio editor' in query:
            speak('Opening Beautiful Audio Editor');
            OpenInChrome("https://beautifulaudioeditor.appspot.com/app");
        elif 'open audio editor online' in query:
            speak('Opening Beautiful Audio Editor');
            OpenInChrome("https://beautifulaudioeditor.appspot.com/app");
        elif 'open online audio editor' in query:
            speak('Opening Beautiful Audio Editor');
            OpenInChrome("https://beautifulaudioeditor.appspot.com/app");

        elif 'github' in query:
            speak('Opening Github');
            OpenInChrome("https://github.com/HisSarthak?tab=repositories");
        
        elif 'open cloud convert' in query:
            speak('Opening Cloud Convert');
            OpenInChrome("cloudconvert.com");

        elif 'open gmail' in query:
            speak('Opening Gmail');
            OpenInChrome("https://mail.google.com/mail/u/0/#inbox");

        elif 'exit' in query:
            speak('Ok Bye Sir');
            exit();

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import urllib
from urllib.request import urlopen

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

    speak("I am Trophin, How can I help you??")


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

        speak("Say that again please...");
        return "None";
    return query;

def OpenInChrome(url):
    chromedir = "C:\Program Files\Google\Chrome\Application\chrome.exe";
    webbrowser.Chrome(name=chromedir).open(url,2);

def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1);
        return True;
    except urllib.error.URLError as e:
        return False;

def search(str):
    if 'for' in str:
        subquery=str.split(' for ');
        str1=subquery[1];
    elif 'search' in str:
        subquery=str.split(' search ');
        str1=subquery[1];
    else:
        subquery=str.split(' ');
        str1=' '.join(subquery[1:]);
    link=prelink + str1;
    OpenInChrome(link);

if __name__ == "__main__":
    if is_internet():

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

            elif 'youtube' in query:
                prelink="https://www.youtube.com/results?search_query=";
                search(query);
                speak('Opening Youtube...');
            
            elif 'search' in query:
                if 'google' in query:
                    prelink="https://www.google.com/search?q=";
                    search(query);
                elif 'youtube' in query:
                    prelink="https://www.youtube.com/results?search_query=";
                    search(query);
                else:
                    speak("Sorry Sir. Some error has occured");
                    speak("Please try again.");

            elif 'Google' in query:
                prelink="https://www.google.com/search?q=";
                search(query);
                speak('Opening Google...');

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

            elif 'stop listening' in query:
                speak('Ok Sir, I will be ready for further commands');
                break;
    else:
        speak("Sorry sir, seems like you are disconnected.\nPlease check Your connection and try again");
        exit();

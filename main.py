import speech_recognition as sr
from time import ctime
import webbrowser

r = sr.Recognizer()

def recordAudio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnKnownValueError:
            print('Sorry, I did not understand')
        except sr.RequestError:
            print('Sorry, my speech service is down')    
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is Bot")
    if 'what time is it' or 'what is the time' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = recordAudio('What would you like me to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here are the results that I have found for ' + search)
        
print('How can I help you?')
voice_data = recordAudio()
respond(voice_data)
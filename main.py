import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random 
from gtts import gTTS 

r = sr.Recognizer()

def recordAudio(ask = False):
    with sr.Microphone() as source:
        if ask:
            bot_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnKnownValueError:
            bot_speak('Sorry, I did not understand')
        except sr.RequestError:
            bot_speak('Sorry, my speech service is down')    
    return voice_data

def bot_speak(audio_string):
    tts = gTTS(text = audio_string, lang ='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    
def respond(voice_data):
    if 'what is your name' in voice_data:
        bot_speak("My name is Bot")
    if 'what time is it' in voice_data:
        bot_speak(ctime())
    if 'search' in voice_data:
        search = recordAudio('What would you like me to search?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        bot_speak('Here are the results that I have found for ' + search)
    if 'find location' in voice_data:
        location = recordAudio('What location would you like me to find?')
        url = 'https://www.google.ml/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        bot_speak('Here are the location results that I have found for ' + location) 
    if 'exit' in voice_data:
        exit()
  
time.sleep(1) 
bot_speak('How can I help you?')
while 1:
    voice_data = recordAudio()
    respond(voice_data)
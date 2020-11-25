import speech_recognition as sr # recognise speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import time
import os # to remove created audio files


r = sr.Recognizer() # initialise a recogniser
print('Speak...')

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            print(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
            #print(voice_data) # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            print('Sorry, the service is down') # error: recognizer is not connected
        print(voice_data) # print what user said
        return voice_data

# get string and make a audio file to be played


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you ", "hey, what's up? ", "I'm listening ", "how can I help you? ", "hello "]
        greet = greetings[random.randint(0,len(greetings)-1)]
        print(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        print("my name is Alexa")


    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        print("I'm very well, thanks for asking ")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + ':' + minutes
        print('The time is '+time )

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        print('Here is what I found for '+search_term+' on google\n')

    # 6: search youtube
    if there_exists(["open YouTube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query="+search_term
        webbrowser.get().open(url)
        print('Here is what I found for '+search_term+' on youtube\n')

    if there_exists(["find location"]):
        search_term = voice_data.split("location")[-1]
        url = "https://google.nl/maps/place/" + search_term +'/&amp;'
        webbrowser.get().open(url)
        print('Here is what I found for '+search_term+' on google maps\n')
   
    if there_exists(["exit", "quit", "goodbye"]):
        print("going offline\n")
        exit()


time.sleep(2)

while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
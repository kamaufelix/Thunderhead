import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import

listener = sr.Recognizer()
engine = pyttsx3.init()
AI = 'Alpha'

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say('Hello. I am ' + AI + ', how can I help you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print(AI + ' Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        print('fuck')
    return command

def run_asistant():
    command = take_command()
    if 'play' in command:
        song = command.replace('play ', '')
        print('playing' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif AI in command:
        command = command.replace(AI, '')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'search on wikipedia about' in command:
        info = command.replace('search on wikipedia about', '')
        talk('Searching information about ' + info)
        info = wikipedia.summary(info, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather' in command:
        weather = weather.
    else:
        talk('come again please')

while True:
    run_asistant()

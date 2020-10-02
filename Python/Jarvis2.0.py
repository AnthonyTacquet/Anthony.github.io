from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import wolframalpha
client = wolframalpha.Client("8K346X-HPX972TA7G")

import wikipedia

import PySimpleGUI as sg
sg.theme('LightBlue')
layout =[[sg.Text('Where can i help you with'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Jarvis', layout)

import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 155)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talkToMe(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();
    return command
def assistant(command):
    "if statements for executing commands"
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif "lock my PC" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")


    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')
        
    elif 'what is' in command:
        res = request.get(
            'https://www.wolframalpha.com/'
        if res.status_code == request.codes.ok:
            talkToMe(wolfram_res = next(client.query(values[0]).results).text)


    )

    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()
        if 'Geoffrey' in recipient:
            talkToMe('What should I say?')
            content = myCommand()
            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            #identify to server
            mail.ehlo()
            #encrypt session
            mail.starttls()
            #login
            mail.login('username', 'password')
            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)
            #end mail connection
            mail.close()
            talkToMe('Email sent.')
        else:
            talkToMe('I don\'t know what you mean!')
talkToMe('I am ready for your command')
#loop to continue executing multiple commands
while True:
    assistant(myCommand())
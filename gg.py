import pyttsx3
import speech_recognition
import wikipedia
from datetime import date, datetime
import webbrowser
import time
import os
from gtts import gTTS
import pyaudio
import playsound
i = 0
while True:
    hear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print('Listening:...')
        ai = 'Listening'
        audio = hear.record(mic, duration=3)
        ai = "..."
    try:
        you = hear.recognize_google(audio)
    except:
        you = ""
    if you == "":
        ai = "I can't hear you, Sir"
    elif "today" in you:
        today = date.today()
        ai = today.strftime("month: %B, day: %d , year: %Y ")
    elif "day" in you:
        today = date.today()
        ai = today.strftime("month: %B, day: %d , year: %Y ")
    elif "hello" in you:
        now = datetime.now()
        gio = int(now.strftime("%H"))
        if (gio > 0 and gio <= 9):
            chao = "Good morning, Sir. Can I have you?"
        elif (gio >= 10 and gio <= 18):
            chao = "Good afternoon, Sir. Can I have you?"
        else:
            chao = "Good evening, Sir. Can I have you?"
        ai = chao
    elif "hi" in you:
        now = datetime.now()
        gio = int(now.strftime("%H"))
        if (gio > 0 and gio <= 9):
            chao = "Good morning, Sir. Can I have you?"
        elif (gio >= 10 and gio <= 18):
            chao = "Good afternoon, Sir. Can I have you?"
        else:
            chao = "Good evening, Sir. Can I have you?"
        ai = chao
    elif "time" in you:
        now = datetime.now()
        ai = now.strftime("%H Hours %M Minutes %S Seconds")
    elif 'how are you' in you:
        ai = "I'm fine, thank you, Sir"
    elif 'how old are you' in you:
        ai = "I'm zero year old"
    elif "thank" in you:
        ai = 'You are welcome'
        print('Me:', you)
        print('AI:', ai)
        aispeak = pyttsx3.init()
        aispeak.say(ai)
        aispeak.runAndWait()
        break
    elif "name" in you:
        ai = "My name is Peter, I'm your robot, Sir"
    elif 'sleep 10 second' in you:
        ai = 'Finish'
        time.sleep(10)
    elif 'sleep 1 minute' in you:
        ai = 'Finish'
        time.sleep(60)
    elif 'shut down' in you:
        os.system('shutdown -s')
    elif 'restart' in you:
        os.system('shutdown -r')
    elif "live" in you:
        webbrowser.open(
            'https://www.youtube.com/channel/UCc_gMV4N9vJtpy7GcMUHaVw', new=1)
        ai = "Ok!"

    elif "program" in you:
        webbrowser.open(
            'https://www.youtube.com/channel/UCMYT8xymrm4VOP241b86MCQ', new=1)
        ai = "ok!"

    elif "YouTube" in you:
        webbrowser.open('https://www.youtube.com', new=1)
        ai = "ok! Opening YouTube"

    elif "Google" in you:
        webbrowser.open('https://www.google.com.vn/', new=1)
        ai = "ok! Opening Google"

    elif "music" in you:
        webbrowser.open(
            'https://www.youtube.com/results?search_query=music', new=1)
        ai = "ok! "

    elif "EDM" in you:
        webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA', new=1)
        ai = "ok!"

    elif "Facebook" in you:
        webbrowser.open('https://www.facebook.com/', new=1)
        ai = "ok! Opening Facebook"

    elif "Gmail" in you:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=1)
        ai = "ok!"

    elif "bye" in you:
        ai = 'GoodBye'
        print('Me:', you)
        print('AI:', ai)
        aispeak = pyttsx3.init()
        aispeak.say(ai)
        aispeak.runAndWait()
        break
    elif "okay" in you:
        ai = 'GoodBye'
        print('Me:', you)
        print('AI:', ai)
        aispeak = pyttsx3.init()
        aispeak.say(ai)
        aispeak.runAndWait()
        break
    elif 'Wikipedia' in you:
        hear = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            print("Wikipedia: ...")
            audio = hear.record(mic, duration=3)
        try:
            wiki = hear.recognize_google(audio)
        except:
            wiki = 'Sorry'
        wikipedia.set_lang("vi")
        wiki = wikipedia.summary(wiki)
        print(wiki)
        ai = wiki
        output = gTTS(ai, lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        ai = 'Đến đây là hết thông tin'
        time.sleep(3)
        continue
    else:
        ai = 'Sorry!'
    print('Me:', you)
    print('AI:', ai)
    aispeak = pyttsx3.init()
    aispeak.say(ai)
    aispeak.runAndWait()

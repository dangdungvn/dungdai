import speech_recognition as sr
import pyttsx3
from datetime import date,datetime
from gtts import gTTS
import pyaudio
import playsound
import os
import datetime
import time
import wikipedia
import webbrowser

laika_mouth = pyttsx3.init()
laika_brain =""

x = datetime.datetime.now()
thoigian = int(x.strftime("%H"))
if 5 < thoigian < 12 :
	loichao = "Chào buổi sáng tốt lành "
elif 12 <= thoigian < 13:
	loichao = "Nghỉ trưa thôi "
elif 13 <= thoigian < 17:
	loichao = "Chào buổi chiều "
elif 18 <= thoigian < 23:
	loichao = "Chào buổi tối "
elif thoigian >= 23:
	loichao = "Đêm rồi đi ngủ thôi "


def wiki(keyword):
    try:
        print('**đang tim kiem tren wiki**')
        print(wikipedia.summary(keyword))       
    except:
        print('Không mở được.')
        print('')
    run = False



i=0
while i<3:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("laika: Mời bạn nói: ")
		audio = r.listen(source,timeout=3, phrase_time_limit=3)
		print("laika:...")
		try: 
			you = r.recognize_google(audio,language="vi-VI")
			print("You -->: {}".format(you))
		except:
			i=i+1
			print("laika: Xin lỗi! tôi không nhận được voice!")
			laika_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			os.remove('output.mp3')
			continue
		if "chào" in you:
			laika_brain = loichao + "Tôi là laika, trợ lý ảo của bạn. Bạn cần giúp gì không"
			print("laika: ",laika_brain)
		if "tuổi" in you:
			laika_brain = "Tôi chưa sinh nhật lần nào hết"
			print("laika: ", laika_brain)
		elif "ngày" in you:
			today = date.today()
			laika_brain = today.strftime("Hôm nay là ngày: %d tháng %m năm %Y")
			print ("laika: ", laika_brain)
		elif "giờ" in you:
			giờ = time.localtime()
			laika_brain= time.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y='ờ')
			print ("laika: ",laika_brain)
		elif "trực tiếp" in you:
			webbrowser.open('https://www.youtube.com/channel/UCc_gMV4N9vJtpy7GcMUHaVw',new=1)
			laika_brain="Ok! Dũng C T đang được mở"
			print('Me:',you)
			print('AI:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "lập trình" in you:
			webbrowser.open('https://www.youtube.com/channel/UCMYT8xymrm4VOP241b86MCQ',new=1)
			laika_brain="Ok! Dũng lại lập trình đang được mở"
			print('Me:',you)
			print('AI:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		
		elif "Youtube" in you:
			webbrowser.open('https://www.youtube.com',new=1)
			laika_brain="Ok!Youtbe đang được mở"
			print('Me:',you)
			print('AI:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "Chrome" in you:
			webbrowser.open('https://www.google.com.vn/',new=1)
			laika_brain="Ok!Google đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "music" in you:
			webbrowser.open('https://www.youtube.com/results?search_query=music',new=1)
			laika_brain="Ok!Nhạc đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "edm" in you:
			webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=1)
			laika_brain="Ok!EDM đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Facebook" in you:
			webbrowser.open('https://www.facebook.com/',new=1)
			laika_brain="Ok!facebook đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break

		elif "Gmail" in you:
			webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=1)
			laika_brain="Ok!Gmail đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		
		elif "Wikipedia" in you:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				print("Wikipedia: ...")
				audio = r.listen(source,timeout=5, phrase_time_limit=5)
			try:
				wiki = r.recognize_google(audio,language="vi-VI")
			except:
				wiki='Sorry'
			wikipedia.set_lang("vi")
			wiki=wikipedia.summary(wiki)
			print(wiki)
			laika_brain=wiki
			
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			os.remove('output.mp3')
			laika_brain='Đến đây là hết thông tin'
			time.sleep(3)
			continue
		

		elif "Flappy Bird" in you:
			os.system('python fly.py')
			laika_brain='Đang mở game'	
		elif 'nghỉ 10 giây' in you:
			laika_brain='Finish'
			time.sleep(10)

		elif 'nghỉ 1 phút' in you:
			laika_brain='Finish'
			time.sleep(60)

		elif 'tắt máy' in you:
			os.system('shutdown -s')

		elif 'khởi động lại' in you:
			os.system('shutdown -r')

		elif "tạm biệt" in you:
			laika_brain = "Tạm biệt bạn, hẹn gặp lại"
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		else:
			laika_brain = "Xin lỗi phần này tôi chưa được học"

		output = gTTS(laika_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		os.remove('output.mp3')
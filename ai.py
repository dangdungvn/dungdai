import speech_recognition as sr
from datetime import date,datetime
from gtts import gTTS
import pyaudio
from playsound import playsound
import os
from datetime import date,datetime
import time
import wikipedia
import webbrowser
from pyowm import OWM
ai = ""
loichao = ""
x = datetime.now()
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
while True:
	r = sr.Recognizer()
	with sr.Microphone() as mic:
		print("AI: Mời bạn nói: ")
		audio = r.listen(mic)
		print("AI:...")
	try: 
		you = r.recognize_google(audio,language="vi-VI")
		print("You -->: {}".format(you))
	except:
		print("AI: Tôi không nghe đc bạn nói, Bạn nói lại được không?")
		ai = "Tôi không nghe được bạn nói, Bạn nói lại được không?"
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		continue
	if "chào" in you.lower():
		ai = loichao + ", Tôi là Đỗ Nam Trung, trợ lý ảo của bạn. Bạn cần tôi giúp gì không?"
		print("AI: ",ai)
	elif "tuổi" in you.lower():
		ai = "Tôi sinh ngày 16 tháng 7 năm 2020. Hiện tại tôi 0 tuổi"
		print("AI: ",ai)
	elif "ngày" in you.lower():
		today = date.today()
		fullnamnay = datetime.now()
		namnay = int(fullnamnay.strftime ("%Y"))
		sothu= today.weekday() +2
		thu= str(sothu)
		if thu=="8":
			thu="chủ nhật"
		ai ="hôm nay là thứ "+thu+today.strftime(" ngày %d tháng %m năm %Y")
		print("AI: ",ai)
	elif "thời gian" in you.lower():
		giờ = time.localtime()
		ai = time.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y="ờ")
		print ("AI: ",ai)
	elif "giờ" in you.lower():
		giờ = time.localtime()
		ai = time.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y="ờ")
		print ("AI: ",ai)
	elif "trực tiếp" in you.lower():
		webbrowser.open('https://www.youtube.com/channel/UCc_gMV4N9vJtpy7GcMUHaVw',new=1)
		ai ="Ok! Dũng C T đang được mở"
		print('Me:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break
	elif "lập trình" in you.lower():
		webbrowser.open('https://www.youtube.com/channel/UCMYT8xymrm4VOP241b86MCQ',new=1)
		ai ="Ok! Dũng lại lập trình đang được mở"
		print('Me:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break
	elif "thời tiết" in you.lower():
		owm = OWM('f582deb1c5ae0bf090fe4a6bf9f9d053')
		mgr = owm.weather_manager()
		observation= mgr.weather_at_place('Thanh Hoa,VN')
		weather = observation.weather
		w = weather.humidity
		temper= weather.temperature('celsius')['temp']
		t2= int(temper)
		t3=str(t2)
		ai = "nhiệt độ hiện tại là: " + t3 + " độ C. Độ ẩm là: " + str(w) + " %."
		print('AI:',ai)
	elif "Youtube" in you:
		webbrowser.open('https://www.youtube.com',new=1)
		ai ="Ok!Youtbe đang được mở"
		print('Me:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break

	elif "Chrome" in you:
		webbrowser.open('https://www.google.com.vn/',new=1)
		ai ="Ok!Google đang được mở"
		print('you:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break

	elif "music" in you:
		webbrowser.open('https://www.youtube.com/results?search_query=music',new=1)
		ai ="Ok!Nhạc đang được mở"
		print('you:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break

	elif "edm" in you:
		webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=1)
		ai ="Ok!EDM đang được mở"
		print('you:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=1)
		ai ="Ok!facebook đang được mở"
		print('you:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break

	elif "Gmail" in you:
		webbrowser.open('https://mail.google.com/',new=1)
		ai ="Ok!Gmail đang được mở"
		print('you:',you)
		print('AI:',ai)
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break
		
	elif "Wikipedia" in you or "wiki" in you.lower():
		r = sr.Recognizer()
		with sr.Microphone() as mic:
			print("Wikipedia: ...")
			audio = r.listen(mic)
		try:
			wiki = r.recognize_google(audio,language="vi-VI")
		except:
			wiki='Sorry'
		wikipedia.set_lang("vi")
		wiki=wikipedia.summary(wiki)
		print(wiki)
		ai =wiki
		i += 1	
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		ai ='Đến đây là hết thông tin'
		time.sleep(3)
		continue
	elif 'nghỉ 10 giây' in you.lower():
		ai ='Finish'
		time.sleep(10)
	elif 'nghỉ 1 phút' in you.lower():
		ai ='Finish'
		time.sleep(60)
	elif 'tắt máy' in you.lower():
		os.system('shutdown -s')
	elif 'khởi động lại' in you.lower():
		os.system('shutdown -r')
	elif "tạm biệt" in you.lower():
		ai = "Tạm biệt bạn, hẹn gặp lại"
		i += 1
		tts = gTTS(text = ai,lang = 'vi', slow = False)
		tts.save("AI" + str(i) + ".mp3")
		playsound("AI" + str(i) + ".mp3")
		os.remove("AI" + str(i) + ".mp3") 
		break
	else:
		ai = "Xin lỗi phần này tôi chưa được học"
	i +=1
	tts = gTTS(text = ai,lang = 'vi', slow = False)
	tts.save("AI" + str(i) + ".mp3")
	playsound("AI" + str(i) + ".mp3")
	os.remove("AI" + str(i) + ".mp3")
import os
import time
from colorama import Fore,Back,Style
from colorama import init,AnsiToWin32
import random
import sys
init(wrap= False)
stream= AnsiToWin32(sys.stderr).stream
def nho(string,n,m,sl):
	mau = Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.WHITE
	print(random.choice(mau)+'\n'.join(
		[' '.join(
		[
		(
		string[(x-y) % len(string)] if ((x*n)**2+(y*m)**2-1)**3-(x*n)**2*(y*m)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	time.sleep(s)
	os.system("cls")
def to(string,n,m):
	mau = Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.WHITE
	print(random.choice(mau)+'\n'.join(
		['  '.join(
		[
		(
		string[(x-y) % len(string)] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	os.system("cls")
def main():
	nho("ANH",0.03,0.7,0) #1
	nho("YEU",0.04,0.6,0) #2
	nho("EM",0.05,0.5,0) #3
	nho("I",0.06,0.4,0) #4
	nho("LOVE",0.07,0.3,0) #5
	nho("YOU",0.07,0.2,0) #6
	nho("SO",0.07,0.1,0.3) #7
	to("MUCH",0.07,0.09) #to1
	nho("ANH YEU EM",0.07,0.1,0) #nho1
	to("I LOVE YOU",0.07,0.09) #to2
	nho("SO MUCH",0.07,0.1,0) #nho2
	to("ANH YEU EM",0.07,0.09) #to3
	nho("ANH",0.07,0.1,0) #nho3
	to("YEU",0.07,0.09) #to4
	nho("EM",0.07,0.1,0) #nho4
	to("I",0.07,0.09) #to5
	nho("LOVE",0.07,0.1,0.3) #nho5
	nho("YOU",0.07,0.2,0) #6
	nho("LOVE LOVE",0.07,0.3,0) #5
	nho("YOU",0.06,0.4,0) #4
	nho("ANH YEU EM",0.05,0.5,0) #3
	nho("I LOVE YOU",0.04,0.6,0) #2
	nho("ANH YEU EM",0.03,0.7,0) #1
while True:
	main()

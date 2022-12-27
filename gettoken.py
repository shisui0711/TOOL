import os
import requests
from time import sleep
from time import sleep
from datetime import datetime
from datetime import date
import requests, os, sys, re, json
from threading import Thread
import json,requests,time
from pystyle import *
from pathlib import Path
__dir__: Path = Path(__file__).parent
def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''\n
    ╔═════════════════════════════════╗
    ║ ➽ Facebook : Nguyễn Văn Khang   ║ 
    ║ ➽ Zalo : 0988655794             ║
    ║ ➽ Youtube : Shisui0711          ║
    ║ ➽ Bản Quyền : Shisui0711        ║
    ║                                 ║
    ╚═════════════════════════════════╝                                                                                             
                               \n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(banner)))
s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+" "
banner()
acc=input(sr+"Nhập UID|PASS|2FA: ")
# uid=input(sr+"Nhập UID: ")
# pas=input(sr+"Nhập PASS: ")
# secret_key=input(sr+"Nhập 2FA: ")
# if secret_key !="":
#     secret_key= '|'+secret_key
# acc=uid+'|'+pas+secret_key
print(acc)
print(sr+"Định Dạng Token [EAAD/EAAV/EAAAAU/EAAC/EAAAAAY]")
loai = input(sr+"Vui Lòng Nhập Định Dạng Token Muốn Get: ")
re=requests.get(f"https://api.maihuybao.live/api/getToken?account={acc}&type={loai}").json()
try:
	token = re["access_token"]
except:
	exit()
with open(__dir__/'token.txt','a') as file:
    file.write(token+"\n")
print(sr+"Get thành công token vô file 'token.txt' ")

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
from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*1246546+23472)
key = 'NVK'+key1
url = 'https://khangpro.site/key.html?key='+key
token_link1s = 'c1a994eec33d0e0f31ed05afe1f42fb57dfc0202'
link1s = requests.get(f'https://link1s.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
	print(link1s['message'])
	quit()
else:
	link_key=link1s['shortenedUrl']
key_pastebin = (requests.get("https://pastebin.com/raw/xSWKZxu0").text)
def login():
    while True:
        banner()
        print(sr+'Link Để Vượt Key Là: '+link_key)
        check_key=input(sr+"Nhập Key: ")
        if check_key == key or check_key == key_pastebin:
            break
        print(sr+"Vui lòng liên hệ Admin để lấy key")
        sleep(1)
def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''\n
    ╔═════════════════════════════════╗
    ║ ➽ Facebook : Nguyễn Văn Khang   ║ 
    ║ ➽ Zalo : 0988655794             ║
    ║ ➽ Youtube : Shisui0711          ║
    ║ ➽ Bản Quyền : Shisui0711        ║
    ╚═════════════════════════════════╝                                                                                             
                               \n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(banner)))
def dk():
   a= "\033[1;91m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+" "
login()
banner()
dk()
print(sr+"Nhập [1] Tool Tặng Quà")
print(sr+"Nhập [2] Tool Buff Share Ảo Facebook")
print(sr+"Nhập [3] Tool Reg Page Profile")
print(sr+"Nhập [4] Tool Mã Hóa Python")
print()
dk()
choose = int(input(sr+"Nhập Số : "))
try:
    if choose == 1:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/toolspam_fullsource.py").text)
    if choose == 2:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/bufshare_facebook.py").text)
    if choose == 3:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/regpro5.py").text)
    if choose == 4:
        exec(requests.get('https://raw.githubusercontent.com/shisui0711/TOOL/main/encode.py').text)
except ValueError:
    print(sr+"Vui lòng chọn số nguyên")


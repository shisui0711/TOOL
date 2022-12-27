import os
try:
	import requests,bs4,pystyle,pathlib,colorama,inquirer,prettytable
except ImportError or ModuleNotFoundError:
	os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pathlib && pip install colorama && pip install inquirer && pip install prettytable')
import json
from time import sleep
import sys
import requests
from pystyle import *
def checkey(key):
    data = {
        "key": key
    }
    response = requests.post("https://khangpro.site/api/checkey.php",data=data).json()
    if(response['status'] == 'correct'):
        return True
    else: 
        return False
def login():
    while True:
        banner()
        print(sr+'Lấy Key Tại: khangpro.site/getkey.php')
        key=input(sr+"Nhập Key: ")
        if checkey(key):
            break
        print(sr+"Key Không Đúng Hoặc Đã Hết Hạn")
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
print(sr+"Nhập [4] Tool Mã Hóa Python Hyperion")
print(sr+"Nhập [5] Tool Get Token từ UID|PASS|2FA")
print(sr+"Nhập [6] Tool Buff View Story Facebook")
print(sr+"Nhập [7] Tool Buff Cảm Xúc Story Facebook")
print()
dk()
try:
    choose = int(input(sr+"Nhập Số : "))
    if choose == 1:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/toolspam_fullsource.py").text)
    if choose == 2:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/bufshare_facebook.py").text)
    if choose == 3:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/regpro5.py").text)
    if choose == 4:
        exec(requests.get('https://raw.githubusercontent.com/shisui0711/TOOL/main/encode.py').text)
    if choose == 5:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/gettoken.py").text)
    if choose == 6:
        exec(requests.get("https://raw.githubusercontent.com/shisui0711/TOOL/main/view_story.py").text)
    if choose == 7:
        exec(requests.get("https://github.com/shisui0711/TOOL/blob/main/react_story.py").text)
    
except ValueError:
    print(sr+"Vui lòng chọn số nguyên")


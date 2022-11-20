import os
import random
import threading
import requests
from pystyle import *
import time
import sys
import datetime
import datetime
from time import sleep
import threading,sys
from urllib.parse import *
import requests,os
from time import sleep
import time
from pathlib import Path
__dir__: Path = Path(__file__).parent
class MainSHare:
    os.system('clear') 
    def __init__(self):
        self.red=Col.red
        self.green=Col.green
        self.yellow=Col.yellow
        try:
            self.open_file = open(__dir__/'token.txt',"r").read().split('\n')
            try:
                self.open_file.remove('')
            except:
                pass
            self.total = str(len(self.open_file))
        except:
            quit(self.format_print_error("</>", 'Dữ liệu file "token.txt" không hợp lệ'))
    def format_print(self, symbol, text):
        return f"""{Col.Symbol(symbol, self.green, self.green)} {self.green}{text}{Col.reset}"""
    def format_print_error(self, symbol, text):
        return f"""{Col.Symbol(symbol, self.red, self.red)} {self.red}{text}{Col.reset}"""
    def format_input(self, symbol, text):
        return f"""{Col.Symbol(symbol, self.yellow, self.yellow)} {self.yellow}{text}{Col.reset}"""
    def banner(self):
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
        if self.total == '0':
            print(self.format_print_error("</>", "Số Token Không Đủ. Vui lòng mở file và nhập thêm mỗi token một dòng"))
            sleep(3)
            sys.exit()
    def share(self, id_post, token):
            rq = random.choice([requests.get, requests.post])
            dt_now = datetime.datetime.now()
            response = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
            if 'id' in response:
                print(self.format_print("</>",f"{dt_now.strftime('%H:%M:%S')}: {response['id']}"))
            else:
                print(self.format_print_error("</>",f"{dt_now.strftime('%H:%M:%S')}: TOKEN DIE"))
    def run_share(self):
            try:
                self.open_file = open(__dir__/'token.txt',"r").read().split('\n')
                try:
                    self.open_file.remove('')
                except:
                    pass
                self.total = str(len(self.open_file))
            except:
                quit(self.format_print_error("</>", 'Dữ liệu file "token.txt" không hợp lệ'))
            while True:
                main.banner()
                try:
                    print(self.format_print("</>","Số Token:"+self.total)) 
                    id_post = input(self.format_input("</>",f"Nhập ID Bài Viết: "))
                    threa = int(input(self.format_input("</>",f"Số luồng: ")))
                    if id_post != '' and threa > 0:
                        break
                    else:
                        print(self.format_print("</>", "Số luồng > 0"))
                        time.sleep(3)
                except:
                    print(self.format_print("</>", "Lỗi dữ liệu đầu vào"))
                    time.sleep(1)
            while True:
                for token in self.open_file:
                    t = threading.Thread(target=self.share, args=(id_post, token))
                    t.start()
                    while threading.active_count() > threa:
                        t.join()
if __name__ == "__main__":
    try:
        with open(__dir__/'token.txt',"a"):
            pass
        main = MainSHare()
        print(main.format_print("</>","Số Token:"+main.total))
        print(main.format_print("1","Chạy Số Token Có Sẵn"))
        print(main.format_print("2","Nhập Thêm Token"))
        print(main.format_print("3","Xóa Toàn Bộ Token Và Nhập Lại"))
        try:
            while True:
                abc = int(input(main.format_input("</>","Chọn Số:")))
                if abc == 1 or abc == 2 or abc == 3:
                    break
                print(main.format_print_error("</>","Vui lòng chọn đúng chức năng"))
        except:
            print(main.format_print("</>", "Lỗi dữ liệu đầu vào"))
        if abc == 1:
            pass
        if abc == 2:
            dem=1
            while True:
                tk = input(main.format_input("</>","Nhập Token Thứ "+str(dem)+":"))
                if tk =="":
                    break
                dem+=1
                with open(__dir__/"token.txt","a") as f:
                    f.write(tk+"\n")
        if abc == 3:
            with open(__dir__/"token.txt","w"):
                pass
            dem=1
            while True:
                token = input(main.format_input("</>","Nhập Token Thứ "+str(dem)+":"))
                if token =="":
                    break
                dem+=1
                with open(__dir__/"token.txt","a") as f:
                    f.write(token+"\n")
        
        main.run_share()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+main.format_print('</>', ':)'))

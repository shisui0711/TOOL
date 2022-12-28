import os,sys,requests,threading
from time import sleep
from datetime import datetime
from pystyle import*
class ReactStory:
    def __init__(self):
        self.blue = Col.blue
        self.yellow=Col.yellow
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.blue, Col.blue))
        self.red = Colors.StaticMIX((Col.red, Col.red, Col.red))
        self.green= Colors.StaticMIX((Col.green, Col.white, Col.white))
        self.sr = "\033[1;91m『\033[1;97m亗\033[1;91m』"+"\033[1;97m▶▶\033[1;92m"+" "
        self.dem=0
        self.listcx = []
        self.list_page_pro5 = []
    def format_print_success(self, text):
        return f"""{self.lblue}{text}{Col.reset}"""
    def format_print_error(self, text):
        return f"""{self.red}{text}{Col.reset}"""
    def format_input(self, text):
        return f"""{self.green}{text}{Col.reset}"""
    def banner(self):
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
    def checklive(self):
        headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': self.cookie,
        }
        try:
            print(self.sr+"Đang Check Live Cookie")
            find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
            self.fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
        except:
            exit(self.sr+"Cookie Die Vui Lòng Kiểm Tra Lại")
    def get_id_pro5(self):
        headers_getid = {
            'cookie': self.cookie, 
        }
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
            'doc_id': '5300338636681652'
        }
        getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
        for i in getidpro5:
            uid_page = i['profile']['id']
            name_page = i['profile']['name']
            gomlist = f'{uid_page}|{name_page}'
            self.list_page_pro5.append(gomlist)
    def run(self):
        self.banner()
        self.cookie = input(self.format_input('Nhập Cookie Chứa Page Pro5:'))
        self.checklive()
        self.get_id_pro5()
        print(self.sr+'Đã Tìm Thấy '+str(len(self.list_page_pro5))+' Page Pro5')
        linkstr = input(self.format_input('Nhập Link Story:'))
        data = linkstr.split('/')[5].split('/?')[0]
        print(self.sr+'Nhập Số 1 Để Tăng Cảm Xúc Like')
        print(self.sr+'Nhập Số 2 Để Tăng Cảm Xúc Love')
        print(self.sr+'Nhập Số 3 Để Tăng Cảm Xúc Care')
        print(self.sr+'Nhập Số 4 Để Tăng Cảm Xúc Haha')
        print(self.sr+'Nhập Số 5 Để Tăng Cảm Xúc Wow')
        print(self.sr+'Nhập Số 6 Để Tăng Cảm Xúc Sad')
        print(self.sr+'Nhập Số 7 Để Tăng Cảm Xúc Angry')
        try:
            cx = int(input(self.format_input('Nhập cảm xúc muốn thả:')))
        except ValueError:
            exit(self.sr+'Lỗi dữ liệu')
        if cx==1:
            self.listcx.append('👍')
        elif cx==2:
            self.listcx.append('❤️')
        elif cx==3:
            self.listcx.append('🤗')
        elif cx==4:
            self.listcx.append('😆')
        elif cx==5:
            self.listcx.append('😮')
        elif cx==6:
            self.listcx.append('😢')
        elif cx==7:
            self.listcx.append('😡')
        else:
            exit(self.sr+'Không tồn tại số đã chọn')
        soluongcx = int(input(self.format_input('Nhập Số Lượng Cảm Xúc Cần Tăng:')))
        while True:
            for x in range(int(len(self.list_page_pro5))):
                self.dem=self.dem+1
                threading.Thread(target=self.tangcxstr,args=(x, self.dem, linkstr, data, )).start()
                if self.dem == soluongcx:
                    sleep(3)
                    exit(self.format_print_success('Đã Hoàn Thành '+str(soluongcx)+' Cảm Xúc '))
    def tangcxstr(self,x, dem, linkstr, dataurlstr):
        camxuc = self.listcx[0]
        time = datetime.now().strftime("%H:%M:%S")
        uid_page = self.list_page_pro5[x].split('|')[0]
        name_page = self.list_page_pro5[x].split('|')[1]
        list1 = (f'i_user={uid_page};')
        cookie9 = (f'{self.cookie}{list1}')
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': linkstr,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1221',
            'x-fb-friendly-name': 'useStoriesSendReplyMutation',
            'x-fb-lsd': '4CR-snjduLBRfA-cdgjhg_',
            'cookie': cookie9,
        }

        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': '4CR-snjduLBRfA-cdgjhg_',
            '__aaid': '497084035286445',
            '__spin_r': '1006641324',
            '__spin_b': 'trunk',
            '__spin_t': '1669734368',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useStoriesSendReplyMutation',
            'variables': '{"input":{"attribution_id_v2":"StoriesCometSuspenseRoot.react,comet.stories.viewer,via_cold_start,1669734368520,55579,,","lightweight_reaction_actions":{"offsets":[0],"reaction":"'+str(camxuc)+'"},"message":"'+str(camxuc)+'","story_id":"'+str(dataurlstr)+'","story_reply_type":"LIGHT_WEIGHT","actor_id":"100088148974138","client_mutation_id":"2"}}',
            'server_timestamps': 'true',
            'doc_id': '4826141330837571',
        }

        runtanglikestr = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
        if 'data' in runtanglikestr:
            print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[0;93mSUCCESS \033[1;31m| \033[1;34m'+str(uid_page)+' \033[1;31m| \033[1;35m'+str(name_page)+' \033[1;31m| \033[1;37m'+str(camxuc)+' \033[1;31m| \033[1;37m'+str(dataurlstr)+' ')
        else:
            print('\033[1;31mTăng Cảm Xúc Thất Bại, Có Vẻ ACC Bạn Đã Bị Block!!')
if __name__ == "__main__":   
    try:
        ReactStory().run()
    except KeyboardInterrupt:
        exit()
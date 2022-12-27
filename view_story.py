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
        self.cout=0
        self.list_id_name_page = []
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
            self.list_id_name_page.append(gomlist)
    def run(self):
        self.banner()
        self.cookie = input(self.format_input('Nhập Cookie Chứa Page Pro5:'))
        self.checklive()
        self.get_id_pro5()
        print(self.sr+'Đã Tìm Thấy '+str(len(self.list_id_name_page))+' Page Pro5')
        linkstr = input(self.format_input('Nhập Link Story:'))
        data = linkstr.split('/')[5].split('/?')[0]
        soluongview = int(input(self.format_input('Nhập Số Lượng View Cần Tăng:')))
        for x in range(soluongview):
            dem=dem+1
            threading.Thread(target=self.buffview,args=(x, data, linkstr, self.cookie, )).start()
    def buffview(self,x, thanhphan9, url_str, cookie):
        time = datetime.now().strftime("%H:%M:%S")
        uid_page = self.list_id_name_page[x].split('|')[0]
        name_page = self.list_id_name_page[x].split('|')[1]
        list1 = (f'i_user={uid_page};')
        cookie9 = (f'{cookie}{list1}')
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'origin': 'https://www.facebook.com',
            'referer': url_str,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1186',
            'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
            'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
            'cookie': cookie9,
        }

        data = {
            'av': uid_page,
            '__user': uid_page,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
            'variables': '{"input":{"bucket_id":"259253279258515","story_id":"'+str(thanhphan9)+'","actor_id":"'+uid_page+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5127393270671537',
        }

        runview = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        print('\033[1;31m[\033[0;93m'+str(x+1)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[0;93mSUCCESS \033[1;31m| \033[1;35m'+str(uid_page)+' \033[1;31m| \033[1;34m'+str(name_page)+' \033[1;31m| \033[1;37m'+str(thanhphan9)+'')
if __name__ == "__main__":   
    try:
        ReactStory().run()
    except KeyboardInterrupt:
        exit()
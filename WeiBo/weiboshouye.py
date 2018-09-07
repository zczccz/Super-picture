import hashlib

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re
import threading
import requests
import urllib
import urllib.error
import random

# browser = webdriver.Chrome()

browser = webdriver.Firefox()
browser.get('https://m.weibo.cn/')
def login():
    log_bt = browser.find_element_by_class_name('lite-log-in')
    log_bt.click()
    time.sleep(4)
    login_name = browser.find_element_by_id('loginName')
    login_name.send_keys('')
    login_pass = browser.find_element_by_id('loginPassword')
    login_pass.send_keys('')
    time.sleep(1.5)
    login_bt = browser.find_element_by_id('loginAction')
    login_bt.click()
    browser.maximize_window()  # 将浏览器最大化显示
    time.sleep(5)


def category(iii):
    time.sleep(3)
    spark1 = browser.find_element_by_css_selector('.nt-search > input:nth-child(2)')
    spark1.clear()
    spark1.send_keys(iii)
    spark1.send_keys(Keys.ENTER)
    time.sleep(3)


def scrollto():
    time.sleep(0.8)
    # 下拉滑动框
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(random.randrange(2,5))
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(random.randrange(2,5))
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(random.randrange(2,5))

def page_source():
    pa = browser.page_source
    # print(pa)
    src = re.compile('<img src="(https://wx[1-4].sinaimg.cn/orj360/.*?jpg)">').findall(pa)

    for s in src:
        s = str(s).replace('orj360', 'mw1024')
        hashy = str(s).split('/')[4][0:16]
        # print(hashy)
        hashi = hashlib.md5()
        hashi.update(bytes(hashy, encoding='utf-8'))
        # print(hashi.hexdigest())  # 加密
        # print(s)
        try:
            r = requests.get(s,timeout=30)
            # urllib.request.urlretrieve(src,'./img/0'+str(24)+'.jpg')
            payload = {'site_id': 3,
                       'page_url': 'https://m.weibo.cn/',
                       'image_url': s,
                       'uid': hashi.hexdigest()}  # hashi.hexdigest()
            files = {'image': ('image.jpg', r.content)}
            p = requests.post("", files=files, data=payload)
            print(p.text)
            print(payload.values())

        except urllib.error.HTTPError as urllib_err:
            print(urllib_err)
            continue
        except Exception as err:
            time.sleep(0.3)
            print(err)
            print("产生未知错误，放弃保存")
            continue


# 登录
login()
# 点击搜索框
spark = browser.find_element_by_css_selector('div.m-text-cut')
spark.click()
time.sleep(2)

file_obj = open("./f.txt",encoding='utf-8')
l1 = file_obj.readlines()
for jj in l1:
    category(jj)
    print(jj)
    for i1 in range(100):

        # page_source()
        time.sleep(1)
        scrollto()
        i1 += 1
        # if i1 % 2 == 0:
    page_source()
    browser.refresh()

# for i in range(10000):
#
#     scrollto()
#     i += 1
#     print(i)
#     if i >= 1000:
#         page_source()
#         time.sleep(2)
print('O V E R')

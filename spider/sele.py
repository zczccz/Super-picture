from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import re
import hashlib
import requests
import urllib
import urllib.error
import random
browser = webdriver.Firefox()
browser.get('https://weibo.com/?topnav=1&mod=logo')
# cooki = browser.get_cookies()
# print(cooki)

# 下拉滑动框
time.sleep(0.5)
browser.maximize_window()  # 将浏览器最大化显示
time.sleep(5)

name = browser.find_element_by_name('username')
name.clear()
name.send_keys('')
pw = browser.find_element_by_name('password')
pw.clear()
pw.send_keys('')
time.sleep(10)
logbtn = browser.find_element_by_class_name('login_btn')
logbtn.click()
time.sleep(6)


def one(starname):
    sear = browser.find_element_by_xpath('//input[@class="W_input"]')
    sear.click()
    sear.clear()
    sear.send_keys(starname)
    searbt = browser.find_element_by_xpath('//a[@title="搜索"]')
    searbt.click()
    time.sleep(10)
    flag = 1
    while flag:
        try:
            star = browser.find_element_by_xpath('//a[@class="name_txt"]')
            star.click()
            time.sleep(3)
            browser.switch_to_window(browser.window_handles[1])
            time.sleep(6)
        except Exception as err:
            time.sleep(1)
            # flag = 0
            print(err)
            break
        flag = 0
    flag2 = 1
    while flag2:
        try:
            # print(browser.current_url)
            print(browser.window_handles)
            gra = browser.find_element_by_css_selector(".tb_tab > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
            gra.click()
            time.sleep(3)
            miankong = browser.find_element_by_css_selector('li.tab_li:nth-child(3) > a:nth-child(1) > span:nth-child(1)')
            miankong.click()
        except Exception as e:
            flag2 = 0
            print(e)
            continue

        try:
            time.sleep(3)
            print(browser.current_url)
            page = browser.current_url
            # browser.refresh()
            # browser.close()
            # page_id = page.split('/')[4]
            # hashi = hashlib.md5()
            # hashi.update(bytes(page_id, encoding='utf-8'))
            # # print(hash.hexdigest())  # 加密
            for i in range(10):
                time.sleep(0.5)
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(1)
                i += 1
            pa = browser.page_source
            print(pa)
            src = re.compile('<img class="photo_pict" src="(//+.*?)">').findall(pa)
            pic_object = re.compile('pic_objects=1042018:(.*?)&').findall(pa)

            with open('./img/ABIG_image_url.csv','a+') as f:
                f.write(page+'--'+str(int(len(src)/22))+'\n')
                f.close()

            # for s in src:
            #     s1 = str(s).replace('thumb300', 'mw1024')
            #     sr = 'https:' + s1
            #
            #     # print(sr)
            #     try:
            #         r = requests.get(sr)
            #         # urllib.request.urlretrieve(src,'./img/0'+str(24)+'.jpg')
            #         payload = {'site_id': 3,
            #                    'page_url': page,
            #                    'image_url': sr,
            #                    'uid': hashi.hexdigest()}
            #         files = {'image': ('image.jpg', r.content)}
            #         p = requests.post(" ", files=files, data=payload)
            #         print(p.text)
            #         print(payload.values())
            #         # with open('./img/'+starname+'image_url.csv','a+') as f:
            #         #     f.write(sr+'\n')
            #         #     f.close()
            #
            #     except urllib.error.HTTPError as urllib_err:
            #         print(urllib_err)
            #         continue
            #     except Exception as err:
            #
            #         print(err)
            #         print("产生未知错误，放弃保存")
            #         continue

            browser.close()
            browser.switch_to_window(browser.window_handles[0])
            # browser.refresh()
            # time.sleep(8)

        except Exception as err:
            time.sleep(1)
            browser.close()
            print(err)
            break
        flag2 = 0


file_obj = open("./e.txt", encoding='utf-8')

l1 = file_obj.readlines()
for i1 in l1[1148:1149]:
    one(i1.strip('\n'))
    time.sleep(random.randrange(10, 17))

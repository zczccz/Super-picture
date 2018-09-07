#6.1 简单Python爬虫的实现

import re
import urllib.request
import urllib3
from lxml import etree
from io import BytesIO
import requests
import json
import jsonpath
from bs4 import BeautifulSoup

url = "http://zhibo.renren.com/liveroom/hot/listClient?offset=12&limit=24&requestToken=1262086851&_rtk=16fae91d"
# url = 'https://user.qzone.qq.com/proxy/domain/vip.qzone.qq.com/fcg-bin/v2/fcg_get_mall_ex?uin=743314618&vip=0&nf=0&mode=1&tips=1&svip=0&sds=0.5089640138459102&g_tk=2147244515&qzonetoken=981e512aae6123fb5864c5366d7356305c63d3b077e403e001368f59c7c48ca3ae3226f7f29eb1&g_tk=2147244515'
html = urllib.request.urlopen(url)
# html1=urllib.request.urlopen(url).read()
# html1=urllib3.PoolManager()
content = requests.request(
                    url=url,
                    method='GET',
                    params={
                        # 'offset':'12',
                        #     'limit':'24',
                            'requestToken':'1262086851',
                            '_rtk':'16fae91d'},
                    headers={
                        # ':authority': 'user.qzone.qq.com',
                        # ':method': 'GET',
                        # ':path':' /proxy/domain/g.qzone.qq.com/fcg-bin/cgi_emotion_list.fcg?uin=2724462510&loginUin=743314618&rd=0.38498249683459584&num=3&noflower=1&g_tk=2147244515&qzonetoken=14a5df7bc3cf146a668b620c68cdf24d33e38860fb74a626fcabb420af8670180379b7aaa4fd9e&g_tk=2147244515',
                        # ':scheme': 'https',
                        # 'accept': '*/*',
                        # 'accept-encoding': 'gzip, deflate, br',
                        # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                        # 'if-modified-since': 'Thu, 12 Jul 2018 06:55:42 GMT',
                        # 'cache-control': 'max-age=0',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Connection': 'keep-alive',
                        'Date': 'Thu, 19 Jul 2018 01:46:26 GMT',
                        'Cookie': 'anonymid=jjru6ktij4mjyc; depovince=SD; _r01_=1; ick_login=0ada2779-218b-4bfb-aa72-dad2ca8a980f; t=347284c6c596afe9f8919eca1d5352fa3; societyguester=347284c6c596afe9f8919eca1d5352fa3; id=966991663; xnsid=4ffdb22b; JSESSIONID=abcFFB7bPij1_e9lLaWsw; jebe_key=9a8d8b04-18de-4acc-b3f9-a13a6937c2e4%7C3705d2fcf7540774bc3a0c42690ce552%7C1531961301671%7C1%7C1531961305291; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1531963090; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1531963090; _ga=GA1.2.514988511.1531963090; _gid=GA1.2.1695812455.1531963090; wp_fold=0; jebecookies=7fcda17a-230a-45a9-90f3-fcaeee81bde7|||||; BAIDU_SSP_lcr=https://www.baidu.com/link?url=dABGkocDGAxabwsztHGOBSKdskAoZzx-GPQYdPO2zOELnFXAXPsnAPtVzvzBCKKU&wd=&eqid=81052f180000272d000000045b4feb37',
                        'referer': 'http://zhibo.renren.com/top',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
                            })
content.encoding = 'utf-8'
soup = content.text
selector = etree.HTML(soup)
# soup = urllib.request.urlopen(url).read().decode('utf-8')
# soup = BeautifulSoup(html.read(), 'lxml').decode('utf-8')
print(soup)
content2 = json.loads(soup)
print(content2)
for i in range(len(content2['data'])):
    u = content2['data'][i]['coverImgUrl']
    print(u)
    r = requests.get(u,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'})
    # # urllib.request.urlretrieve(u, './img/'+str(i)+'.jpeg')
    with open('./img/'+str(i)+'.jpeg', 'wb') as f:
        f.write(r.content)
    # payload = {'site_id': 1,
    #            'page_url': 'http://zhibo.renren.com/top',
    #            'image_url': u}
    # files = {'image': ('image.jpg', r.content)}

    # p = requests.post("http://192.168.1.103:33333/recv", files=files, data=payload)
    # print(p.text)
# content2 = json.loads(content1)
# print(content2)
# soup = BeautifulSoup(content1,'html.parser')
# soup = jsonpath.jsonpath(content2,'img')

# pat1 = soup.find_all('//*[@id="j-feeds-list"]/ul/li['+str(i)+']/div/div[2]/div[1]/ul/li['+str(j)+']/div/div/a/img/@src')


    # req = urllib.request.urlopen(content).read()
    # html2=etree.HTML(req)
src = selector.xpath('//img[@class="poster"]/@src')
print(src, end='\n')
# imagelist=re.compile(pat1).findall(soup)
# result1=soup[0]
# pat2='<src="(.*?)">'
# imagelist=re.compile(pat2).findall(result1)
# x=1
# for imageurl in pat1.find('img'):
#     imagename="img/"+str(x)+".jpg"
#     imageurl=imageurl
#     print(imageurl)
#     try:
#         urllib.request.urlretrieve(imageurl,filename=imagename)
#     except urllib.error.URLError as e:
#         if hasattr(e,"code"):
#             x+=1
#         if hasattr(e,"reason"):
#             x+=1
#     x += 1

# page = 1

import urllib.error
import requests,os,re,time
from lxml import etree
from urllib import parse
import json
import random


# 下载图片
def download_bl_picture(pn):

        # 浏览器头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            'Cookie': 'finger=edc6ecda; buvid3=62555CF8-6623-4DED-9002-F76F24B0D62E42812infoc; LIVE_BUVID=AUTO4515337088375177',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
        }
        proxy_list0 = [
            {'http': '219.141.153.38:80'},
            {'http': '121.43.170.207:3128'},
            {'http': '111.155.116.208:8123'},
            {'http': '118.190.95.35:9001'},
            {'http': '139.129.166.68:3128'},
            {'http': '61.135.217.7:80'},
            {'http': '110.73.11.214:8123'},
            {'http': '183.30.204.163:9000'}
        ]
        # proxy_list = [
        #     {'https': '101.132.122.230:3128'},
        #     {'https': '114.215.95.188:3128'},
        #     {'https': '113.122.12.129:53128'},
        #     {'https': '61.50.244.179:808'},
        #     {'https': '106.75.71.122:80'},
        #     {'https': '115.198.35.80:6666'},
        #     {'https': '110.86.139.126:33067'},
        #     {'https': '183.129.207.74:14823'},
        #     {'https': '115.204.24.5:6666'}
        # ]
        proxy = random.choice(proxy_list0)
        # proxy = proxy_list0[7]  # 测试代理
#  明星 https://api.bilibili.com/x/web-interface/newlist?rid=137&type=0&pn=20
        htt = 'https://api.bilibili.com/x/web-interface/newlist?rid=157&type=0&pn='+str(pn)
        # 输出爬取网址
        print(htt)
        flag = 1
        while flag:
            try:
                tex = requests.request(method='GET', url=htt, headers=headers, proxies=proxy)
                tex.encoding = 'utf-8'
                text1 = tex.text
                content2 = json.loads(text1)
                print(content2)
                # print(tex.content)
                print(proxy)
                # selector = etree.HTML(text1)
                #
                for i in range(len(content2['data']['archives'])):
                    picture = content2['data']['archives'][i]['pic']
                    pageurl = htt
                    # print(picture)

            # print(pictureList)
            # for eachpicture in pictureList:#每个图片地址 picturelist 有48项

                    try:
                        r = requests.get(picture, timeout=60)
                        # urllib.request.urlretrieve(picture,'./p/'+str(picture[-8:-5])+'.jpg')
                        payload = {'site_id': 13,
                                   'page_url': pageurl,
                                   'image_url': picture}
                        files = {'image': ('image.jpg', r.content)}
                        # pp = requests.post("http://", files=files, data=payload)
                        # print(pp.text)
                        # with open('./SouGou/' + word + 'image_url.csv', 'a+') as f:
                        #     f.write(picture + '\n')
                        #     f.close()
                        print(payload.values())
                    except urllib.error.HTTPError as urllib_err:
                        print(urllib_err)
                        continue
                    except Exception as err:
                        time.sleep(0.3)
                        print(err)
                        print("产生未知错误，放弃保存")
                        continue
            except Exception as e:
                print(e)
                continue
            flag = 0


if __name__ == '__main__':
    for p in range(3, 13289):
        download_bl_picture(p)
        time.sleep(random.randrange(15, 20))

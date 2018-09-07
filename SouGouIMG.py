import urllib.error
import requests,os,re,time
from lxml import etree
from urllib import parse
import json
import random
import urllib.request

# 创建文件夹 用来存放图片
def makedir(dirname):
    if os.path.lexists(dirname):
        os.chdir(dirname)
    else:
        os.makedirs(dirname)
        os.chdir(dirname)


# 下载搜狗图片
def downloadSogouPicture(word,page2):
        # makedir('./SouGou/'+str(word))

        # 浏览器头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            'Cookie': 'IPLOC=CN3702; SUV=00E3C89F3A38A8465B63AE4249EE1757; SUID=46A8383A5F20940A000000005B63AE44; usid=46A8383AE609990A000000005B63AE5F; sct=7; SNUID=FE1F8082B7B2C5048C0ABB8DB84FB1EB; ld=Rlllllllll2bBdEElllllVHXTs7llllln0AoSkllll9lllllxklll5@@@@@@@@@@; SUIR=9F71E0E2D8DCABA41A733130D992C725; tip_show=20180806; tip_show_detail=20180806; ABTEST=0|1533601438|v1; JSESSIONID=aaaWl8H5HfPuLbgVnXruw',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'pic.sogou.com',
            'Upgrade-Insecure-Requests': '1'
        }
        proxy_list = [
            {'https': '101.132.122.230:3128'},
            {'https': '114.215.95.188:3128'},
            {'https': '113.122.12.129:53128'},
            {'http': '219.141.153.38:80'},
            {'https': '61.50.244.179:808'},
            {'https': '106.75.71.122:80'},
            {'https': '115.198.35.80:6666'},
            {'https': '110.86.139.126:33067'},
            {'https': '183.129.207.74:14823'},
            {'https': '115.204.24.5:6666'}
        ]
        proxy = random.choice(proxy_list)
        # proxy = proxy_list[3]  # 测试代理
        # 查询网址
        # http = 'http://pic.sogou.com/pics?query='
        # http = http + str(word)
        # http://pic.sogou.com/pics?query=%BA%FA%CF%C4&did=1&mode=1&start=0&reqType=ajax&tn=0&reqFrom=detail
        htt = 'http://pic.sogou.com/pics?query='+str(parse.quote(word))+'&mode=1&start='+str(page2)+'&reqType=ajax&tn=0&reqFrom=detail'
        # 输出爬取网址
        print(htt)
        flag = 1
        while flag:
            try:
                tex = requests.request(method='GET', url=htt, headers=headers,proxies=proxy)
                tex.encoding = 'utf-8'
                text1 = tex.text
                content2 = json.loads(text1)
                print(content2)
                print(tex.content)
                print(proxy)
                # selector = etree.HTML(text1)
                #
                for i in range(len(content2['items'])):
                    picture = content2['items'][i]['pic_url_noredirect']
                    pageurl = content2['items'][i]['page_url']
                    # print(picture)

            # print(pictureList)
            # for eachpicture in pictureList:#每个图片地址 picturelist 有48项

                    try:
                        # r = requests.get(picture,timeout=60)
                        urllib.request.urlretrieve(picture,'./tailand/'+str(word)+str(i)+'.jpg')
                        # payload = {'site_id': 9,
                        #            'page_url': pageurl,
                        #            'image_url': picture}
                        # files = {'image': ('image.jpg', r.content)}
                        # p = requests.post("http://192.168.1.103:33333/recv", files=files, data=payload)
                        # print(p.text)
                        # with open('./SouGou/' + word + 'image_url.csv', 'a+') as f:
                        #     f.write(picture + '\n')
                        #     f.close()
                        print('当前是第' + str(int(page2 / 48 + 1)) + '页，第' + str(i + 1) + '张')
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
    file_obj = open("./e.txt", encoding='utf-8')
    l1 = file_obj.readlines()
    for i1 in l1[250:]:
        for j in range(0, 480, 48):
            downloadSogouPicture(i1.strip('\n'), j)
        time.sleep(random.randrange(18, 28))

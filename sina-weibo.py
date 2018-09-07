import urllib.request
from lxml import etree
import requests
import json
import re
import random
import urllib.error
import time
import hashlib

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



class Cr:
    def __init__(self,pageurl, pn):  #, type0
        self.pageurl = pageurl
        self.pn = pn
        # self.typee = type0
        # self.url = url

    def get_urls(self):
        # page = re.compile('&page=(.*?)&').findall(self.url)

        # since_id = re.compile('&since_id=(.*?)&').findall(self.url)
        # owner_uid = re.compile('&owner_uid=(.*?)&').findall(self.url)
        # page_id = re.compile('&page_id=(.*?)&').findall(self.url)
        url = 'https://weibo.com/p/aj/album/loading?ajwvr=6&owner_uid=' + str(self.pageurl.split('/')[4][
                            6:16])+ '&page_id='+str(self.pageurl.split('/')[4])+'&page='+str(self.pn)+'&ajax_call=1'
        print(url)
        proxy = random.choice(proxy_list0)
        content = requests.get(
            url=url,
            proxies=proxy,

            # params={'ajwvr': '6',
            #         'type': 'photo',
            #         'owner_uid': owner_uid,
            #         'viewer_uid': '5578933944',
            #         'since_id': since_id,
            #         'page_id': page_id,
            #         'page': page,
            #         'ajax_call': '1'},
            headers={
                'Connection': 'keep-alive',

                'Cookie': 'SINAGLOBAL=3582516957333.5103.1533610613412; un=17865202426; YF-Page-G0=140ad66ad7317901fc818d7fd7743564; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; wvr=6; YF-V5-G0=bb389e7e25cccb1fadd4b1334ab013c1; _s_tentry=-; Apache=9576707072782.984.1536053050644; ULV=1536053050661:11:1:1:9576707072782.984.1536053050644:1535520987178; UOR=,,www.baidu.com; UM_distinctid=165ac7fd49c11-02a63bbc89de6b-323b5b03-100200-165ac7fd49d92; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5AZl2c6WPkq2J0y4sF8LvF5JpX5KMhUgL.Fo-fS0n4e0e4ShB2dJLoIf2LxKML1hnLBo2LxK-LB-BL1K.LxK-LB--L1-BLxK-LB--L1-BLxKML1-2L1hBLxKnL1heLBK2LxKnL12eLB-eLxK-LBKBLBKMLxK-L12qL1KBt; SCF=AiU6fRvAS1WknEqEnDUMJKboguBQnqnREJwLCn8XLE1Tzrf3vqYXrnZntQR-7hm-psrKH_LodwUTzG6-0FM3r6A.; SUB=_2A252lanUDeRhGeNL7FoY8y3FzziIHXVV4pwcrDV8PUNbmtBeLRPRkW9NSPZuURWciGZNnvdJZiR8pbO-WRIIotfu; SUHB=05i6yN0nM7yWzf',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                              '/66.0.3359.139 Safari/537.36'
            })
        content.encoding = 'utf-8'
        soup = content.text

        rsp_data = json.loads(soup)

        # print(rsp_data['data'])
        selector = etree.HTML(rsp_data['data'])
        pic_object = re.compile('&pic_objects=[0-9]+:(.*?)&tab=2').findall(str(rsp_data['data']))
        src = selector.xpath('//img[@class="photo_pict"]/@src')
        # src = re.compile('<img class="photo_pict " src="https:(//wx3.sinaimg.cn/thumb300.*?)"/>').findall(rsp_data['data'])
        print(src)
        # print(pic_object)
        print(proxy)

        return src, pic_object

    def img(self, srclist, pic_list):  # , pic_list
        d = 0

        # hashi = hashlib.md5()
        # hashi.update(bytes(self.pageurl.split('/')[4], encoding='utf-8'))
        # print(hashi.hexdigest())  # 加密
        for nb in range(1, len(srclist)):
        # for src in srclist:
            src = 'https:' + srclist[nb]

            pic_object = pic_list[nb]
            try:
                r = requests.get(src)
                # urllib.request.urlretrieve(src,'./img/0'+str(24)+'.jpg')
                payload = {'site_id': 3,
                           'page_url': self.pageurl,
                           'image_url': src,
                           'uid': pic_object}  # hashi.hexdigest()
                files = {'image': ('image.jpg', r.content)}
                p = requests.post("http://192.168.1.103:33333/recv", files=files, data=payload)
                print(p.text)
                print(payload.values())
                d += 1
            except urllib.error.HTTPError as urllib_err:
                print(urllib_err)
                continue
            except Exception as err:
                time.sleep(0.3)
                print(err)
                print("产生未知错误，放弃保存")
                continue
        print(d)


if __name__ == '__main__':
    file_obj = open("./ABIG_image_url.csv",encoding='utf-8')
    l1 = file_obj.readlines()
    for l in l1[1:3]:
        pu = l.split('--')[0]
        # 新增type
        type_start = l.find('type=')
        end = l.find('#')
        type1 = l[type_start+5:end]
        # print(type1)
        pnn = int(l.split('--')[1])+2
        for pn in range(1, pnn):
            try:
                cr = Cr(
                    pageurl=pu,
                    pn=pn,
                    # type0=type1
                        )
                cr.img(cr.get_urls()[0],cr.get_urls()[1])
                # cr.get_urls()
            except Exception as E:
                print(E)
                continue
            time.sleep(random.randrange(18, 20))




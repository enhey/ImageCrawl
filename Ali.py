import requests
import re
from urllib.parse import quote
import json
import random
from bs4 import BeautifulSoup
from ECCrawl import ECCrawl

user_agent = [
    'Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)',
    'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN',
    'Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 7.1.1)',
    'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.18.21.0 (Baidu; P1 6.0.1)']
# headers = {
#     'User-Agent': random.choice(user_agent)
# }

BASC_URL = 'http://www.taobao.com'
BRIEF_HEAD_URL = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?'  # 至少需要date和iteamnumid
DETAIL_HEAD_URL = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdesc/6.0/?'


class TB(ECCrawl):
    headers = {
        'User-Agent': random.choice(user_agent)
    }

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.session = requests.Session()
        try:
            self.session.get(BASC_URL, headers=self.headers)  # 先模拟进入淘宝首页
        except:
            print('tb没有网络')

        self.mobile_url = self.mobile_url()
        self.headers['referer'] = self.mobile_url
        self.illegle_char = r"[\/\\\:\*\?\"\<\>\|]"  # 非法文件名字符

        self.brief_content = self.brief()
        self.title, self.id = self.title_and_id()

    def mobile_url(self):  # 获取移动端链接
        url = ''
        try:
            all_html = self.session.get(self.url, headers=self.headers)
            url = all_html.url
        except:
            print('tb请规范输入链接')
            return exit()
        return url

    def brief(self):  # 获取简介HTML,包含淘宝网页头部的大量信息
        detail_content={}
        try:
            id=re.search('id=[0-9]*', self.mobile_url).group()[3:]
            main_data_dict = {}
            main_data_dict['itemNumId'] = id
            main_data_dict['itemId'] = id
            tail_url = str(main_data_dict).replace("'", '"').replace(' ', '')
            tail_url = quote(tail_url)  # 进行URL编码
            detail_url = BRIEF_HEAD_URL + 'ttid=2018@taobao_h5_9.9.9&' + 'data=' + tail_url  # 得到简介页的URL
            detail_content = self.session.get(detail_url, headers=self.headers).json()
        except:
            print('tb配置异常')
        return detail_content

    def title_and_id(self):
        title = ''
        id = ''
        try:
            title = re.sub(self.illegle_char, ' ', self.brief_content['data']['item']['title'])  # 获取页面标题
        except:
            print('无标题')

        try:
            id = re.sub(self.illegle_char, ' ', self.brief_content['data']['item']['itemId'])  # 获取页面标题
        except:
            print('无ID')

        return title, id

    def main_img(self):
        img_urls = []
        try:
            img_tags = self.brief_content['data']['item']['images']  # 主图链接
            for img_tag in img_tags:
                star = img_tag.find('//')
                url = 'http://' + img_tag[star + 2:]
                img_urls.append(url)
        except:
            print('无主图')
        return img_urls

    def color_img(self):
        img_urls = {}
        try:
            props = self.brief_content['data']['skuBase']['props']
            for prop in props:
                color_tags = prop['values']  # 颜色和分类
                for color_tag in color_tags:
                    if 'image' not in color_tag:
                        continue
                    star = color_tag['image'].find('//')
                    color_url = 'http://' + color_tag['image'][star + 2:]
                    color_name = re.sub(self.illegle_char, ' ', color_tag['name'])  # 出去非法文件名
                    img_urls[color_name] = color_url
        except:
            print('不存在颜色分类')

        return img_urls

    def video(self):
        video_urls = []
        try:  # 获取视频链接
            vd_url = json.loads(self.brief_content['data']['apiStack'][0]['value'])['item']['videos'][0]['url']
            video_urls.append(vd_url)
        except:
            print('不存在视频')

        return video_urls

    def pc_img(self):
        detail_html = {}
        img_urls = []
        try:
            id=re.search('id=[0-9]*', self.mobile_url).group()[3:]
            main_data_dict={}
            main_data_dict['id']=id
            main_data_dict['type'] = '1'   #type=0 手机端  type=1 pc端
            tail_url = str(main_data_dict).replace("'", '"').replace(' ', '')
            tail_url = quote(tail_url)  # 进行URL编码
            detail_url = DETAIL_HEAD_URL + 'data=' + tail_url  # 得到详情页的URL
            detail_html = self.session.get(detail_url, headers=self.headers).json()
        except:
            print('电脑详情图内容异常')

        try:  # 寻找电脑链接并获取电脑端图片

            img_str = detail_html['data']['pcDescContent']  # 含有图片链接的一段的文本
            pattern = '<img[^>]+>'
            tags = re.findall(pattern, img_str)
            for tag in tags:
                star = tag.find('//')
                end = tag.find('"', star)
                url = 'http://' + tag[star + 2:end]
                img_urls.append(url)
        except:
            print('无电脑详情图')
        return img_urls


    def mb_img(self):
        detail_html = {}
        img_urls = []
        try:
            # mobile_url_list = re.split("[?&#=]", self.mobile_url)
            # main_data_list = mobile_url_list[1:-1]
            # main_data_dict = dict(zip(main_data_list[0::2], main_data_list[1::2]))  # 获取链接后部的键值对
            id=re.search('id=[0-9]*', self.mobile_url).group()[3:]
            main_data_dict={}
            main_data_dict['id']=id
            main_data_dict['type'] = '0'   #type=0 手机端  type=1 pc端
            tail_url = str(main_data_dict).replace("'", '"').replace(' ', '')
            tail_url = quote(tail_url)  # 进行URL编码
            detail_url = DETAIL_HEAD_URL + 'data=' + tail_url  # 得到详情页的URL
            detail_html = self.session.get(detail_url, headers=self.headers).json()
        except:
            print('手机详情图内容异常')

        try:
            img_tags = detail_html['data']['wdescContent']['pages']
            for img_tag in img_tags:
                if img_tag[0:4] == '<img':
                    pattern = re.compile(r'<[^>]+>', re.S)  # re.S匹配包括换行在内的所有字符
                    out_tag = pattern.sub('', img_tag)
                    star = out_tag.find('//')
                    url = 'http://' + out_tag[star + 2:]
                    img_urls.append(url)
        except:
            print('无手机详情图')
        return img_urls


class Ali(ECCrawl):
    headers = {
        'User-Agent': random.choice(user_agent)
    }
    home_page = 'http://1688.com'

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.session = requests.Session()
        try:
            self.session.get(self.home_page, headers=self.headers)
            self.headers['Referer'] = self.home_page
            self.page_config()
        except:
            print('1688网络异常')

    def page_config(self):
        try:
            self.url=self.url.split('?')[0]+'?spm=a26352.13672862.offerlist.32.66c430e2uKeqti&tracelog=p4p&clickid=d7edffbeb5614e90aaa6578c31848d9a&sessionid=713e60dec747db0c456016f2e0943a9c'
            brief_content = self.session.get(self.url, headers=self.headers)
            self.mobile_url = brief_content.url
            #brief_content = self.session.get(self.mobile_url, headers=self.headers)
            self.headers['Referer'] = self.mobile_url
            self.soup = BeautifulSoup(brief_content.text, 'lxml')
            self.title = self.soup.find('title').get_text()
            self.title = re.sub(self.illegal_char, ' ', self.title)
            self.id = re.split('[./]', self.url)[6]

        except:
            print('1688获取网页配置异常')

    def main_img(self):
        img_tags=[]
        img_urls = []
        try:
            main_content = self.soup.find_all('div', attrs={'class': 'swipe-content'})[1]
            img_tags = main_content.find_all('img')
        except:
            print('1688无法获取主图内容')
        for img_tag in img_tags:
            try:
                url = img_tag.get('swipe-lazy-src')
                if not url.startswith('http'):
                    if url.startswith('//'):
                        url = 'http:' + url
                    else:
                        url = 'http://' + url
                img_urls.append(url)
            except:
                print('1688含有异常主图'+img_tag)
                continue
        return img_urls

    def pc_img(self):
        img_urls=[]
        try:
            soup1 = self.soup.find('div', attrs={'class': 'takal-wap-dpl-box module-wap-detail-common-description'})
            json_str = soup1.find('script',
                                  attrs={'type': 'component/json', 'data-module-hidden-data-area': 'Y'}).get_text()
            json_str = re.sub(r'[[](.*)[]]', '""', json_str)
            desc_json = json.loads(json_str)
            desc_url = desc_json['detailUrl']
            desc_content=self.session.get(desc_url)
            desc_soup=BeautifulSoup(desc_content.text,'lxml')
            img_tags=desc_soup.find_all('img')
        except:
            print('1688无法获取详情图内容')

        for img_tag in img_tags:
            try:
                url=img_tag.get('src')[2:-2]
                if not url.startswith('http'):
                    if url.startswith('//'):
                        url = 'http:' + url
                    else:
                        url = 'http://' + url
                img_urls.append(url)
            except:
                print('1688含有异常详情图'+img_tag)
                continue
        return img_urls

    def color_img(self):
        img_urls={}
        try:
            soup1=self.soup.find('div',attrs={'id':'widget-wap-detail-common-footer'})
            json_str=soup1.find('script').get_text()
            desc_json=json.loads(json_str)
        except:
            print('1688无法获取颜色分类内容')
        try:
            props = desc_json['skuProps'][0]['value']
            for prop in props:
                url=prop['imageUrl']
                name=prop['name']
                img_urls[name]=url
        except:
            print('1688无颜色分类')
        return img_urls

    # def video(self):
    #     headers={
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
    #     }
    #     content=requests.Session().get(url=self.url,headers=headers)
    #     soup=BeautifulSoup(content.text,'lxml')
    #     tag=soup.find('div',attrs={'class':'mod mod-detail-gallery'})
    #     print('')




# url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.808.46fb33a3ifgs0Y&id=610254299107&ns=1&abbucket=9'
# # setting={'mb': True, 'pc': True, 'vd': True, 'cl': True, 'path': 'D:/你好', 'ip': '192.168.122.255', 'port': '0808'}
# m = TB(url)
# m.pc_img()
# print()
# url = 'https://detail.1688.com/offer/607219306584.html?spm=a26352.13672862.offerlist.1.1da841daWqRzdY&tracelog=p4p&clickid=b61dfd5f57d74adc8754486e35586c84&sessionid=dca5f43dcffb45072833a1879e8659cd'
# t = Ali(url)
# t.page_config()
# t.pc_img()
# t.color_img()
# t.video()
# print(' ')

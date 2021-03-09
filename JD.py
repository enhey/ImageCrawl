import os
import requests
import re
from bs4 import BeautifulSoup
import demjson
import random
from ECCrawl import ECCrawl
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11']

BASC_URL = 'http://www.jd.com'


class JD(ECCrawl):
    headers = {
        'User-Agent': random.choice(user_agent)
    }

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.session = requests.Session()
        try:
            self.session.get(BASC_URL, headers=self.headers)  # 先模拟进入京东首页
        except:
            print('jd没有网络')
        self.page_config()

    def page_config(self):
        try:
            brief_content = self.session.get(self.url, headers=self.headers)  # 获取网页的代码
            soup = BeautifulSoup(brief_content.text, 'lxml')
            self.title = soup.find(name='title').get_text()
            self.title = re.sub(self.illegal_char, ' ', self.title)
            content1 = soup.find(name='script').get_text().strip()
            end = content1.find('try')
            js = content1[0:end].strip()[17:-1]
            self.data_json = demjson.decode(js)
            self.id = str(self.data_json['product']['skuid'])
        except:
            print('jd获取配置异常')

    def main_img(self):
        main_imgs = []
        try:
            url_head = 'http://img13.360buyimg.com/n5/'
            imgs = self.data_json['product']['imageList']
            for img in imgs:
                img = 's800x800_jfs' + img[3:]
                img_url = url_head + img
                main_imgs.append(img_url)
        except:
            print('jd主图异常')
        return main_imgs

    def pc_img(self):
        try:
            describ_imgs = []
            desc_url = self.data_json['product']['desc']
            desc_url = 'http:' + desc_url
            desc_content = self.session.get(desc_url, headers=self.headers).json()
            html = desc_content['content']
            soup = BeautifulSoup(html, 'lxml')
            style = soup.find('style')
        except:
            print('jd无法获取详情图内容')
            return

        # 图片放在背景图内
        if style != None and len(style.text) > 0:
            style_content = style.get_text()
            pattern = re.compile(r'background-image:url[(](.*?)[)]')
            urls = pattern.findall(style_content)
            describ_imgs = ['http:' + img_url for img_url in urls]
        # 图片放在div内
        else:
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                try:
                    img_url = img_tag.get('data-lazyload')
                    if not img_url.startswith('http'):
                        if img_url.startswith('//'):
                            img_url='http:'+img_url
                        else:
                            img_url='http://'+img_url
                    describ_imgs.append(img_url)
                except:
                    print('jd详情图异常'+img_tag)
                    continue

        return describ_imgs

    def video(self):
        videos = []
        url_head = 'https://c.3.cn/tencent/video_v2?'
        try:
            video_dict = self.data_json['product']['imageAndVideoJson']
            infoVideoId = video_dict['infoVideoId']
            mainVideoId = video_dict['mainVideoId']
            info_video = url_head + 'vid=' + infoVideoId
            main_video = url_head + 'vid=' + mainVideoId
            info_json = self.session.get(info_video, headers=self.headers).json()
            main_json = self.session.get(main_video, headers=self.headers).json()
            info_url = info_json.get('playUrl')
            main_url = info_json.get('playUrl')
            videos.append(info_url)
            videos.append(main_url)
        except:
            print('jd未找到视频')
        return videos

# url = 'https://item.jd.com/100004770235.html'
# url = 'https://item.jd.com/14157116051.html'
# t = JD(url=url)
# t.page_config()
# main = t.main_img()
# desc = t.pc_img()
# v = t.video()
# print(main + desc + v)

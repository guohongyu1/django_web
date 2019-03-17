import requests
import re
import csv
from fontTools.ttLib import TTFont
from io import BytesIO
from pyquery import PyQuery as pq
import random
class Spider(object):
    def __init__(self):
# 代理ip列表
#         self.proxy_list = [{"http": '219.138.58.114:3128'}, {"http": '61.135.217.7:80'}, {"http": '101.201.79.172:808'},
#         {'http': '122.114.31.177:808'}]
    # 用户代理列表
        self.user_list = [
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        # 'User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
        # 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16']
        # self.index = random.randint(0, 3)
        self.index=0
        self.base_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page='
        self.headers = {"User-Agent": self.user_list[self.index]}

    def send_request(self, page_url):
        data = requests.get(page_url, headers=self.headers).content.decode('utf-8')
        # print(data)
        return data

    def get_font(self, url):
        response = requests.get(url)
        font = TTFont(BytesIO(response.content))
        cmap = font.getBestCmap()
        font.close()
        return cmap

    def get_encode(self, cmap, values):
        WORD_MAP = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                    'seven': '7',
                    'eight': '8', 'nine': '9', 'period': '.'}
        word_count = ''
        for value in values.split(';'):
            value = value[2:]
            key = cmap[int(value)]
            word_count += WORD_MAP[key]
        return word_count

    def parse(self, data, page_url):
        """清洗数据"""
        # 编写正则表达式
        book_name = r'<h4><a href="(.*?)" target="_blank" data-eid=".*?" data-bid="\d*?">(.*?)</a></h4>'  # 链接+书名
        book_author = r'<a class="name" href=".*?" data-eid=".*?" target="_blank">(.*?)</a>'  # 作者
        book_type1 = r'<a href=".*?" target="_blank" data-eid=".*?">(.*?)</a>'  # 类型
        # 新增一个类型
        book_type2 = r'<a class="go-sub-type" data-typeid="\d*?" data-subtypeid="\d*?" href="javascript:" data-eid=".*?">(.*?)</a>'  # 类型
        book_state = r'<span >(.*?)</span>'  # 状态
        book_intro = r'<p class="intro">(.*?)</p>'  # 简介
        imgs = r'data-bid=".*?" data-eid=".*?" target="_blank"><img src="(.*?)"></a>'
        # book_link = r'<h4><a href="//book.qidian.com/info/1010734492" target="_blank" data-eid="qd_B58" data-bid="1010734492">.*?</a></h4>'  # 链接

        informations = book_name + r'.*?' + book_author + r'.*?' + book_type1 + \
                       r'.*?' + book_type2 + r'.*?' + book_state + r'.*?' + book_intro+ r'.*?' +imgs
        # 返回一个正则表达式对象
        # print(informations)
        reg = re.compile(informations, re.S)
        # 开始查找所有信息
        contents_list = re.findall(reg, data)
        print(contents_list)

        # 获取当前页面的html
        response = requests.get(page_url).text
        doc = pq(response)
        # 获取当前字体文件名称
        classattr = doc('p.update > span > span').attr('class')
        cla = doc('p.update > span > span')
        # print(cla)
        pattern = '</style><span.*?%s.*?>(.*?)</span>' % classattr
        # 获取当前页面所有被字数字符
        numberlist = re.findall(pattern, response)
        # 获取当前包含字体文件链接的文本
        fonturl = doc('p.update > span > style').text()
        # 通过正则获取当前页面字体文件链接
        url = re.search('woff.*?url.*?\'(.+?)\'.*?truetype', fonturl).group(1)
        cmap = self.get_font(url)

        contents = []
        # 遍历每一个作品信息，进行修改
        i = 0
        for content in contents_list:
            content = list(content)
            print(content)
            new_content = content[1:3]  # 书名+作者
            new_content.append('https:' + content[0])  # 链接
            new_content.append(content[3] + '-' + content[4])  # 类型
            new_content.append(content[5])  # 状态
            new_content.append(self.get_encode(cmap, numberlist[i][:-1]) + '万字')  # 字数
            new_content.append(content[6].strip())  # 简介
            # 添加到列表
            contents.append(new_content)
            # print(contents)
            i += 1

        return contents

    def write(self, contents, csv_writer):
        """保存内容"""
        for content in contents:
            csv_writer.writerow(content)

    def run(self, pages=1):
        # 设置分类
        fileheader = ['作品', '作者', '链接', '类型', '状态', '字数', '简介','图片']
        # 创建csv文件
        with open('qidian2.csv', 'w', newline='', encoding='gb18030') as f:
            csv_writer = csv.writer(f)
            # 把fileheader的内容写入csv文件中
            csv_writer.writerow(fileheader)
            # print(fileheader)
            for page in range(1, pages + 1):
                # 设置url
                page_url = self.base_url + str(page)
                # print(page_url)
                # 请求数据
                data = self.send_request(page_url)
                # 清洗数据
                contents = self.parse(data, page_url)
                # 写入数据
                self.write(contents, csv_writer)

Spider().run(1)
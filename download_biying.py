#! /usr/bin/env python
# coding:utf-8


import requests
from uuid import uuid4
from lxml import etree
import logging.handlers
import os


# path = os.path.dirname(os.path.abspath(__file__))
path = "D:\\PythonProject\\auto_wallpaper\\"

# img_path = os.path.join(path, "IMG")
img_path = path + "IMG\\"


formatter = logging.Formatter('[%(name)s] %(asctime)s [%(levelname)s] %(filename)s:%(lineno)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.handlers.RotatingFileHandler(os.path.join(path, "download.log"), maxBytes=1024 * 1024 * 20,
                                                    backupCount=3)
file_handler.setFormatter(fmt=formatter)
file_handler.setLevel(logging.INFO)
logging.root.addHandler(hdlr=file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(fmt=formatter)
console_handler.setLevel(logging.DEBUG)
logging.root.addHandler(hdlr=console_handler)

logging.root.setLevel(logging.NOTSET)


def get_uuid_str() -> str:
    return str(uuid4())


base_bing_url = "https://bing.ioliu.cn/?p="

if not os.path.exists(img_path):
    os.mkdir(img_path)

for i in range(1, 123):
    img_page_url = f"{base_bing_url}{i}"
    ret = requests.get(img_page_url)
    html = etree.HTML(ret.text)
    img_url_list = html.xpath("//img/@src")
    for img_url in img_url_list:
        try:
            logging.info(img_url)
            pic = requests.get(img_url)
            if pic.status_code == 200:
                with open(img_path+get_uuid_str()+".jpg", 'wb') as fp:
                    fp.write(pic.content)
                    fp.close()
            logging.info("下载完成")
        except Ellipsis as e:
            logging.exception(e)

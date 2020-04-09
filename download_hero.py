import requests
import json
import os
import time

start = time.time()
url = requests.get('http://pvp.qq.com/web201605/js/herolist.json').content
jsonFile = json.loads(url)  # 提取json

x = 0  # 计数器，记录下载了多少张图片
# 创建目录
# path = os.path.dirname(os.path.abspath(__file__))
path = "D:\\PythonProject\\auto_wallpaper\\"

# img_path = os.path.join(path, "IMG")
hero_dir = path + "IMG\\"

try:  # 使用一个简单的异常处理，防止代码在运行时出现错误
    for m in range(len(jsonFile) - 1):
        ename = jsonFile[m]['ename']  # 编号
        cname = jsonFile[m]['cname']  # 英雄名字
        skinName = jsonFile[m]['skin_name'].split('|')
        skinNumber = len(skinName)

        # 下载图片,构造图片网址
        for bigskin in range(1, skinNumber + 1):
            urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
                ename) + '-bigskin-' + str(bigskin) + '.jpg'
            picture = requests.get(urlPicture).content  # 获取图片的二进制信息
            with open(hero_dir + cname + "-" + skinName[bigskin - 1] + '.jpg', 'wb') as f:  # 保存图片
                f.write(picture)
                x = x + 1
                print("正在下载第" + str(x) + "张图片")
except Exception as e:
    print(e)

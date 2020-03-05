#! /usr/bin/env python
# coding:utf-8

import random
import ctypes
import time
import os
import logging.handlers


path = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(path, "IMG")

debug = False

formatter = logging.Formatter('[%(name)s] %(asctime)s [%(levelname)s] %(filename)s:%(lineno)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.handlers.RotatingFileHandler(os.path.join(path, "run.log"), maxBytes=1024 * 1024 * 20,
                                                    backupCount=3)
file_handler.setFormatter(fmt=formatter)
file_handler.setLevel(logging.INFO)
logging.root.addHandler(hdlr=file_handler)

if debug:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt=formatter)
    console_handler.setLevel(logging.DEBUG)
    logging.root.addHandler(hdlr=console_handler)

logging.root.setLevel(logging.NOTSET)

# 关闭终端
if not debug:
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)


while True:
    try:
        file = os.listdir(img_path)
        filepath = img_path + random.choice(file)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
        logging.info(f"更换壁纸{filepath}成功")
    except Exception as e:
        logging.exception(e)
        logging.error("壁纸更换失败")
    finally:
        time.sleep(1 * 60)

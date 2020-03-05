# auto_wallpaper

# 自动切换壁纸

## 必应壁纸

# 安装python3.8环境

# 第三方依赖包：
requests
lxml
pyinstaller

# 修改配置
    download_biying.py -> path  #auto_wallpaper的路径
    run.py -> path  #auto_wallpaper的路径

# 下载壁纸资源
    python3 download_biying.py

# 打包exe程序
    pyinstaller -F run.py

# 把dist下面的run.exe注册到计划任务，登陆时启动

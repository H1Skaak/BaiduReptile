# BaiduReptile

1、简介

通过selenium进行采集百度搜索url



2、安装依赖

```bash
pip3 install requests
pip3 install selenium
```

下载selenium浏览器驱动

1. 官方网站： https://sites.google.com/a/chromium.org/chrome

2. 下载地址 ：http://npm.taobao.org/mirrors/chromedriver/

需要先下载对应的浏览器，在下载对应版本的驱动器

将下好的驱动放到系统的环境变量中 这样比较方便启动。

3、使用

```bash
python  BaiduReptile.py 查询的关键字 页数
python  BaiduReptile.py 123 10
```


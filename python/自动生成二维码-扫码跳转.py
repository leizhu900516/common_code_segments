# -*- coding: utf-8 -*-
# @author: chenhuachao
# @Time: 2022/11/24 -13:56
# Filename: 自动生成二维码-扫码跳转.py
# Desc:
import qrcode

url = "http://1.192.217.143:8113/"

my_code = qrcode.make(data=url)
# 显示图片
my_code.show()
# 保存图片
my_code.save("./mycode.jpg", format="JPEG")
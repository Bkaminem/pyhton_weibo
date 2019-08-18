#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import sys
window = tk.Tk()

window.resizable(False, False)    #固定窗口大小
windowWidth = 960               #获得当前窗口宽
windowHeight = 640              #获得当前窗口高
screenWidth,screenHeight = window.maxsize()     #获得屏幕宽和高
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
window.geometry(geometryParam)    #设置窗口大小及偏移坐标

tk.Label(window, text='User name: ').place(x=50, y= 150)#创建一个`label`名为`User name: `置于坐标（50,150）


def get_yonghu_info():
     pass
var_usr_name = tk.StringVar()#定义变量
var_usr_name.set('example@python.com')#变量赋值'example@python.com'
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)#创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
entry_usr_name.place(x=160, y=150)
btn_login = tk.Button(window, text='Login', command=get_yonghu_info )#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
window.mainloop()

"""
@Time : 2022/6/6 11:19
@Author : sunny cao
@File : tkinter_demo.py
"""
import tkinter as tk
import hashlib
from tkinter import messagebox


class Tkinter_Demo(object):
    """
    :param root:root对象
    """
    def __init__(self, root):
        self.root = root

    def set_init_window(self, windows):
        root.title("数据转换工具")
        # 设置窗口大小
        root.geometry("550x400")
        # 设置窗口左上角图标
        root.iconbitmap('C:\\Users\\sunny\\Downloads\\favicon.ico')
        # 设置主窗口背景颜色
        root["background"] = "#c9c9c9"
        # 添加文本框
        title_txt = tk.Label(root, text="md5转换工具", bg="orange", fg="green", font=('Times', 20, 'bold italic'))
        # 将文本框添加至主窗口
        title_txt.pack()
        # 添加待转换字符输入框
        label = tk.Label(root, text="请输入：")

        # 添加待转换字符的输入框
        label = tk.Label(root, text="请输入：")
        label.pack()
        entry = tk.Entry(root)
        entry.pack(padx=20, pady=20)
        # 添加提交按钮
        submit_button = tk.Button(root, text="转换", command=lambda: windows.click_button(entry.get()))
        b = submit_button.pack()

    def click_button(self, content):
        md = hashlib.md5()
        md.update(content.encode("utf-8"))
        data = md.hexdigest()
        print("md5转换后：{0}".format(data))
        # 添加转换后的数据
        result = "转换后的数据为："+str(data)
        text = tk.Text(root, height=2)
        text.pack()
        text.insert("insert", result)


if __name__ == '__main__':
    root = tk.Tk()
    windows = Tkinter_Demo(root)
    windows.set_init_window(windows)
    root.mainloop()



import tkinter as tk
from tkinter import filedialog
__version__ = "0.0.1"
__all__ = ["get_download_path"]
__author__ = {"Name:":"jasper","名字：":"方黄旭","Email:":"fanghuangxu@163.com","邮箱：":"fanghuangxu@163.com"}

def select_download_path():
    download_path = filedialog.askdirectory()
    if download_path:
        return download_path
def GUI():
    # 创建主窗口
    root = tk.Tk()
    root.title("选择下载路径")

    # 创建选择路径按钮
    select_path_button = tk.Button(root, text="选择下载路径", command=select_download_path)
    select_path_button.pack(pady=20)

    # 运行主循环
    root.mainloop()

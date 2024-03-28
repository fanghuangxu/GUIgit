import os
import download_git
import get_download_path
path = get_download_path.GUI()
extract_folder = "GitGUI"
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)
print('开始下载git')
download_git.download(path=path+'\\'+extract_folder)
print('下载完成')

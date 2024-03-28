import zipfile
import os
from tqdm import tqdm
def path(new_path):
    # 获取当前的 PATH 环境变量的值
    current_path = os.environ.get('PATH', '')

    # 检查新路径是否已经在 PATH 中，如果不存在则添加
    if new_path not in current_path:
        new_path = new_path + os.pathsep + current_path
        os.environ['PATH'] = new_path

    # 打印更新后的 PATH 环境变量
    print(os.environ['PATH'])


def lzip(): 
    # 要解压的 Zip 文件路径
    zip_file = "fanghuangxu.zip"

    # 解压后的目标文件夹路径
    extract_folder = "Git"

    # 创建一个目标文件夹用于存放解压后的文件
    if not os.path.exists(extract_folder):
        os.makedirs(extract_folder)

    # 打开 Zip 文件
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # 获取压缩文件中的文件列表
        file_list = zip_ref.namelist()

        # 使用 tqdm 显示解压进度
        with tqdm(total=len(file_list)) as pbar:
            for file in file_list:
                zip_ref.extract(file, extract_folder)
                pbar.update(1)
        # 获取当前脚本所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path(new_path=current_dir+'\\Git\\bin')
def download():
    import requests
    from tqdm import tqdm

    url = "https://codeload.github.com/fanghuangxu/git/zip/refs/heads/master"
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0))

    with open("fanghuangxu.zip", "wb") as f:
        with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
            for data in r.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))

    lzip()

download()

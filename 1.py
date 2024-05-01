import requests
import os
def download_file(url, destination):
    # 发送 GET 请求下载文件
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code == 200:
        # 打开文件并写入下载的数据
        with open(destination, 'wb') as file:
            file.write(response.content)
        print("文件下载成功")
    else:
        print("文件下载失败")

# 指定远程文件的URL和本地保存路径
url = "http://aipe-speech.bj.bcebos.com/text_to_speech/2024-04-19/66222128417b2000014180c2/speech/0.mp3?authorization=bce-auth-v1%2FALTAKjI91nE52nvtDNRgFlUCVz%2F2024-04-19T07%3A45%3A49Z%2F259200%2F%2F4ae498ea8b30ee95587ea75aaf84a3095a6f7564b5f2d538e69e18673c169512"
destination = os.getcwd()+".mp3"
print(os.getcwd())

# 调用下载函数
download_file(url, destination)

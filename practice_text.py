import time
# -*- coding: utf-8 -*-
import requests
import json,pygame
from collections import deque
API_KEY = "Y6crpqYFjlDVSfOK61KElCgV"
SECRET_KEY = "88uMGuoFbJLAxH1TxTk3Hga4POeSsIBK"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
message = deque() #存贮文字内容，包含gpt返回文字
message_number = deque() #存贮访问的序列id号码
audio = deque()#存贮音频路径
file_name = "chat_gpt_answer.txt"
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_message():
    with open(file=file_name, mode="r", encoding="utf-8") as f:
        message.extend(f.read().split('\n'))
    print(f"当前文件内容如下：\n{message}")
def send_transparent_request(url):

    get_message()

    while True:
        if message:
            cur_text = message.popleft() #获取当前的文字信息，同时进行弹出
            print(cur_text)
            payload = json.dumps({
                "text": cur_text,
                "format": "mp3-16k",
                "voice": 0,
                "lang": "zh",
                "speed": 5,
                "pitch": 5,
                "volume": 5,
                "enable_subtitle": 0
            })

            response = requests.request("POST", url, headers=headers, data=payload)
            task_id = json.loads(response.text)["task_id"]
            message_number.append(task_id)
            # task_id = response["task_id"]
            print("开始执行")
        else:
            return
def get_result(url):
    while True:
        # if message_number == 0:
        #     print("队列内容已经执行完毕！！！\n-------------------------------\n---------------------------")
        #     break
        payload = json.dumps({"task_ids": list(message_number)})
        while True:
            response_1 = requests.request("POST", url, headers=headers, data=payload)
            file_status = json.loads(response_1.text)["tasks_info"][0]["task_status"]#记录当前的状态
            print(response_1.text)
            if file_status == "Success":
                print(response_1.text)
                viode_url = response_1.json()["tasks_info"][0]["task_result"]["speech_url"]
                print("当前网址下载url为")
                download_viode_file(viode_url)
                break

def download_viode_file(url):
    # 发送 GET 请求下载文件
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code == 200:
        file_name = "text_viode.mp3"
        # 打开文件并写入下载的数据
        print(response.text)
        with open("text_viode.mp3", 'wb') as file:
            file.write(response.content)
        print("文件下载成功,开始播放")
        play_audio(file_name)
    else:
        print("文件下载失败")

def play_audio(filename):
    # 初始化pygame
    pygame.init()

    try:
        # 加载音频文件
        pygame.mixer.music.load(filename)
        # 播放音频文件
        pygame.mixer.music.play()

        # 等待音频播放完毕
        while pygame.mixer.music.get_busy():
            continue

    except pygame.error as e:
        print("播放音频文件时出现错误:", e)

    finally:
        # 退出pygame
        pygame.quit()
def sum_result():
    url_0 = "https://aip.baidubce.com/rpc/2.0/tts/v1/create?access_token=" + get_access_token()
    url_1 = "https://aip.baidubce.com/rpc/2.0/tts/v1/query?access_token=" + get_access_token()
    send_transparent_request(url_0)
    get_result(url_1)

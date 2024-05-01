import json
import time,os
import re
import requests,subprocess
from practice_text import sum_result
import datetime
file_path = "vidoe_transparent.text"
def get_text():
    with open(file=file_path, mode='r', encoding="utf-8") as f:
        text = f.read().rstrip('\n')
        with open(file=file_path, mode='w', encoding="utf-8") as f:
            f.write("")
    return text

def send_and_get_requests(voice=0):
    while True:
        if voice:
            text = get_text()
        else:
            text = input("请输入你想要提问的内容")
        body = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": text,
                }
            ],
            "presence_penalty": 0,
            "temperature": 0.5,
            "stream": True,
            "top_p":1
        }
        headers = {
            "Authorization": "Bearer sk-JfEQ3ZcEBorTO1N47b570e02E9Cc4d47892170Da28271dF8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
            "Content-Type":"application/json",
            "Origin":"https://chat.burn.hair",
            "Priority":"u=1, i",
            "Referer":"https://chat.burn.hair/",
            # "Sec-Ch-Ua":""Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99""
            "Sec-Ch-Ua-Mobile":"?0",
            "Sec-Ch-Ua-Platform":"Windows",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-site",
        }
        # time.sleep(3)
        r = requests.post(url = "https://burn.hair/v1/chat/completions", headers = headers, json = body)
        print(f"成功建立请求链接，状态码{r.status_code}")
        # print(r.content.decode("utf-8"),r.status_code)
        message = r.content.decode("utf-8")
        print(message)
        match = re.findall(r'content":"([^"]+)"', message)

        text_1 = "".join(match).replace("\\n",'')
        if match and voice:
            print(text_1)
            with open("chat_gpt_answer.txt", "w", encoding="utf-8") as f:
                f.write(text_1)
                sum_result()

        if match and not voice:

            # 指定记事本文件路径
            notepad_path = r"C:\Windows\System32\notepad.exe"

            # 要打开的记事本文件路径
            # file_path = r"path\to\your\file.txt"

            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            current_datetime = datetime.datetime.now()
            # 指定要创建的文件路径
            file_path = os.path.join(desktop_path, 'daily.txt')
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding="utf-8") as f:
                    text_2 = "PANPAN的chatgpt爬虫日志"
                    total_width = 160  # 假设文本总宽度为80个字符
                    left_spaces = (total_width - len(text_2)) // 2
                    right_spaces = total_width - len(text_2) - left_spaces

                    # 生成居中的文本
                    centered_text = "-" * left_spaces + text_2 + "-" * right_spaces

                    f.write(centered_text+'\n')
            # 获取桌面路径
            with open(file_path,"a",encoding='utf-8') as f:
                print("结果:", text_1)
                f.write(f"时间：{current_datetime}\n问题:{text}\n回答:{text_1}\n")
                print("日志内容以写入完成，可以进行查看")

                # 使用subprocess打开记事本文件
                subprocess.Popen([notepad_path, file_path])
            yes = input("是否需要继续问答y/n")
            if yes.upper() == "N":
                break
            print("正在重新建立网络请求..............")
            time.sleep(3)
            print("完成！！！")
        # 获取字典中键为 'content' 的
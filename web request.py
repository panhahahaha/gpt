import time
import json, requests

Context = [{"role": "user", "content": "你的名字是哮天犬，作为一个四足机器人来回答我的问题"}]
data = {
        "frequence_penalty" : 0,
        "model": "gpt-3.5-turbo(OpenAI)",
        "messages": [
            {
                "role": "assistant ",
                "content": "111111。"
            }
        ],
        "stream":False,
        "temperature": 0.7,
        "top_p": 1
    }

def gpt(message):
     global Context,data
     if len(Context) > 8:
          Context = [{"role": "user", "content": "你的名字是哮天犬,作为一个四足机器人来回答我的问题"}]
     Context.append({"role": "user", "content": message})
     response = requests.post(" https://burn.hair/v1/chat/completions", headers={
          # "Content-Type": "application/json",
          "Authorization": "Bearer sk-JfEQ3ZcEBorTO1N47b570e02E9Cc4d47892170Da28271dF8"
     },
     data = data)
     print(data)
     print(response.status_code)
     print(response.text)
     s = response.json()
     print(s)
     # print("响应：" + data['choices'][0]['message']['content'])

     Context.append(data['choices'][0]['message'])
gpt("fsdefesdv")
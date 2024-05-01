# -*- coding: utf-8 -*-

import os,time
import subprocess

# from practice_voide import sum_step
from voide_db_test import detect_volume2
from gpt import send_and_get_requests
import constant
fucntion_tools = ['pygame', 'urllib3', 'torch', 'requests', 'numpy', 'h5py', 'matplotlib', 'h11','subprocess' ]
lack_pack = []
constant.main_file_path = os.getcwd()
print(constant.main_file_path)
class User:
    def __init__(self,using_voice:bool):
        self.using_voice = using_voice
def main():
    using_voice = False
    while 1:
        s = input("是否需要语音环境 Y/N")
        if s.upper() == 'Y':
            using_voice = True
            break
        elif s.upper() == 'N':
            using_voice = False
            break

    user = User(using_voice=using_voice)
    # detect_volume2()
    if user.using_voice:
        detect_volume2()
    else:
        send_and_get_requests()
# main()
print("正在检测当前配置包环境 -/ -/ -/ -/")
def check_and_install(package_name):
        try:
            __import__(package_name)
        except ImportError:
            lack_pack.append(package_name)

for nums, item in enumerate(fucntion_tools):
    print(f"\r进度:", "*"*(nums+1), " "*(len(fucntion_tools) - nums), "||||", f"正在验证包：{item}" , end="",sep = "", flush=True)
    check_and_install(item)
    # time.sleep(1)
print(f"\n验证完成————————————————：缺失包有：{lack_pack}")
for item in lack_pack:
    print(f"正在修复包：{item}", flush=True)
    subprocess.run(['pip', 'install',item ])
main()

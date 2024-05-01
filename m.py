

import pyaudio
import numpy as np
from file_retrieve import list_files_with_suffix
from practice_voide import sum_step
import constant
# 设置阈值（分贝）
threshold_db = 30
print("using")
# 定义音量检测函数
def detect_volume(stream, chunk_size=1024):
    data = stream.read(chunk_size)
    # 将二进制数据转换为NumPy数组
    audio_data = np.frombuffer(data, dtype=np.int16)
    # 计算音量（分贝）
    volume = 20 * np.log10(np.sqrt(np.mean(audio_data ** 2)))
    return volume

def detect_volume2() -> bool:
    # 创建PyAudio对象
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    try:
        while True:
            # 检测当前音量
            volume = detect_volume(stream)
            print("当前音量大小:", volume)

            # 如果音量大于阈值，则启动程序
            if volume > threshold_db:
            print("音量大小超过阈值，开始进行记录")
            #这里保留一个开始进行录音的接口启动程序
            stream.stop_stream()
             stream.close()
             p.terminate()
             sum_step()
    finally:
        # 关闭音频流
        return True
if __name__ == "__main__":
    detect_volume2()



from gpiozero import InputDevice
from signal import pause

# 定义震动信号输入引脚
vibration_pin = 18

# 创建输入设备对象
vibration_sensor = InputDevice(vibration_pin)

def detect_vibration():
    """
    检测震动信号的回调函数
    """
    if vibration_sensor.is_active:
        print("检测到震动！")

# 注册回调函数，当检测到震动时触发
vibration_sensor.when_activated = detect_vibration

try:
    # 持续监听震动信号，直到程序被中断
    pause()
except KeyboardInterrupt:
    print("程序已终止")

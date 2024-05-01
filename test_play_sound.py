import pygame

# 初始化 Pygame
pygame.init()

# 加载声音文件
sound = pygame.mixer.Sound("text_viode.mp3")

# 播放声音
sound.play()

# 等待声音播放完成
pygame.time.wait(int(sound.get_length() * 1000))

# 退出 Pygame
pygame.quit()


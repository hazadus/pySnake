# https://skillbox.ru/media/code/sozdayem-pervuyu-igru-na-python-i-pygame/
# https://www.pygame.org/wiki/GettingStarted

import pygame

pygame.init()

dis = pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption("Hazardous Snake")  # Добавляем название игры.

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)  # Выводить в терминал все произошедшие события.

pygame.quit()
quit()

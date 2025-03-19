#mickey the clocks

import pygame
import sys
import time
import math

pygame.init()

s_w = 800
s_h = 800
screen = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("Mickey Clock")

picture=pygame.image.load("c:\\Users\\USER\\Downloads\\mickeyclock.jpeg")
pygame.display.set_icon(picture)

done = False

left = pygame.image.load("C:\\Users\\USER\\Downloads\\left-hand.png")
right = pygame.image.load("c:\\Users\\USER\\Downloads\\right-hand.png")
body = pygame.image.load("c:\\Users\\USER\\Downloads\\main-clock.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    time_now = time.localtime()
    second = -(time_now.tm_sec / 60) * 360
    minute = -(((time_now.tm_min + time_now.tm_sec / 60) / 60) * 360)

    left_hand = pygame.transform.rotate(left, second)
    right_hand = pygame.transform.rotate(right, minute)


    screen.fill((255, 255, 255))

    
    screen.blit(body, (s_w // 2 - body.get_width() // 2, s_h // 2 - body.get_height() // 2))
    
    
    screen.blit(left_hand, (s_w // 2 - left_hand.get_width() // 2, s_h // 2 - left_hand.get_height() // 2))
    screen.blit(right_hand, (s_w // 2 - right_hand.get_width() // 2, s_h // 2 - right_hand.get_height() // 2))

    
    pygame.display.flip()

    
    pygame.time.delay(100)


pygame.quit()
sys.exit()

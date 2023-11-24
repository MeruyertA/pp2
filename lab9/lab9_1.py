import pygame
import sys
from datetime import datetime

pygame.init()

wid, hei = 800, 600
window = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Mickey's clock")
background = pygame.image.load("main-clock.png")  
right = pygame.image.load("right-hand.png")  
left = pygame.image.load("left-hand.png")  

def rotating(image, angle):
    return pygame.transform.rotate(image, angle)
clocking = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    current = datetime.now().time()
    min = current.minute
    sec = current.second
    angle_min = -(min * 6) 
    angle_sec = -(sec * 6) 

    right_rot = rotating(right, angle_min)
    left_rot = rotating(left, angle_sec)
    window.blit(pygame.transform.scale(background, (wid, hei)), (0, 0))
    window.blit(right_rot, (wid // 2 - right_rot.get_width() // 2, hei // 2 - right_rot.get_height() // 2))
    window.blit(left_rot, (wid // 2 - left_rot.get_width() // 2, hei // 2 - left_rot.get_height() // 2))

    pygame.display.flip()
    clocking.tick(60) 

import pygame

pygame.init()

width, height = 600, 400
radius_ball = 25
size_ball = 2 * radius_ball
moving_num = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red ball moving")

pos_x = width // 2
pos_y = height // 2

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (pos_x, pos_y), radius_ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if pos_y - moving_num >= radius_ball:
                    pos_y -= moving_num
            elif event.key == pygame.K_DOWN:
                if pos_y + moving_num <= height - radius_ball:
                    pos_y += moving_num
            elif event.key == pygame.K_LEFT:
                if pos_x - moving_num >= radius_ball:
                    pos_x -= moving_num
            elif event.key == pygame.K_RIGHT:
                if pos_x + moving_num <= width - radius_ball:
                    pos_x += moving_num

    pygame.display.flip()


pygame.quit()

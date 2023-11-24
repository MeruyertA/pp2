import pygame

pygame.init()
pygame.mixer.init()

music = ['track01.mp3', 'track02.mp3', 'track03.mp3', 'track04.mp3', 'track05.mp3']
t_num = 0
paused = False

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("mp3")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def knopki():
    screen.fill(GREEN)
    font = pygame.font.SysFont(None, 36)
    playing = font.render('play/pause', True, WHITE)
    stopping = font.render('stop', True, WHITE)
    next_track = font.render('next', True, WHITE)
    previous_track = font.render('previous', True, WHITE)
    screen.blit(playing, (30, 30))
    screen.blit(stopping, (30, 80))
    screen.blit(next_track, (30, 150))
    screen.blit(previous_track, (30, 190))

pygame.mixer.music.load(music[t_num])
pygame.mixer.music.play(-1)

run = True

while run:
    knopki()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 20 <= mouse[0] <= 150 and 20 <= mouse[1] <= 50:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif 20 <= mouse[0] <= 150 and 70 <= mouse[1] <= 100:
                pygame.mixer.music.stop()
                paused = False
            elif 20 <= mouse[0] <= 150 and 120 <= mouse[1] <= 150:
                t_num = (t_num + 1) % len(music)
                pygame.mixer.music.load(music[t_num])
                pygame.mixer.music.play(-1)
                paused = False
            elif 20 <= mouse[0] <= 150 and 170 <= mouse[1] <= 200:
                t_num = (t_num - 1) % len(music)
                pygame.mixer.music.load(music[t_num])
                pygame.mixer.music.play(-1)
                paused = False

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()

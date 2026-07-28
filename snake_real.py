import pygame
import random

clock = pygame.time.Clock()

pygame.init()




screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')


square = pygame.Surface((20, 20))
square.fill((36,255,20))
snake_x = 400
snake_y = 300


dx = +20
dy = 0



apple = pygame.Surface((20, 20))
apple.fill((255, 0, 0))




apple_x = random.randint(0, 800)
apple_y = random.randint(0, 600)




running = True




while running:
    screen.fill(('black'))
    screen.blit(square, (snake_x, snake_y))
    screen.blit(apple, (apple_x, apple_y))






    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        dx = 0
        dy = -20
    if keys[pygame.K_RIGHT]:
        dx = +20
        dy = 0
    if keys[pygame.K_LEFT]:
        dx = -20
        dy = 0
    if keys[pygame.K_DOWN]:
        dx = 0
        dy = 20
    snake_x += dx
    snake_y += dy



    if snake_x < 0 or snake_x > 800:
        running = False
        pygame.quit()
    if snake_y < 0 or snake_y > 600:
        running = False
        pygame.quit()





    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



    clock.tick(5)

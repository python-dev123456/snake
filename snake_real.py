import pygame
import random

clock = pygame.time.Clock()

pygame.init()




screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')


snake = pygame.Surface((20, 20))
snake.fill((36,255,20))
snake1 = pygame.Surface((20, 20))
snake1.fill((0, 0, 255))
snake_x = 400
snake_y = 300



snake_els = []



dx = +20
dy = 0



apple = pygame.Surface((20, 20))
apple.fill((255, 0, 0))




apple_x = random.randint(0, 39) * 20
apple_y = random.randint(0, 29) * 20


old_head_pos = []


running = True




while running:
    screen.fill(('black'))
    screen.blit(apple, (apple_x, apple_y))
    old_head_pos.insert(0, (snake_x, snake_y))







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
    screen.blit(snake, (snake_x, snake_y))


    if apple_x == snake_x and apple_y == snake_y:
        apple_x = random.randint(0, 39) * 20
        apple_y = random.randint(0, 29) * 20
    else:
        old_head_pos.pop()

    
    if old_head_pos:
        for i in old_head_pos:
            screen.blit(snake, (i))



    if snake_x < 0 or snake_x > 800:
        running = False
        pygame.quit()
    if snake_y < 0 or snake_y > 600:
        running = False

    if running == False:
        pygame.quit()
    else:





        pygame.display.update()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()



    clock.tick(5)

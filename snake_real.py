import pygame

clock = pygame.time.Clock()

pygame.init()




screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')
icon = pygame.image.load('imgs/51c682403e35afce960e7e039d68bd8d_t.jpeg')
# pygame.display.set_icon(icon)


square = pygame.Surface((20, 20))
square.fill((36,255,20))
square_x = 400
square_y = 300






running = True




while running:
    screen.fill(('black'))
    screen.blit(square, (square_x, square_y))


    square_x -= 20




    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        square_y -= 20
        square_x += 20
    if keys[pygame.K_RIGHT]:
        square_x += 40








    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



    clock.tick(5)
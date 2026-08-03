import pygame
import random
from tkinter import *


game = True


while game:

    tkinter = True

    while tkinter:
        win = Tk()
        win.geometry('800x600')
        win.title('Меню')
        win.config(bg='black')

        def f():
            global tkinter
            tkinter = False
            win.destroy()
            

        lbl = Label(text='Змейка', foreground='red', bg='black', width=10, height=3, bd=0)
        lbl.pack()
        btn = Button(text='Играть', foreground='red', bg='black', width=10, height=3, bd=0, command=f)
        btn.pack()









        win.mainloop()



    if tkinter == False:

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




    if running == False and tkinter == False:
        win_r = Tk()
        win_r.title('Экран проигрыша')
        win_r.geometry('800x600')
        win_r.config(bg='black')

        lbl1 = Label(text='Вы проиграли', foreground='red', bg='black', width=10, height=3, bd=0)
        lbl1.pack()

        def f1():
            global tkinter
            tkinter = True
            win_r.destroy()

        def f2():
            global game
            game = False
            win_r.destroy()

        btn1 = Button(text='Начать заново', foreground='red', bg='black', width=10, height=3, bd=0, command=f1)
        btn1.pack()
        btn2 = Button(text='Выйти из игры', foreground='red', bg='black', width=10, height=3, bd=0, command=f2)
        btn2.pack()

        win_r.mainloop()



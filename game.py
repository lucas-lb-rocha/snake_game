import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('sounds/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

noise_when_losing = pygame.mixer.Sound('sounds/smw_ludwig_morto.wav')
noise_to_pick_apple = pygame.mixer.Sound('sounds/smw_kick.wav')

largura = 640
altura = 480

x_snake = int(largura/2) 
y_snake = int(altura/2)

velocidade = 10
x_control = velocidade
y_control = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

points = 0
font = pygame.font.SysFont('arial', 40, bold=True, italic=True)

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
snake_list = []
length_initial = 5
game_over = False

def increase_snake(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(screen, (0,0,255), (XeY[0], XeY[1], 20, 20))

def restart_game():
    global points, length_initial, x_snake, y_snake, head_list, snake_list, x_maca, y_maca, game_over
    points = 0
    length_initial = 5
    x_snake = int(largura/2) 
    y_snake = int(altura/2)
    head_list = []
    snake_list = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    game_over = False

def verify_game_over():
    if (snake_list.count(head_list) > 1):
        screen.fill((255,255,255)) # Cria uma screen em branco
        noise_when_losing.play()   # Lanca o barulho de game over

        # Criacao da mensagem para a screen
        font_to_restart = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Press the R key to play again.'
        formatted_text = font_to_restart.render(mensagem, True, (0,0,0))
        ret_texto = formatted_text.get_rect()
        ret_texto.center = (largura//2, altura//2)
        screen.blit(formatted_text, ret_texto)
        pygame.display.update()

        return True
    return False

if __name__ == "__main__":

    while True:
        clock.tick(30)
        screen.fill((255,255,255))
        
        mensagem = f'Points: {points}'
        formatted_text = font.render(mensagem, True, (0,0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    if (x_control == velocidade):
                        pass
                    else:
                        x_control = -velocidade
                        y_control = 0
                if event.key == K_d:
                    if (x_control == -velocidade):
                        pass
                    else:
                        x_control = velocidade
                        y_control = 0
                if event.key == K_w:
                    if (y_control == velocidade):
                        pass
                    else:
                        x_control = 0
                        y_control = -velocidade
                if event.key == K_s:
                    if (y_control == -velocidade):
                        pass
                    else:
                        x_control = 0
                        y_control = velocidade
        
        x_snake = x_snake + x_control
        y_snake = y_snake + y_control

        cobra = pygame.draw.rect(screen, (0,0,255), (x_snake,y_snake,20,20))
        maca = pygame.draw.rect(screen, (255,0,0), (x_maca,y_maca,20,20))
        
        if cobra.colliderect(maca):
            x_maca = randint(40, 600)
            y_maca = randint(50, 430)
            points += 1
            noise_to_pick_apple.play()
            length_initial = length_initial + 1

        head_list = []
        head_list.append(x_snake)
        head_list.append(y_snake)
        
        snake_list.append(head_list)

        if (verify_game_over()):
            game_over = True
            while game_over:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            restart_game()  

        if (x_snake > largura):
            x_snake = 0
        if (x_snake < 0):
            x_snake = largura
        if (y_snake < 0):
            y_snake = altura
        if (y_snake > altura):
            y_snake = 0

        if (len(snake_list) > length_initial):
            del snake_list[0]

        increase_snake(snake_list)

        screen.blit(formatted_text, (0,40))

        pygame.display.update()
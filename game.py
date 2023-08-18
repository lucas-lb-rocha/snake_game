import pygame
from pygame.locals import *
from sys import exit
from Snake import Snake

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('sounds/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

noise_when_losing = pygame.mixer.Sound('sounds/smw_ludwig_morto.wav')
noise_to_pick_apple = pygame.mixer.Sound('sounds/smw_kick.wav')

largura = 640
altura = 480

font = pygame.font.SysFont('arial', 40, bold=True, italic=True)

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

if __name__ == "__main__":
    snake = Snake()

    while True:
        clock.tick(30)
        screen.fill((255,255,255))
        pygame.display.set_caption('Game')

        mensagem = f'Points: {snake.points}'
        formatted_text = font.render(mensagem, True, (0,0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    if (snake.x_control == snake.velocidade):
                        pass
                    else:
                        snake.x_control = -snake.velocidade
                        snake.y_control = 0
                if event.key == K_d:
                    if (snake.x_control == -snake.velocidade):
                        pass
                    else:
                        snake.x_control = snake.velocidade
                        snake.y_control = 0
                if event.key == K_w:
                    if (snake.y_control == snake.velocidade):
                        pass
                    else:
                        snake.x_control = 0
                        snake.y_control = -snake.velocidade
                if event.key == K_s:
                    if (snake.y_control == -snake.velocidade):
                        pass
                    else:
                        snake.x_control = 0
                        snake.y_control = snake.velocidade
        
        snake.x = snake.x + snake.x_control
        snake.y = snake.y + snake.y_control

        snake_position = pygame.draw.rect(screen, (0,0,255), (snake.x,snake.y,20,20))
        apple_position = pygame.draw.rect(screen, (255,0,0), (snake.Apple.x,snake.Apple.y,20,20))
        
        if snake_position.colliderect(apple_position):
            snake.Apple.updateXandY()
            snake.points += 1
            noise_to_pick_apple.play()
            snake.length_initial = snake.length_initial + 1        

        snake.head_list = []
        snake.head_list.append(snake.x)
        snake.head_list.append(snake.y)
        
        snake.snake_list.append(snake.head_list)

        if (snake.verify_game_over(screen)):
            noise_when_losing.play()   # Lanca o barulho de game over
            snake.game_over = True
            while snake.game_over:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            snake.restart_game()  

        if (snake.x > largura):
            snake.x = 0
        if (snake.x < 0):
            snake.x = largura
        if (snake.y < 0):
            snake.y = altura
        if (snake.y > altura):
            snake.y = 0

        if (len(snake.snake_list) > snake.length_initial):
            del snake.snake_list[0]

        snake.increase_snake(screen)

        screen.blit(formatted_text, (0,40))

        pygame.display.update()
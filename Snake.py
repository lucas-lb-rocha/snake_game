from random import randint
import pygame
from pygame.locals import *

class Snake:
    largura = 640
    altura = 480
    velocidade = 10

    def __init__(self) -> None:
        self.x_snake = int(self.largura/2) 
        self.y_snake = int(self.altura/2)

        self.x_control = self.velocidade
        self.y_control = 0

        self.x_maca = randint(40, 600)
        self.y_maca = randint(50, 430)
        
        self.points = 0
        self.font = pygame.font.SysFont('arial', 40, bold=True, italic=True)

        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()
        self.head_list = []
        self.snake_list = []
        self.length_initial = 5

        self.game_over = False
    
    def restart_game(self):
        self.points = 0
        self.length_initial = 5
        self.x_snake = int(self.largura/2) 
        self.y_snake = int(self.altura/2)
        self.head_list = []
        self.snake_list = []
        self.x_maca = randint(40, 600)
        self.y_maca = randint(50, 430)
        self.game_over = False

    def increase_snake(self):
        for XeY in self.snake_list:
            pygame.draw.rect(self.screen, (0,255,0), (XeY[0], XeY[1], 20, 20))

    def verify_game_over(self):
        if (self.snake_list.count(self.head_list) > 1):
            self.screen.fill((255,255,255)) # Cria uma screen em branco
            self.noise_when_losing.play()   # Lanca o barulho de game over

            # Criacao da mensagem para a screen
            font_to_restart = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game over! Press the R key to play again.'
            formatted_text = font_to_restart.render(mensagem, True, (0,0,0))
            ret_texto = formatted_text.get_rect()
            ret_texto.center = (self.largura//2, self.altura//2)
            self.screen.blit(formatted_text, ret_texto)
            pygame.display.update()

            return True
        return False
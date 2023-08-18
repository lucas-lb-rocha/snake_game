from random import randint
import pygame
from pygame.locals import *
from Apple import Apple

class Snake:
    largura = 640
    altura = 480
    velocidade = 10

    def __init__(self) -> None:
        self.x = int(self.largura/2) 
        self.y = int(self.altura/2)

        self.x_control = self.velocidade
        self.y_control = 0

        self.Apple = Apple()
        
        self.points = 0
        self.font = pygame.font.SysFont('arial', 40, bold=True, italic=True)

        self.head_list = []
        self.snake_list = []
        self.length_initial = 5
        self.game_over = False
    
    def restart_game(self) -> None:
        self.points = 0
        self.length_initial = 5
        self.x = int(self.largura/2) 
        self.y = int(self.altura/2)
        self.head_list = []
        self.snake_list = []
        self.Apple.updateXandY()
        self.game_over = False

    def increase_snake(self, screen: pygame.display) -> None:
        for XeY in self.snake_list:
            pygame.draw.rect(screen, (0,0,255), (XeY[0], XeY[1], 20, 20))

    def verify_game_over(self, screen: pygame.display) -> bool:
        if (self.snake_list.count(self.head_list) > 1):
            screen.fill((255,255,255)) # Cria uma screen em branco
            
            # Criacao da mensagem para a screen
            font_to_restart = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game over! Press the R key to play again.'
            formatted_text = font_to_restart.render(mensagem, True, (0,0,0))
            ret_texto = formatted_text.get_rect()
            ret_texto.center = (self.largura//2, self.altura//2)
            screen.blit(formatted_text, ret_texto)
            pygame.display.update()

            return True
        return False
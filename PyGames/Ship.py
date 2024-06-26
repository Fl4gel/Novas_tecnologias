import pygame

class Ship():
        
    def __init__(self,screen):

        self.screen = screen
        self.image = pygame.image.load('IMG/ship.png')
        self.image_size = (100,100)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1
        if self.moving_up:
            self.rect.centery -=1
        if self.moving_down:
            self.rect.centery +=1
        


    def blitme(self):
        """Desenha a espaçonave na posição inicial"""

        self.screen.blit(self.image, self.rect)
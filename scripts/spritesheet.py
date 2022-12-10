import pygame

class Spritesheet:
    def __init__(self, file):
        self.spritesheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))

        #carrega imagem da posição (x,y) com tamanho (w,h) na superficie
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite
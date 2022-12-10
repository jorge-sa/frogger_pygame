import pygame

class Car:
    def __init__(self, x, y, direcao, speed, sprite):
        self.speed = speed
        self.direcao = direcao
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, sprite.get_width(), sprite.get_height())
        self.surf = True

    def run(self, screen_size, dt, x=0):
        self.x += self.speed * self.direcao * dt
        self.rect.x = self.x
        self.rect.y = self.y

        if self.x > screen_size+self.sprite.get_width():
            self.x = x - self.sprite.get_width()

        if self.x < self.sprite.get_width()*(-1):
            self.x = screen_size+self.sprite.get_width()
    
    def draw(self, screen, dt, x=0):
        self.run(screen.get_width(), dt, x)
        screen.blit(self.sprite, (self.x, self.y))
        #pygame.draw.rect(screen, (255,0,150), self.rect, 1)
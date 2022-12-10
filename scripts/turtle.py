import pygame
from scripts.car import Car

class Turtle(Car):
    def __init__(self, x, y, direcao, speed, sprites, sink):
        super().__init__(x, y, direcao, speed, sprites[0])
        self.sprite = sprites
        self.current_sprite = 0
        self.sink = sink
        no_sprite = pygame.Surface((16,16))
        no_sprite.fill((0,0,71))
        self.sprite.append(no_sprite)
        self.sprite.append(self.sprite[4])
        self.sprite.append(self.sprite[3])
        self.sprite.append(self.sprite[2])
        if self.sink:
            self.limit = 9
        else:
            self.limit = 3
        self.surf = True

    def run(self, screen_size, dt, x=0):

        #move
        self.x += self.speed * self.direcao * dt

        #update sprite
        self.current_sprite += 2*dt
        if int(self.current_sprite) == 5:
            self.surf = False
        else:
            self.surf = True
        if self.current_sprite > self.limit:
            self.current_sprite = 0

        #update rect pos
        self.rect.x = self.x
        self.rect.y = self.y

        if self.x > screen_size+self.sprite[0].get_width():
            self.x = x - self.sprite[0].get_width()

        if self.x < self.sprite[0].get_width()*(-1):
            self.x = screen_size+self.sprite[0].get_width()
    
    def draw(self, screen, dt, x=0):
        self.run(screen.get_width(), dt, x)
        screen.blit(self.sprite[int(self.current_sprite)], (self.x, self.y))
        #pygame.draw.rect(screen, (205,200,70), self.rect, 1)
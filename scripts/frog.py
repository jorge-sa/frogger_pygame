import pygame

class Frog(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        self.vidas = 7
        self.x_inicial = x
        self.y_inicial = y
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x+2,y+2,12,12)
        self.sprites = sprites
        self.draw_sprite = sprites[0]
        self.jump = 16
        self.direcao = 0
        self.attached = False
        self.jump_sound = pygame.mixer.Sound("./sounds/pulo.wav")
        self.dead_sound = pygame.mixer.Sound("./sounds/perde_2.wav")
        self.moving = False
        self.counter = 0
        self.previous_pos = None

    def move(self, direction):
        self.moving = True
        self.previous_pos = (self.x, self.y)
        self.counter = 0
        if direction == 'up':
            self.direcao = 0
            #self.y -= self.jump
            print('up')
        elif direction == 'down':
            self.direcao = 180
            #self.y += self.jump
            print('down')
        elif direction == 'left':
            self.direcao = 90
            #self.x -= self.jump
            print('left')
        elif direction == 'right':
            self.direcao = 270
            #self.x += self.jump
            print('right')

        self.jump_sound.play()
        #self.rect.x = self.x+2
        #self.rect.y = self.y+2

    def draw(self, screen):
        sapo_rotate = pygame.transform.rotate(self.draw_sprite, self.direcao)
        screen.blit(sapo_rotate, (self.x, self.y))
        #pygame.draw.rect(screen, (0,100,255), self.rect, 1)

    def update(self, dt):
        if self.moving:
            self.draw_sprite = self.sprites[1]
            self.counter += (self.jump*8)*dt
            if self.counter >= self.jump:
                self.moving = False
            print(self.counter >= self.jump)
            print(self.counter)
            if self.direcao == 0:
                self.y = self.previous_pos[1]+(int(self.counter) if self.counter < 17 else 16)*(-1)
            elif self.direcao == 90:
                self.x = self.previous_pos[0]+(int(self.counter) if self.counter < 17 else 16)*(-1)
            elif self.direcao == 180:
                self.y = self.previous_pos[1]+(int(self.counter) if self.counter < 17 else 16)
            else:    
                self.x = self.previous_pos[0]+(int(self.counter) if self.counter < 17 else 16)

            self.rect.x = self.x+2
            self.rect.y = self.y+2
        else:
            self.draw_sprite = self.sprites[0]

    def kill(self, coliders):
        if self.rect.collidelist(coliders) != -1 or (self.rect.y < 128 and self.attached == False):
            self.vidas -= 1
            self.dead_sound.play()
            self.moving = False
            self.reset()

    def attach(self, objects, dt):
        for obj in objects:
            self.attached = False
            for sub_obj in obj.objeto:
                if self.rect.collidelist([sub_obj.rect]) != -1 and sub_obj.surf:
                    self.attached = True
            else:
                if self.attached:
                    self.x += obj.speed*obj.direcao*dt
                    self.rect.x = self.x+2
                    break
    
    def reset(self):
        self.moving = False
        self.x = self.x_inicial
        self.y = self.y_inicial
        self.rect.x = self.x+2
        self.rect.y = self.y+2
        self.direcao = 0
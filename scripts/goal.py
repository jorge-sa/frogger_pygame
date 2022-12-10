import pygame

class Goal:
    def __init__(self, x, y, sprite):
        self.catch = False
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, 16, 16)
        self.alert = pygame.mixer.Sound("./sounds/chegada.wav")

    def update(self, frog):
        if self.rect.colliderect(frog.rect) and not self.catch:
            self.catch = True
            self.alert.play()
            frog.reset()
            return 150
        else:
            return 0

    def draw(self, screen):
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)
        if self.catch:
            screen.blit(self.sprite, (self.x, self.y))
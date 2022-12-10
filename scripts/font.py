import pygame

class Font:
    def __init__(self, image):
        alphanum = '0123456789abcdefghijklmnopqrstuvwxyz-*&'
        self.font_sheet = image
        self.chars = dict()

        y = 250
        x = 1
        for char in alphanum:
            self.chars.update({char: self.font_sheet.get_sprite(x, y, 8, 8)})
            x += 9
            if x > 145:
                x = 1
                y += 9
            print(char)
        self.chars.update({" ": pygame.Surface((8,8))})

    def write(self, screen, x, y, text):
        for char in text:
            screen.blit(self.chars[char], (x,y))
            x += 8
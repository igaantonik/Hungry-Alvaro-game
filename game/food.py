import pygame

class Food():
    def __init__(self, x, y, quantity, image):
        self.quantity = quantity
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # To do
    def draw(self, surface):
        return


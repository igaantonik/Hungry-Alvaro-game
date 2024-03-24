import pygame
from enum import Enum
class Topping_name(Enum):
    MOZZARELLA = 1
    FETA = 2
    BLUE_CHEESE = 3
    SALAMI = 4
    HAM = 5
    CHICKEN = 6
    MUSHROOMS = 7
    ONIONS = 8
    PEPPERS = 9
    OLIVES = 10
    CORN = 11
    TOMATOES = 12
    PINEAPPLE = 13
    SPINACH = 14
    ARUGULA = 15


class Topping():
    def __init__(self, x, y, name, quantity,scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.name = name
        self.quantity = quantity
        self.image = None
        self.rect = None


    def print_name(self):
        print(self.name.name)
    # To do
    def draw(self, surface):
        if self.name.value == 1:
            image = pygame.image.load("img/cheese.png")
            width, height = image.get_size()
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        if self.name.value == 4:
            image = pygame.image.load("img/salami.png")
            width, height = image.get_size()
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        if self.name.value == 13:
            image = pygame.image.load("img/pinapple.png")
            self.image = image
            width, height = image.get_size()
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        if self.name.value == 7:
            image = pygame.image.load("img/mashrooms.png")
            self.image = image
            width, height = image.get_size()
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
            surface.blit(self.image, (self.rect.x, self.rect.y))

        #  more to do
        else:
            return 0




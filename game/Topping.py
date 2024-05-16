import pygame
from enum import Enum


class ToppingName(Enum):
    CHEESE = 1
    SALAMI = 2
    MUSHROOMS = 3
    PINEAPPLE = 4
    HAM = 5
    SHRIMP = 6
    ANCHOVIES = 7
    PEPPERS = 8
    GREEN_OLIVES = 9
    BLACK_OLIVES = 10
    BACON = 11
    TOMATOES = 12
    ONIONS = 13
    SPINACH = 14
    ARUGULA = 15


class Topping():
    def __init__(self, x, y, name, quantity, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.name = name
        self.quantity = quantity
        self.image = None
        self.rect = None
        self.set_image()

    def set_image(self):
        if self.name.value == 1:
            self.image = pygame.image.load("img/cheese.png")

        if self.name.value == 2:
            self.image = pygame.image.load("img/salami_final.png")

        if self.name.value == 3:
            self.image = pygame.image.load("img/mashrooms_final.png")

        if self.name.value == 4:
            self.image = pygame.image.load("img/pinapple_final.png")

        if self.name.value == 5:
            self.image = pygame.image.load("img/ham_final.png")

        if self.name.value == 6:
            self.image = pygame.image.load("img/shrimp_final.png")

        if self.name.value == 7:
            self.image = pygame.image.load("img/anchovies_final.png")

        if self.name.value == 8:
            self.image = pygame.image.load("img/peppers_final.png")

        if self.name.value == 9:
            self.image = pygame.image.load("img/green_olives_final.png")

        if self.name.value == 10:
            self.image = pygame.image.load("img/black_olives_final.png")

        if self.name.value == 11:
            self.image = pygame.image.load("img/bacon_final.png")


        # more to do

    def draw(self, surface):
        if self.image:
            width, height = self.image.get_size()
            image = pygame.transform.scale(self.image, (int(width * self.scale), int(height * self.scale)))
            self.rect = image.get_rect()
            self.rect.topleft = (self.x, self.y)
            surface.blit(image, (self.rect.x, self.rect.y))

    def __str__(self):
        formatted_name = self.name.name.replace("_", " ")
        # formatted_name = self.name.name.replace("_", " ").title()
        return formatted_name

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


class Topping():
    IMAGE_PATHS = {
        ToppingName.CHEESE: "img/cheese.png",
        ToppingName.SALAMI: "img/salami_final.png",
        ToppingName.MUSHROOMS: "img/mashrooms_final.png",
        ToppingName.PINEAPPLE: "img/pinapple_final.png",
        ToppingName.HAM: "img/ham_final.png",
        ToppingName.SHRIMP: "img/shrimp_final.png",
        ToppingName.ANCHOVIES: "img/anchovies_final.png",
        ToppingName.PEPPERS: "img/peppers_final.png",
        ToppingName.GREEN_OLIVES: "img/green_olives_final.png",
        ToppingName.BLACK_OLIVES: "img/black_olives_final.png",
        ToppingName.BACON: "img/bacon_final.png"
    }

    def __init__(self, x, y, name, quantity, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.name = name
        self.quantity = quantity
        self.image = pygame.image.load(self.IMAGE_PATHS[name])
        self.rect = None

    def draw(self, surface):
        if self.image:
            width, height = self.image.get_size()
            image = pygame.transform.scale(self.image, (int(width * self.scale), int(height * self.scale)))
            self.rect = image.get_rect()
            self.rect.topleft = (self.x, self.y)
            surface.blit(image, (self.rect.x, self.rect.y))

    def __str__(self):
        formatted_name = self.name.name.replace("_", " ")
        return formatted_name

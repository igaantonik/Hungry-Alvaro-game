import pygame
import topping
import random

class Pizza():
    def __init__(self, x, y,scale):
        self.rect = None
        self.scale = scale
        self.image = pygame.image.load("img/dough_sauce.png")
        self.x = x
        self.y = y
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_toppings(self):
        for topping in self.toppings:
            topping.print_name()

    def generate_pizza(self, toppings_amount, min_amount_topping, max_amount_topping):
        available_toppings = [i for i in range(2,16)]
        cheese = topping.Topping(self.x, self.y, topping.Topping_name(1), 1,self.scale)
        self.toppings.append(cheese)
        for i in range(toppings_amount):
            rand_name = random.choice(available_toppings)
            available_toppings.remove(rand_name)
            rand_amount = random.randint(min_amount_topping, max_amount_topping)
            top = topping.Topping(self.x+ 50 * self.scale, self.y+50*self.scale, topping.Topping_name(rand_name), rand_amount,self.scale)
            self.add_topping(top)

    def draw(self, surface):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
        surface.blit(self.image, (self.rect.x, self.rect.y))
        for topping in self.toppings:
            topping.draw(surface)
        return 0

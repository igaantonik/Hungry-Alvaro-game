import time
from abc import ABC, abstractmethod

import pygame

import game.Button
import game.Game
import game.Button
import game.Topping
import game.Pizza
import game.Counter


class AbstractOrder(ABC):
    def __init__(self, pizza, toppings_amount, min_amount, max_amount, order_owner, mode, played_game):
        self.pizza = pizza
        self.played_game = played_game
        self.mode = mode
        self.toppings_amount = toppings_amount
        self.required_pizza = game.Pizza.Pizza(pizza.x, pizza.y, pizza.scale)
        self.required_pizza.generate_pizza(toppings_amount, min_amount, max_amount)
        self.counter = game.Counter.Counter(200, 80, played_game)
        self.pressed_topping = None
        self.order_owner = order_owner
        self.setup_buttons()
        self.end_time = 0

    @abstractmethod
    def display_order(self,position,color):
        pass

    @abstractmethod
    def make_order(self):
        pass

    def display_pressed_topping(self):
        if self.pressed_topping:
            text = (str(self.pressed_topping))
        else:
            text = "Choose topping"

        # topping_text = self.played_game.font.render(text, True, (255, 255, 255))
        topping_text = self.played_game.font.render(text, True, (117, 105, 104))
        topping_text_rect = topping_text.get_rect()
        topping_text_rect.topleft = (170, 30)
        self.played_game.screen.blit(topping_text, topping_text_rect)

    def display_score(self):
        text = ("Score: " + str(self.mode.score))
        # score_text = self.played_game.font.render(text, True, (255, 255, 255))
        score_text = self.played_game.font.render(text, True, (117, 105, 104))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (280, 520)
        self.played_game.screen.blit(score_text, score_text_rect)

    def display_timer(self):
        timer = round(self.mode.end_time - time.time(), 2)
        text = ("Time left: " + str(timer))
        # timer_text = self.played_game.font.render(text, True, (255, 255, 255))
        timer_text = self.played_game.font.render(text, True, (117, 105, 104))
        timer_text_rect = timer_text.get_rect()
        timer_text_rect.topleft = (170, 5)
        self.played_game.screen.blit(timer_text, timer_text_rect)

    def check_order(self):
        made = self.pizza.toppings
        required = self.required_pizza.toppings
        for i in range(len(required)):
            if i < len(made):
                if made[i].name == required[i].name and made[i].quantity == required[i].quantity:
                    self.mode.score += 100 // (self.toppings_amount + 1)

    def setup_buttons(self):
        # Toppings
        cheese_img = pygame.image.load("img/cheese2.png")
        self.cheese_button = game.Button.Button(15, 10, cheese_img, 0.15)

        mushrooms_img = pygame.image.load("img/mushroom.png")
        self.mushrooms_button = game.Button.Button(15, 80, mushrooms_img, 0.15)

        salami_img = pygame.image.load("img/salami1.png")
        self.salami_button = game.Button.Button(15, 150, salami_img, 0.15)

        pineapple_img = pygame.image.load("img/pinapple1.png")
        self.pineapple_button = game.Button.Button(100, 300, pineapple_img, 0.15)

        ham_img = pygame.image.load("img/ham1.png")
        self.ham_button = game.Button.Button(15, 300, ham_img, 0.15)

        shrimp_img = pygame.image.load("img/shripm1.png")
        self.shrimp_button = game.Button.Button(15, 370, shrimp_img, 0.15)

        anchovie_img = pygame.image.load("img/fish1.png")
        self.anchovie_button = game.Button.Button(80, 80, anchovie_img, 0.15)

        pepper_img = pygame.image.load("img/pepper1.png")
        self.pepper_button = game.Button.Button(100, 370, pepper_img, 0.15)

        black_olive_img = pygame.image.load("img/olive_black1.png")
        self.black_olive_button = game.Button.Button(100, 150, black_olive_img, 0.15)

        green_olive_img = pygame.image.load("img/olive_green1.png")
        self. green_olive_button = game.Button.Button(100, 230,  green_olive_img, 0.15)

        bacon_img = pygame.image.load("img/bacon2.png")
        self.bacon_button = game.Button.Button(5, 210, bacon_img, 0.20)


        # "+", "-"
        minus_img = pygame.image.load("buttons/minus_button.png")
        self.minus_button = game.Button.Button(240, 80, minus_img, 0.07)

        plus_img = pygame.image.load("buttons/plus_button.png")
        self.plus_button = game.Button.Button(280, 80, plus_img, 0.07)

        # Add, Back
        back_img = pygame.image.load("buttons/back_button.png")
        self.back_button = game.Button.Button(15, 500, back_img, 0.25)

        add_img = pygame.image.load("buttons/add_button.png")
        self.add_button = game.Button.Button(90, 500, add_img, 0.25)

        # Done
        done_img = pygame.image.load("buttons/done_button.png")
        self.done_button = game.Button.Button(450, 500, done_img, 0.25)


    def display_buttons(self):
        # Toppings buttons
        if self.cheese_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 10 * self.pizza.scale, self.pizza.y + 10 * self.pizza.scale,
                                  game.Topping.ToppingName(1), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()
        if self.mushrooms_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 100 * self.pizza.scale, self.pizza.y + 70 * self.pizza.scale,
                                  game.Topping.ToppingName(3), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()
        if self.salami_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 100 * self.pizza.scale, self.pizza.y + 90 * self.pizza.scale,
                                  game.Topping.ToppingName(2), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()
        if self.pineapple_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 80 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  game.Topping.ToppingName(4),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()
        if self.ham_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 100 * self.pizza.scale, self.pizza.y + 80 * self.pizza.scale,
                                  game.Topping.ToppingName(5),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()
        if self.shrimp_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 100 * self.pizza.scale, self.pizza.y + 80 * self.pizza.scale,
                                  game.Topping.ToppingName(6),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        if self.anchovie_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 160 * self.pizza.scale, self.pizza.y + 140 * self.pizza.scale,
                                  game.Topping.ToppingName(7),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        if self.pepper_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 180 * self.pizza.scale, self.pizza.y + 140 * self.pizza.scale,
                                  game.Topping.ToppingName(8), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        if self.black_olive_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x +100 * self.pizza.scale, self.pizza.y + 90 * self.pizza.scale,
                                  game.Topping.ToppingName(10), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        if self.green_olive_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 80 * self.pizza.scale, self.pizza.y + 70 * self.pizza.scale,
                                  game.Topping.ToppingName(9), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        if self.bacon_button.draw(self.played_game.screen):
            top = game.Topping.Topping(self.pizza.x + 80 * self.pizza.scale, self.pizza.y + 70 * self.pizza.scale,
                                  game.Topping.ToppingName(11), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
            self.counter.restart()

        # Counter buttons
        if self.plus_button.draw(self.played_game.screen):
            self.counter.increment()

        if self.minus_button.draw(self.played_game.screen):
            self.counter.decrement()

        if self.back_button.draw(self.played_game.screen):
            self.pizza.remove_last_topping()

        if self.add_button.draw(self.played_game.screen):
            if self.pressed_topping:
                self.pressed_topping.quantity = self.counter.value
                if self.pressed_topping.quantity > 0:
                    self.pizza.add_topping(self.pressed_topping)

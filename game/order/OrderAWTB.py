import time
import pygame
import game.Button
import game.Topping
import game.Pizza
import game.Counter
from game.order.AbstractOrder import AbstractOrder


class OrderAWTB(AbstractOrder):
    def __init__(self, pizza, toppings_amount, min_amount, max_amount, order_owner, mode, end_time, played_game):
        super().__init__(pizza, toppings_amount, min_amount, max_amount, order_owner, mode, played_game)
        self.setup_order_name_button()
        self.end_time = end_time
        self.flag = False

    def display_orders(self):
        position = 0
        n = 0
        for order in self.mode.orders:
            if order.end_time > time.time():
                order.display_order_name_button(n)
                n += 1
                if order == self:
                    color = pygame.Color(210, 46, 31)
                else:
                    color = pygame.Color(117, 105, 104)
                position = order.display_order(position, color)
            else:
                self.check_order()
                self.mode.orders.remove(order)
                self.mode.score -= 40
                self.mode.next_order()

    def display_order(self, position, color):
        font = pygame.font.Font('fonts/yellowtail/yellowtail.ttf', 30)
        text = str(self.order_owner)
        topping_text = self.played_game.font.render(text, True, (207, 62, 62))
        topping_text_rect = topping_text.get_rect()
        topping_text_rect.topleft = (550, 5 + position * 22)
        self.played_game.screen.blit(topping_text, topping_text_rect)
        position += 1
        font = pygame.font.Font('fonts/yellowtail/yellowtail.ttf', 20)
        self.display_order_timer(position)
        position += 1
        topping_counter = 0
        for topping in self.required_pizza.toppings:
            text = (str(topping) + " x " + str(topping.quantity))
            topping_text = font.render(text, True, color)
            topping_text_rect = topping_text.get_rect()
            topping_text_rect.topleft = (550, 5 + position * 22)
            self.played_game.screen.blit(topping_text, topping_text_rect)
            topping_counter += 1
            position += 1

        if topping_counter < 6:
            position += 6 - topping_counter

        position += 1
        return position

    def setup_order_name_button(self):
        make_img = pygame.image.load("buttons/button_make2.png")
        if len(self.mode.orders) > 2:
            self.boy_name_button1 = game.Button.Button(715, 150, make_img, 0.35)
            self.boy_name_button2 = game.Button.Button(715, 350, make_img, 0.35)
            self.boy_name_button3 = game.Button.Button(715, 550, make_img, 0.35)

    def display_order_name_button(self, n):
        if not self.flag:
            self.setup_order_name_button()
            self.flag = True
        if n == 0:
            if self.boy_name_button1.draw(self.played_game.screen):
                self.make_order()
        if n == 1:
            if self.boy_name_button2.draw(self.played_game.screen):
                self.make_order()
        if n == 2:
            if self.boy_name_button3.draw(self.played_game.screen):
                self.make_order()

    def display_order_timer(self, position):
        font = pygame.font.Font('fonts/yellowtail/yellowtail.ttf', 20)
        timer = round(self.end_time - time.time(), 2)
        if timer < 5:
            color = pygame.Color(210, 46, 31)
        else:
            color = pygame.Color(117, 105, 104)
        text = ("left: " + str(timer))
        timer_text = font.render(text, True, color)
        timer_text_rect = timer_text.get_rect()
        timer_text_rect.topleft = (715, 100 + position * 22)
        self.played_game.screen.blit(timer_text, timer_text_rect)
        self.played_game.screen.blit(timer_text, timer_text_rect)

    def display_timer(self):
        timer = round(self.mode.end_time - time.time(), 2)
        text = "Time left: " + (str(timer))
        timer_text = self.played_game.font.render(text, True, (117, 105, 104))
        timer_text_rect = timer_text.get_rect()
        timer_text_rect.topleft = (340, 80)
        self.played_game.screen.blit(timer_text, timer_text_rect)

    def display_order_name(self):
        text = ("Order for: " + self.order_owner)
        owner_text = self.played_game.font.render(text, True, (210, 46, 31))
        owner_text_rect = owner_text.get_rect()
        owner_text_rect.topleft = (170, 5)
        self.played_game.screen.blit(owner_text, owner_text_rect)


    def make_order(self):
        running = True
        while running:
            self.played_game.screen.fill((238, 229, 199))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if self.mode.end_time <= time.time():
                self.check_order()
                self.mode.display_final_score()

            self.pizza.draw_pizza(self.played_game.screen)
            self.display_orders()
            self.display_pressed_topping()
            self.counter.draw()
            self.display_buttons()
            self.pizza.draw_toppings(self.played_game.screen)
            self.display_score()
            self.display_timer()
            self.display_order_name()
            pygame.display.update()

    def display_buttons(self):
        super().display_buttons()
        if self.done_button.draw(self.played_game.screen):
            self.check_order()
            self.mode.orders.remove(self)
            self.mode.next_order()


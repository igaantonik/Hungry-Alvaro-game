import time

import pygame
from game.order.AbstractOrder import AbstractOrder


class OrderMA(AbstractOrder):
    def __init__(self, pizza, toppings_amount, min_amount, max_amount, order_owner, mode, played_game):
        super().__init__(pizza, toppings_amount, min_amount, max_amount, order_owner, mode, played_game)

    def display_order(self, position=0,color=1):
        # position = 0
        text = str(self.order_owner)
        topping_text = self.played_game.font.render(text, True, (207, 62, 62))
        topping_text_rect = topping_text.get_rect()
        topping_text_rect.topleft = (540, 20)
        position += 1
        self.played_game.screen.blit(topping_text, topping_text_rect)
        for topping in self.required_pizza.toppings:
            text = (str(topping) + " x " + str(topping.quantity))
            topping_text = self.played_game.font.render(text, True, (255, 255, 255))
            topping_text_rect = topping_text.get_rect()
            topping_text_rect.topleft = (540, 30 + position * 30)
            self.played_game.screen.blit(topping_text, topping_text_rect)
            position += 1

    def make_order(self):
        running = True
        while running:

            self.played_game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if self.mode.end_time <= time.time():
                self.check_order()
                self.mode.set_end_time()
                self.mode.next_order()

            self.pizza.draw_pizza(self.played_game.screen)
            self.display_order()
            self.display_pressed_topping()
            self.counter.draw()
            self.display_buttons()
            self.pizza.draw_toppings(self.played_game.screen)
            self.display_score()
            self.display_timer()
            pygame.display.update()

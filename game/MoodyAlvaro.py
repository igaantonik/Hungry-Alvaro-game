import pygame
import Pizza
import Order
import time
from enum import Enum


class MoodyAlvaro:
    def __init__(self, game, difficulty):
        pygame.init()
        self.difficulty = difficulty
        self.is_running = True
        self.game = game
        self.score = 0
        self.name = "Moody Alvaro"
        self.current_order = 0
        self.orders = []
        self.all_orders = 3
        self.play_time = 0
        self.end_time = 0

    def run(self):
        self.set_end_time()
        self.next_order()

    def set_end_time(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 30
        elif self.difficulty == 2:
            self.end_time = time.time() + 20
        else:
            self.end_time = time.time() + 10

    def next_order(self):
        if len(self.orders) == 1:
            self.orders.pop()
        if self.current_order < self.all_orders-1:
            self.current_order += 1
            order = Order.Order(Pizza.Pizza(160, 150, 0.70), 4, 2, 5, "Alvaro", self, self.game)
            self.orders.append(order)
            order.make_order()
        else:
            self.display_final_score()

    def display_final_score(self):
        running = True
        while running:
            self.game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            pygame.init()
            text = ("Your final score is: " + str(self.score))
            score_text = self.game.font.render(text, True, (255, 255, 255))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.game.screen.get_width() // 2, self.game.screen.get_height() // 2)
            self.game.screen.blit(score_text, score_text_rect)
            pygame.display.update()

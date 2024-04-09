import pygame
import Pizza
import Order
import time
from enum import Enum

class HungryAlvaro:
    def __init__(self, game, difficulty):
        pygame.init()
        self.difficulty = difficulty
        self.is_running = True
        self.game = game
        self.score = 0
        self.name = "Hungry Alvaro"
        self.current_order = -1
        self.orders = []
        self.play_time = 0
        self.end_time = 0

    def run(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 60
        elif self.difficulty == 2:
            self.end_time = time.time() + 40
        else:
            self.end_time = time.time() + 20

        self.next_order()

    def timer(self):
        start_time = time.time()
        end_time = start_time + self.play_time
        # self.next_order()
        self.current_order += 1
        order = Order.Order(Pizza.Pizza(160, 150, 0.70), 4, 2, 5, self, self.game)

        while time.time() < end_time:
            mins, secs = divmod(self.play_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            self.orders.append(order)
            order.make_order()
            time.sleep(1)

        self.display_final_score()


    def next_order(self):
        self.current_order += 1
        # if self.current_order < self.number_of_orders:
        order = Order.Order(Pizza.Pizza(160, 150, 0.70), 4, 2, 5, self, self.game)
        self.orders.append(order)
        order.make_order()
        # else:
        #     self.display_final_score()

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
            score_text_rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
            self.game.screen.blit(score_text, score_text_rect)
            pygame.display.update()





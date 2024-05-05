import json

import pygame
import Pizza
import Order
import time
from enum import Enum
import Button
import Game
from ScoreManager import ScoreManager

from game.OrderAWTB import OrderAWTB


class AlvaroWithTheBoys():
    def __init__(self, game, difficulty):
        pygame.init()
        self.difficulty = difficulty
        self.is_running = True
        self.game = game
        self.score = 0
        self.name = "AlvaroWithTheBoys"
        self.current_order = -1
        self.orders = []
        self.all_orders = 3
        self.start_nr_orders = 3
        self.play_time = 0
        self.end_time = 0
        self.order_end_time = 0
        self.setup_final_buttons()
        with open("results.json", "r") as json_file:
            self.results = json.load(json_file)

    def run(self):
        self.set_end_time()
        self.init_orders()

    def set_end_time(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 60
            self.order_end_time = 30
        elif self.difficulty == 2:
            self.end_time = time.time() + 60
            self.order_end_time = 20
        else:
            self.end_time = time.time() + 1
            self.order_end_time = 10

    def init_orders(self):
        for i in range(self.start_nr_orders):
            self.current_order += 1
            order = OrderAWTB(Pizza.Pizza(160, 150, 0.70), 4, 2, 5,"Alvaro" + str(i),self, time.time() + (i+1)*self.order_end_time, self.game)
            self.orders.append(order)
        # for i in range(3):
        #     self.current_order += 1
        #     order = OrderAWTB(Pizza.Pizza(160, 150, 0.70), 4, 2, 5,"Alvaro" + str(i),self, time.time() + (i+1)*self.order_end_time, self.game)
        #     self.orders.append(order)

        self.orders[0].make_order()


    def next_order(self):
        self.all_orders += 1
        self.current_order += 1
        order = OrderAWTB(Pizza.Pizza(160, 150, 0.70), 4, 2, 5, "Alvaro" + str(self.all_orders - 1), self, time.time() + self.order_end_time*1.5,self.game)
        self.orders.append(order)
        order.make_order()


    def display_final_score(self):
        self.results[self.name][str(self.difficulty)].append(self.score)
        ScoreManager.save_score(self.results)

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
            self.display_final_buttons()

            if self.exit_button.draw(self.game.screen):
                running = False
                pygame.quit()

            pygame.display.update()


    def setup_final_buttons(self):
        restart_img = pygame.image.load("buttons_img/button_restart.png")
        self.restart_button = Button.Button(500, 360, restart_img, 1)

        exit_button_img = pygame.image.load("buttons_img/button_exit.png")
        self.exit_button = Button.Button(500, 415, exit_button_img, 1)


    def display_final_buttons(self):
        if self.restart_button.draw(self.game.screen):
            pygame.quit()
            game = Game.Game()
            game.main_menu()


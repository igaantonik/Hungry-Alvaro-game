import json
from abc import ABC, abstractmethod
import random

import pygame
import game.Button
import game.Game
from game.ScoreManager import ScoreManager


class AbstractMode(ABC):
    def __init__(self, game, difficulty, name):
        pygame.init()
        self.difficulty = difficulty
        self.is_running = True
        self.game = game
        self.score = 0
        self.name = name
        self.current_order = 0
        self.orders = []
        self.end_time = 0
        self.setup_final_buttons()
        with open("results.json", "r") as json_file:
            self.results = json.load(json_file)

    def run(self):
        self.set_end_time()
        self.next_order()

    @abstractmethod
    def set_end_time(self):
        pass

    @abstractmethod
    def next_order(self):
        pass

    def display_final_score(self):
        self.results[self.name][str(self.difficulty)].append(self.score)
        ScoreManager.save_score(self.results)

        running = True
        while running:
            # self.game.screen.fill((242, 177, 202))
            self.game.screen.fill((238, 229, 199))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            pygame.init()
            text = ("Your final score is: " + str(self.score))
            # score_text = self.game.font.render(text, True, (255, 255, 255))
            font = pygame.font.Font('fonts/genty/genty.ttf', 50)
            score_text = font.render(text, True, (117, 105, 104))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.game.screen.get_width() // 2, self.game.screen.get_height() // 2 - 50)
            self.game.screen.blit(score_text, score_text_rect)
            self.display_final_buttons()

            if self.exit_button.draw(self.game.screen):
                running = False
                pygame.quit()

            pygame.display.update()

    def setup_final_buttons(self):
        restart_img = pygame.image.load("buttons/button_restart2.png")
        self.restart_button = game.Button.Button(280, 360, restart_img, 1)

        exit_button_img = pygame.image.load("buttons/button_exit2.png")
        self.exit_button = game.Button.Button(280, 415, exit_button_img, 1)

    def display_final_buttons(self):
        if self.restart_button.draw(self.game.screen):
            pygame.quit()
            new_game = game.Game.Game()
            new_game.main_menu()

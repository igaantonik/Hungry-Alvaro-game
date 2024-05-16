import json
from enum import Enum

import pygame

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class ScoreManager:

    @staticmethod
    def save_score(score):
        with open("results.json", "w") as json_file:
            json.dump(score, json_file)

    @staticmethod
    def load_results(self):
        with open("results.json", "r") as json_file:
            self.results = json.load(json_file)


    @staticmethod
    def display_results(self):
        running = True
        while running:
            # self.screen.fill((242, 177, 202))
            self.screen.fill((238,229, 199))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            score_text = pygame.font.Font('fonts/genty/genty.ttf', 60).render("Your latest results!", True, (29, 91, 76))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.screen.get_width() // 2, 40)
            self.screen.blit(score_text, score_text_rect)

            y_offset = 70
            for game_mode, mode_results in self.results.items():
                mode_text = pygame.font.Font('fonts/genty/genty.ttf', 50).render(f"{game_mode}:", True, (207, 62, 62))
                self.screen.blit(mode_text, (50, y_offset))
                best_text = pygame.font.Font('fonts/genty/genty.ttf', 25).render("High score:", True, (207, 62, 62))
                self.screen.blit(best_text, (600, y_offset+20))
                y_offset += 60
                for difficulty, scores in mode_results.items():
                    recent_scores = scores[::-1][:5]
                    recent_scores_text = ', '.join(map(str, recent_scores))
                    recent_text = self.font.render(f"{Difficulty(int(difficulty)).name}: {recent_scores_text}", True, (117, 105, 104))
                    self.screen.blit(recent_text, (70, y_offset))

                    best_score = max(scores, default=0)
                    best_score_value = self.font.render(f"{best_score}", True, (117, 105, 104))
                    self.screen.blit(best_score_value, (650, y_offset))
                    y_offset += 30
                y_offset += 30

            pygame.display.update()










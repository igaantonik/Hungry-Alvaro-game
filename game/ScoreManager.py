import json

import pygame


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
            self.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            y_offset = 50
            for game_mode, mode_results in self.results.items():
                mode_text = self.font.render(f"{game_mode}:", True, (255, 255, 255))
                self.screen.blit(mode_text, (50, y_offset))
                y_offset += 30
                for difficulty, scores in mode_results.items():
                    # Sortowanie wyników od najwyższego do najniższego
                    # Wyświetlenie 5 najnowszych wyników
                    recent_scores = scores[::-1][:5]
                    recent_scores_text = ', '.join(map(str, recent_scores))
                    recent_text = self.font.render(f"Difficulty {difficulty}: {recent_scores_text}", True, (255, 255, 255))
                    self.screen.blit(recent_text, (70, y_offset))
                    y_offset += 30

                    # Wyświetlenie najlepszego wyniku
                    best_score = max(scores, default=0)
                    best_text = self.font.render(f"Best Score: {best_score}", True, (255, 255, 255))
                    self.screen.blit(best_text, (70, y_offset))
                    y_offset += 30
                y_offset += 30

            pygame.display.update()










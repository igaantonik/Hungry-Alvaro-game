import json

import pygame
from pygame import mixer

import Button
from game.modes import AlvaroWithTheBoys, HungryAlvaro, MoodyAlvaro
from ScoreManager import ScoreManager

BUTTON_IMAGES = {
    "hungry_alvaro": "buttons/buttonHA.png",
    "moody_alvaro": "buttons/buttonMA2.png",
    "alvaro_with_the_boys": "buttons/buttonAWTB.png",
    "exit": "buttons/button_exit2.png",
    "easy": "buttons/button_easy2.png",
    "medium": "buttons/button_medium2.png",
    "hard": "buttons/button_hard2.png",
    "results": "buttons/button_results2.png"
}
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pizza Game")
        icon = pygame.image.load("img/pizzaicon.png")
        pygame.display.set_icon(icon)
        self.font = pygame.font.Font('fonts/yellowtail/yellowtail.ttf', 30)
        self.setup_buttons()
        self.setup_text()
        with open("results.json", "r") as json_file:
            self.results = json.load(json_file)

    def main_menu(self):
        mixer.init()
        mixer.music.load("music/italian_music.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play(loops=-1)

        running = True
        while running:

            self.screen.fill((239, 233, 208))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.hungry_alvaro_button.draw(self.screen):
                self.choose_difficulty(1)
            if self.moody_alvaro_button.draw(self.screen):
                self.choose_difficulty(2)
            if self.alvaro_with_the_boys_button.draw(self.screen):
                self.choose_difficulty(3)

            if self.results_button.draw(self.screen):
                ScoreManager.display_results(self)

            if self.exit_button.draw(self.screen):
                running = False

            self.screen.blit(self.intro_text_2,self.intro_text_2_rect)
            self.screen.blit(self.intro_text, self.intro_text_rect)
            self.draw_pizza_image()
            pygame.display.update()

    def choose_difficulty(self, mode):
        running = True
        while running:

            self.screen.fill((239, 233, 208))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if self.easy_button.draw(self.screen):
                self.play(mode, 1)
            if self.medium_button.draw(self.screen):
                self.play(mode, 2)
            if self.hard_button.draw(self.screen):
                self.play(mode, 3)

            self.screen.blit(self.difficulty_text, self.difficulty_text_rect)
            self.draw_alvaro()
            pygame.display.update()

    def play(self, mode, difficulty):
        if mode == 1:
            chosen_mode = HungryAlvaro.HungryAlvaro(self, difficulty, 'Hungry Alvaro')
        elif mode == 2:
            chosen_mode = MoodyAlvaro.MoodyAlvaro(self, difficulty,'Moody Alvaro')
        else:
            chosen_mode = AlvaroWithTheBoys.AlvaroWithTheBoys(self, difficulty, 'Alvaro With The Boys')
        chosen_mode.run()

    def draw_alvaro(self):
        self.alvaroImg = pygame.image.load("img/alvaro.png")
        self.ciaoImg = pygame.image.load("img/ciao.png")
        self.screen.blit(self.alvaroImg, (100, 450))
        self.screen.blit(self.ciaoImg, (150, 300))

    def draw_pizza_image(self):
        self.pizza_image = pygame.image.load("img/pizza_start.png")
        self.screen.blit(self.pizza_image, (120, 280))

    def setup_buttons(self):
        button_data = [
            ("hungry_alvaro", 500, 270),
            ("moody_alvaro", 500, 325),
            ("alvaro_with_the_boys", 500, 380),
            ("exit", 500, 490),
            ("easy", 500, 250),
            ("medium", 500, 305),
            ("hard", 500, 360),
            ("results", 500, 435)
        ]
        for name, x, y in button_data:
            img = pygame.image.load(BUTTON_IMAGES[name])
            setattr(self, f"{name}_button", Button.Button(x, y, img, 1))

    def setup_text(self):
        self.intro_text_2 = pygame.font.Font('fonts/genty/genty.ttf', 60).render("Bake pizza for Alvaro!", True, (29, 91, 76))
        self.intro_text_2_rect = self.intro_text_2.get_rect()
        self.intro_text_2_rect.topleft = (60, 80)

        self.intro_text = pygame.font.Font('fonts/genty/genty.ttf', 50).render("Choose your mode", True, (29, 91, 76))
        self.intro_text_rect = self.intro_text.get_rect()
        self.intro_text_rect.topleft = (60, 180)

        self.difficulty_text = pygame.font.Font('fonts/genty/genty.ttf', 50).render("Choose your difficulty", True, (29, 91, 76))
        self.difficulty_text_rect = self.difficulty_text.get_rect()
        self.difficulty_text_rect.topleft = (60, 150)
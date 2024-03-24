import pygame
import button
import pizza
from enum import Enum

class Mode(Enum):
    MODE1 = 1
    MODE2 = 2
    MODE3 = 3
class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title, Icon, Font
pygame.display.set_caption("Pizza Game")
icon = pygame.image.load("img/pizzaicon.png")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("", 40)

# Buttons colors #e24f4f, #d64e95

# Hungry Alvaro button
hungry_alvaro_button_img = pygame.image.load("buttons/button_hungry-alvaro.png")
hungry_alvaro_button = button.Button(500, 250, hungry_alvaro_button_img, 1)

# Moody Alvaro button
moody_alvaro_button_img = pygame.image.load("buttons/button_moody-alvaro.png")
moody_alvaro_button = button.Button(500, 305, moody_alvaro_button_img, 1)

# Alvaro with the boys button
alvaro_with_the_boys_button_img = pygame.image.load("buttons/button_alvaro-with-the-boys.png")
alvaro_with_the_boys_button = button.Button(500, 360, alvaro_with_the_boys_button_img, 1)

# Exit button
exit_button_img = pygame.image.load("buttons/button_exit.png")
exit_button = button.Button(500, 415, exit_button_img, 1)

#Easy button
easy_button_img = pygame.image.load("buttons/button_easy.png")
easy_button = button.Button(500, 250, easy_button_img, 1)

#Medium button
medium_button_img = pygame.image.load("buttons/button_medium.png")
medium_button = button.Button(500, 305, medium_button_img, 1)

#Hard button
hard_button_img = pygame.image.load("buttons/button_hard.png")
hard_button = button.Button(500, 360, hard_button_img, 1)

# Intro
intro_text = font.render("Choose your mode", True, (255, 255, 255))
intro_text_rect = intro_text.get_rect()
intro_text_rect.center = (200, 150)

# Difficulty
difficulty_text = font.render("Choose your difficulty", True, (255, 255, 255))
difficulty_text_rect = difficulty_text.get_rect()
difficulty_text_rect.center = (200, 150)

# Alvaro
alvaroImg = pygame.image.load("img/alvaro.png")
ciaoImg = pygame.image.load("img/ciao.png")
def alvaro():
    screen.blit(alvaroImg, (100, 450))
    screen.blit(ciaoImg, (150, 300))

def chooseDifficulty(mode):
    running = True
    while running:

        screen.fill((242, 177, 202))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        if easy_button.draw(screen):
            play(mode, 1)
        if medium_button.draw(screen):
            play(mode, 2)
        if hard_button.draw(screen):
            play(mode, 3)

        screen.blit(difficulty_text, difficulty_text_rect)
        alvaro()
        pygame.display.update()

def play(mode, difficulty):
    running = True
    while running:

        screen.fill((242, 177, 202))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        text = "You chose mode: " + Mode(mode).name + " and difficulty: " + Difficulty(difficulty).name
        choosen_text = font.render(text, True, (255, 255, 255))
        choosen_text_rect = choosen_text.get_rect()
        choosen_text_rect.center = (screen.get_width()//2, 150)
        screen.blit(choosen_text, choosen_text_rect)
        alvaro()
        pygame.display.update()

def main_menu():
    running = True
    while running:

        screen.fill((242, 177, 202))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing buttons and checking if they are clicked
        if hungry_alvaro_button.draw(screen):
            pygame.mouse.set_pos(screen.get_width()//2, screen.get_height()//2)
            chooseDifficulty(1)
        if moody_alvaro_button.draw(screen):
            pygame.mouse.set_pos(screen.get_width() // 2, screen.get_height() // 2)
            chooseDifficulty(2)
        if alvaro_with_the_boys_button.draw(screen):
            pygame.mouse.set_pos(screen.get_width() // 2, screen.get_height() // 2)
            chooseDifficulty(3)

        if exit_button.draw(screen):
            running = False

        screen.blit(intro_text, intro_text_rect)
        alvaro()
        pygame.display.update()

main_menu()

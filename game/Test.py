import pygame
import Pizza

# widok testowy z wygenerowaną pizza

pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))

pizza1 = Pizza.Pizza(50, 50,1)
pizza1.generate_pizza(4, 2, 7)
font = pygame.font.SysFont("Times New Roman", 40)

text = "BUILD THIS PIZZA"
choosen_text = font.render(text, True, (255, 255, 255))
choosen_text_rect = choosen_text.get_rect()
choosen_text_rect.center = (screen.get_width() // 2, 30)
while running:

    screen.fill((242, 177, 202))
    screen.blit(choosen_text, choosen_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pizza1.draw_pizza(screen)
    pizza1.draw_toppings(screen)
    alvaroImg = pygame.image.load("img/alvaro.png")
    screen.blit(alvaroImg, (50, 450))
    pygame.display.update()

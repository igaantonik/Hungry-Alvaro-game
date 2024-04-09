import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = True

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # Check mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True


        # Draw a button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

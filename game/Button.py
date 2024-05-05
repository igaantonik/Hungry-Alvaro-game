import pygame


class Button:

    def __init__(self, *args):
        self.args_no = len(args)
        if len(args) == 4:
            x = args[0]
            y = args[1]
            image = args[2]
            scale = args[3]
            width, height = image.get_size()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = True

        if len(args) == 3:
            self.font = pygame.font.SysFont("", 30)
            x = args[0]
            y = args[1]
            text = args[2]
            self.button_text = self.font.render(text, True, (255, 255, 255))
            self.rect = self.button_text.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = True


    def draw(self, surface):
        if self.args_no == 4:
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

        if self.args_no == 3:
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
            surface.blit(self.button_text, (self.rect.x, self.rect.y))

            return action

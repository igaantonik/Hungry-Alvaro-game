class Counter:
    def __init__(self, x, y, game):
        self.game = game
        self.value = 1
        self.x = x
        self.y = y

    def restart(self):
        self.value = 1

    def increment(self):
        if self.value < 10:
            self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

    def draw(self):
        counter_text = self.game.font.render(str(self.value), True, (117, 105, 104))
        self.game.screen.blit(counter_text, (self.x, self.y))

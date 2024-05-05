import random

import game.Pizza
import time
import game.Button
import game.Game
from game.modes.AbstractMode import AbstractMode
from game.order.OrderHA import OrderHA


class HungryAlvaro(AbstractMode):
    def __init__(self, game, difficulty, name):
        super().__init__(game, difficulty, name)

    def set_end_time(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 60
        elif self.difficulty == 2:
            self.end_time = time.time() + 40
        else:
            self.end_time = time.time() + 20
        self.next_order()

    def next_order(self):
        self.current_order += 1
        order = game.order.OrderHA.OrderHA(game.Pizza.Pizza(160, 150, 0.70), random.randint(2,5), 2, 5, "Alvaro", self, self.game)
        self.orders.append(order)
        order.make_order()
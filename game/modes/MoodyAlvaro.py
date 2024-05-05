import random

import game.Pizza
import time
import game.Button
import game.Game
from game.order.OrderMA import OrderMA

from game.modes.AbstractMode import AbstractMode


class MoodyAlvaro(AbstractMode):
    def __init__(self, game, difficulty, name):
        super().__init__(game, difficulty, name)
        self.all_orders = 3
        self.play_time = 0

    def set_end_time(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 30
        elif self.difficulty == 2:
            self.end_time = time.time() + 20
        else:
            self.end_time = time.time() + 10

    def next_order(self):
        if self.current_order < self.all_orders:
            self.current_order += 1
            order = game.order.OrderMA.OrderMA(game.Pizza.Pizza(160, 150, 0.70),random.randint(2, 5) , 2, 5, "Alvaro", self, self.game)
            self.orders.append(order)
            order.make_order()
        else:
            self.display_final_score()

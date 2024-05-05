import random

import game.Pizza
import time
import game.Button
import game.Game
import game.order.OrderAWTB
from game.modes.AbstractMode import AbstractMode


class AlvaroWithTheBoys(AbstractMode):
    def __init__(self, game, difficulty, name):
        super().__init__(game, difficulty, name)
        self.start_nr_orders = 3
        self.order_end_time = 0

    def run(self):
        self.set_end_time()
        self.init_orders()

    def set_end_time(self):
        if self.difficulty == 1:
            self.end_time = time.time() + 60
            self.order_end_time = 30
        elif self.difficulty == 2:
            self.end_time = time.time() + 60
            self.order_end_time = 15
        else:
            self.end_time = time.time() + 60
            self.order_end_time = 10

    def init_orders(self):
        for i in range(self.start_nr_orders):
            self.current_order += 1
            name = self.generate_name()
            if i == 0:
                name = "Alvaro"
            order = game.order.OrderAWTB.OrderAWTB(game.Pizza.Pizza(160, 150, 0.70), random.randint(2, 5), 2, 5, name, self,
                              time.time() + (i + 1) * self.order_end_time, self.game)
            self.orders.append(order)

        self.orders[0].make_order()

    def generate_name(self):
        names = [
            "James", "John", "Robert", "Michael", "William",
            "David", "Richard", "Joseph", "Thomas", "Charles",
            "Christopher", "Daniel", "Matthew", "Anthony", "Mark"
        ]
        return random.choice(names)

    def next_order(self):
        self.current_order += 1
        order = game.order.OrderAWTB.OrderAWTB(game.Pizza.Pizza(160, 150, 0.70), random.randint(2, 5), 2, 5, self.generate_name(), self,
                          time.time() + self.order_end_time * 1.5, self.game)

        self.orders.append(order)
        order.make_order()

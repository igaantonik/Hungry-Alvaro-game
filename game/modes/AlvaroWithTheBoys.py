import game.Pizza
import time
import game.Button
import game.Game
from game.order.OrderAWTB import OrderAWTB
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
            self.end_time = time.time() + 40
            self.order_end_time =15
        else:
            self.end_time = time.time() + 30
            self.order_end_time = 10

    def init_orders(self):
        for i in range(self.start_nr_orders):
            self.current_order += 1
            order = OrderAWTB(game.Pizza.Pizza(160, 150, 0.70), 4, 2, 5, "Alvaro" + str(self.current_order), self,
                              time.time() + (i + 1) * self.order_end_time, self.game)
            self.orders.append(order)

        self.orders[0].make_order()

    def next_order(self):
        self.current_order += 1
        order = OrderAWTB(game.Pizza.Pizza(160, 150, 0.70), 4, 2, 5, "Alvaro" + str(self.current_order), self,
                          time.time() + self.order_end_time * 1.5, self.game)
        self.orders.append(order)
        order.make_order()

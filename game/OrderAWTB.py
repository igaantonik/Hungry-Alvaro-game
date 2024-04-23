import time

import pygame
import Button
import Topping
import Pizza
import Counter


class OrderAWTB:
    def __init__(self, pizza, toppings_amount, min_amount, max_amount, order_owner, mode, end_time, game):
        self.pizza = pizza
        self.game = game
        self.mode = mode
        self.toppings_amount = toppings_amount
        self.required_pizza = Pizza.Pizza(pizza.x, pizza.y, pizza.scale)
        self.required_pizza.generate_pizza(toppings_amount, min_amount, max_amount)
        self.counter = Counter.Counter(170, 80, game)
        self.pressed_topping = None
        self.order_owner = order_owner
        self.note_button = None
        self.setup_buttons()
        self.end_time = end_time

    def display_orders(self):
        position = 0
        n = 0
        for order in self.mode.orders:
            if order.end_time > time.time():
                order.display_order_name_button(position)
                position += 1
                n += 1
                position = order.display_order(position)
            else:
                self.mode.orders.remove(order)
                self.mode.score -= 40
                self.mode.next_order()

    def display_order(self, position):
        font = pygame.font.SysFont("", 25)
        self.display_order_timer(position)
        position += 1

        for topping in self.required_pizza.toppings:
            text = (str(topping) + " x " + str(topping.quantity))
            topping_text = font.render(text, True, (255, 255, 255))
            topping_text_rect = topping_text.get_rect()
            topping_text_rect.topleft = (580, 5 + position * 22)
            self.game.screen.blit(topping_text, topping_text_rect)
            position += 1
        position += 1
        return position

    def display_order_name_button(self,position):
        self.boy_name_button = Button.Button(580, 5 + position * 22, self.order_owner)
        if self.boy_name_button.draw(self.game.screen):
            print("clicked1")
            self.make_order()

    # def setup_order_name_button(self, position):
    #     self.boy_name_button = Button.Button(580, 5 + position * 30,  self.order_owner)


    def display_order_timer(self,position):
        font = pygame.font.SysFont("", 25)
        timer = round(self.end_time - time.time(), 2)
        text = ("Time left: " + str(timer))
        timer_text = font.render(text, True, (255, 255, 255))
        timer_text_rect = timer_text.get_rect()
        timer_text_rect.topleft = (580, 5 + position * 22)
        self.game.screen.blit(timer_text, timer_text_rect)

    def display_pressed_topping(self):
        if self.pressed_topping:
            text = (str(self.pressed_topping))
        else:
            text = "Choose topping"

        topping_text = self.game.font.render(text, True, (255, 255, 255))
        topping_text_rect = topping_text.get_rect()
        topping_text_rect.topleft = (170, 30)
        self.game.screen.blit(topping_text, topping_text_rect)

    def display_score(self):
        text = ("Score: " + str(self.mode.score))
        score_text = self.game.font.render(text, True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (280, 520)
        self.game.screen.blit(score_text, score_text_rect)

    # def display_timer(self):
    #     timer = round(self.mode.end_time - time.time(), 2)
    #     text = ("Time left: " + str(timer))
    #     timer_text = self.game.font.render(text, True, (255, 255, 255))
    #     timer_text_rect = timer_text.get_rect()
    #     timer_text_rect.topleft = (170, 5)
    #     self.game.screen.blit(timer_text, timer_text_rect)

    def display_order_name(self):
        text = ("Order for: " + self.order_owner)
        owner_text = self.game.font.render(text, True, (255, 255, 255))
        owner_text_rect = owner_text.get_rect()
        owner_text_rect.topleft = (170, 5)
        self.game.screen.blit(owner_text, owner_text_rect)

    def check_order(self):
        made = self.pizza.toppings
        required = self.required_pizza.toppings

        for i in range(len(required)):
            if i < len(made):
                if made[i].name == required[i].name and made[i].quantity == required[i].quantity:
                    self.mode.score += 100 // (self.toppings_amount + 1)

    def make_order(self):
        running = True
        while running:

            self.game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if self.mode.end_time <= time.time():
                self.check_order()
                if self.mode.name == "AlvaroWithTheBoys":
                    self.mode.display_final_score()

            # if self.end_time <= time.time():
            #     # self.check_order()
            #     self.mode.score -= 40
            #     self.mode.orders.remove(self)
            #     self.mode.next_order()

            self.pizza.draw_pizza(self.game.screen)
            self.display_orders()
            self.display_pressed_topping()
            self.counter.draw()
            self.display_buttons()
            self.pizza.draw_toppings(self.game.screen)
            self.display_score()
            # self.display_timer()
            self.display_order_name()
            pygame.display.update()

    def setup_buttons(self):
        # Toppings
        cheese_img = pygame.image.load("img/cheese.png")
        self.cheese_button = Button.Button(15, 10, cheese_img, 0.15)

        mushrooms_img = pygame.image.load("img/mushroom.png")
        self.mushrooms_button = Button.Button(15, 80, mushrooms_img, 0.15)

        salami_img = pygame.image.load("img/salami1.png")
        self.salami_button = Button.Button(15, 150, salami_img, 0.15)

        pineapple_img = pygame.image.load("img/pinapple1.png")
        self.pineapple_button = Button.Button(15, 230, pineapple_img, 0.15)

        ham_img = pygame.image.load("img/ham1.png")
        self.ham_button = Button.Button(15, 300, ham_img, 0.15)

        shrimp_img = pygame.image.load("img/shripm1.png")
        self.shrimp_button = Button.Button(15, 370, shrimp_img, 0.15)

        anchovie_img = pygame.image.load("img/fish1.png")
        self.anchovie_button = Button.Button(15, 440, anchovie_img, 0.15)

        # "+", "-"
        minus_img = pygame.image.load("buttons_img/minus_button.png")
        self.minus_button = Button.Button(240, 80, minus_img, 0.07)

        plus_img = pygame.image.load("buttons_img/plus_button.png")
        self.plus_button = Button.Button(280, 80, plus_img, 0.07)

        # Add, Back
        back_img = pygame.image.load("buttons_img/back_button.png")
        self.back_button = Button.Button(15, 500, back_img, 0.25)

        add_img = pygame.image.load("buttons_img/add_button.png")
        self.add_button = Button.Button(90, 500, add_img, 0.25)

        # Done
        done_img = pygame.image.load("buttons_img/done_button.png")
        self.done_button = Button.Button(450, 500, done_img, 0.25)

        note_img = pygame.image.load("buttons_img/note_button.png")
        self.note_button = Button.Button(540, 35, note_img, 1.25)

    def display_buttons(self):
        # Toppings buttons
        if self.cheese_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 10 * self.pizza.scale, self.pizza.y + 10 * self.pizza.scale,
                                  Topping.ToppingName(1), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.mushrooms_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(3), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.salami_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(2), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.pineapple_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(4),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.ham_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(5),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.shrimp_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(6),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top

        if self.anchovie_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(7),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top

        # Counter buttons
        if self.plus_button.draw(self.game.screen):
            self.counter.increment()

        if self.minus_button.draw(self.game.screen):
            self.counter.decrement()

        if self.back_button.draw(self.game.screen):
            self.pizza.remove_last_topping()

        if self.add_button.draw(self.game.screen):
            self.pressed_topping.quantity = self.counter.value
            if self.pressed_topping.quantity > 0:
                self.pizza.add_topping(self.pressed_topping)

        if self.done_button.draw(self.game.screen):
            self.check_order()
            self.mode.orders.remove(self)
            self.mode.next_order()
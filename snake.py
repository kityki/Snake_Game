import pygame
from constants import *
import random


class Cube:

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))


class Apple(Cube):
    def __init__(self, color):
        self.change_position()
        super().__init__(self.position, color)

    def change_position(self):
        random_width = random.randint(0, COLUMS_NUM) * BLOCK_SIZE
        random_height = random.randint(0, ROWS_NUM) * BLOCK_SIZE
        self.position = [random_width, random_height]


class Snake(Cube):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.body = [self.position]
        self.direction_x_y = [0, 0]
        self.counter = 0
        self.head = self.body[0]

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction_x_y = LEFT_DIR

        if keys[pygame.K_RIGHT]:
            self.direction_x_y = RIGHT_DIR

        if keys[pygame.K_UP]:
            self.direction_x_y = UP_DIR

        if keys[pygame.K_DOWN]:
            self.direction_x_y = DOWN_DIR

        self.position[0] += self.direction_x_y[0] * BLOCK_SIZE
        self.position[1] += self.direction_x_y[1] * BLOCK_SIZE

        self.body.insert(0, self.position)
        del self.body[-1]
        self.counter += 1
        if self.counter == 10:
            print(self.body)
            self.counter = 0
        self.head = self.body[0]

    def draw(self, window):
        for cube in self.body:
            self.position = cube
            super().draw(window)

    def add_body(self):

        tail = self.body[-1]
        self.body.append([tail[0] - self.direction_x_y[0] * BLOCK_SIZE, tail[1] - self.direction_x_y[1] * BLOCK_SIZE])

    def is_collision(self):
        """"this function returns True if snake meets the wall, and returns False otherwise"""
        if self.head[0] >= WIDTH or self.head[0] < 0 or self.head[1] >= HEIGHT or self.head[1] < 0:
            return True
        else:
            return False

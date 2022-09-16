import pygame
from constants import *
import random


class Cube():

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
        self.body = [position]
        self.direction_x_y = [0, 0]

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.position[0] -= BLOCK_SIZE
            self.direction_x_y[0] = -1

        if keys[pygame.K_RIGHT]:
            self.position[0] += BLOCK_SIZE
            self.direction_x_y[0] = 1

        if keys[pygame.K_UP]:
            self.position[1] -= BLOCK_SIZE
            self.direction_x_y[1] = -1

        if keys[pygame.K_DOWN]:
            self.position[1] += BLOCK_SIZE
            self.direction_x_y[1] = 1



    def draw(self, window):
        for cube in self.body:
            self.position = cube
            super().draw(window)
            print(cube)

    def add_body(self):

        tail = self.body[-1]
        self.body.append([tail[0] - self.direction_x_y[0] * BLOCK_SIZE, tail[1] - self.direction_x_y[1] * BLOCK_SIZE])




# modify func add_body
# for that we should add a new variable to the func move like direction x and y








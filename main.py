import pygame

from constants import *
import sys
from snake import Apple, Snake
import pygame.freetype


def drawGrid(screen):
    BLOCK_SIZE = 20 #Set the size of the grid block
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)


def draw_text(text):
    font = pygame.font.SysFont("arial", size=10)
    text_surface = font.render(text, True, BLUE, RED)
    return text_surface


def main():
    # Initializing Pygame
    pygame.init()
    # Initializing surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    clock = pygame.time.Clock()

    drawGrid(screen)
    pygame.font.init()
    surface = draw_text("Score: 0")

    snake_instance = Snake([WIDTH_CENTER, HEIGHT_CENTER], RED)
    snake_instance.draw(screen)

    apple_instance = Apple(GREEN)
    apple_instance.draw(screen)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if apple_instance.position == snake_instance.body[0]:
            apple_instance.change_position()
            snake_instance.add_body()

        if snake_instance.is_collision():
            pygame.quit()
            sys.exit()

        if snake_instance.is_body_collision():
            pygame.quit()
            sys.exit()

        # Drawing Rectangle
        #pygame.draw.rect(screen, RED, pygame.Rect(WIDTH_CENTER, HEIGHT_CENTER, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()
        screen.fill(BLACK)
        drawGrid(screen)
        surface = draw_text("Score: 0")
        screen.blit(surface, (100, 80))
        snake_instance.draw(screen)
        apple_instance.draw(screen)
        snake_instance.move()
        pygame.display.update()
        clock.tick(6)







main()





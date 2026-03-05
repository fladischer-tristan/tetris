"""
Provides central game functions
"""
import pygame

from Tetris import __all__


def run():
    pygame.init()

    screen = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("Tetris")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_gamewindow(screen)
        pygame.display.flip()            
    pygame.quit()
    pass

def draw_gamewindow(screen):
    pygame.draw.rect(screen, (255, 255, 255), 
                 [50, 50, 300, 400], 2)
    pass

def draw_block(screen, block):
    pass
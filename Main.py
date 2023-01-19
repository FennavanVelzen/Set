# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:50:46 2023

@author: Fenna
"""

import pygame

WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Set")
WHITE = (255, 255, 255)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(WHITE)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

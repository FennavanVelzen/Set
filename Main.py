# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:50:46 2023

@author: Fenna
"""

import pygame
pygame.init()

WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Set")
FPS = 60

#Kleuren RGB
WHITE = (255, 255, 255)
LILA = 	(220,175,255)
BLACK = (0,0,0)

"""Functie om alle combinatie mogelijkheden voor kaarten te genereren.
Deze functie neemt steeds een eigenschap uit een lijst en voegt hier alle 
overige mogelijkheden van combinaties van andere lijsten aan toe."""

def Kaarten():
    Kleuren = ['Rood', 'Groen', 'Paars'] #lijsten met eigenschap mogelijkheden van de kaarten
    Vormen = ['Ruit', 'Ovaal', 'Golf']
    Hoeveelheid = [1, 2, 3]
    Vulling = ['leeg', 'Gestreept' , 'Vol']
    Kaarten = []                        #lijst om alle kaart combinaties in toe te voegen
    for kleur in Kleuren:
        for vorm in Vormen:
            for aantal in Hoeveelheid:
                for inhoud in Vulling:
                    Kaart = [kleur, vorm, aantal, inhoud]
                    Kaarten.append(Kaart)
        
    return Kaarten
"""Een functie die text print in het scherm"""
def text(Text):
    font = pygame.font.SysFont("Times New Roman", 40, True, False)
    service = font.render( Text , True, (BLACK))
    WIN.blit(service, (200, 200))

"""Main funcitie die alle functies los oproept"""
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(LILA)
        text("Set")
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
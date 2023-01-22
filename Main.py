# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:50:46 2023

@author: Fenna
"""

import pygame
import random
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

"""Fuctie voor het schudden van de lijst met kaarten, deze functie gaat twee keer door
dezelfde for loop zodat de hoeveelheid kaarten beter geschud is"""
def Schudden(Kaarten):
    for positie in range(len(Kaarten)):
        WillekeurigGetal = random.randint(0,(len(Kaarten)-1))
        Kaarten[positie], Kaarten[WillekeurigGetal] = Kaarten[WillekeurigGetal], Kaarten[positie]
    for positie in range(len(Kaarten)):
        WillekeurigGetal = random.randint(0,(len(Kaarten)-1))
        Kaarten[positie], Kaarten[WillekeurigGetal] = Kaarten[WillekeurigGetal], Kaarten[positie]
    return Kaarten
    

"""Een functie die text print in het scherm"""
def text(Text):
    font = pygame.font.SysFont("Times New Roman", 50, True, False)
    service = font.render( Text , True, (BLACK))
    WIN.blit(service, (0, 0))


"""Functies voor het maken van de 3 figuren, vol en leeg"""
GOLF = [(300, 300), (250, 250), (200, 300), (150, 250)] #hoekputen
RUIT = [(400, 360), (350, 400), (400, 440), (450, 400)] #hoekputen
OVAAL = (40, 50, 130, 50)                               #hoekputen

def GolfVOL():
    pygame.draw.polygon(WIN, BLACK , GOLF)

def GolfLEEG():
    pygame.draw.polygon(WIN, BLACK , GOLF ,3)
    
def RuitVOL():
    pygame.draw.polygon(WIN, BLACK , RUIT)

def RuitLEEG():
    pygame.draw.polygon(WIN, BLACK , RUIT,3)
    
def OvaalVOL():
    pygame.draw.ellipse(WIN, BLACK, OVAAL)

def OvaalLEEG():
    pygame.draw.ellipse(WIN, BLACK, OVAAL)
    
    
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
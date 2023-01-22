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

#Alle vorm en vulling combinaties
R_Ruit_Leeg = pygame.image.load("R_Ruit_Leeg.png")
R_Ruit_Gestreept  = pygame.image.load("R_Ruit_Gestreept.png")
R_Ruit_Vol  = pygame.image.load("R_Ruit_Vol.png")
R_Golf_Leeg  = pygame.image.load("R_Golf_Leeg.png")
R_Golf_Gestreept  = pygame.image.load("R_Golf_Gestreept.png")
R_Golf_Vol  = pygame.image.load("R_Golf_Vol.png")
R_Ovaal_Leeg  = pygame.image.load("R_Ovaal_Leeg.png")
R_Ovaal_Gestreept  = pygame.image.load("R_Ovaal_Gestreept.png")
R_Ovaal_Vol  = pygame.image.load("R_Ovaal_Vol.png")
G_Ruit_Leeg = pygame.image.load("G_Ruit_Leeg.png")
G_Ruit_Gestreept  = pygame.image.load("G_Ruit_Gestreept.png")
G_Ruit_Vol  = pygame.image.load("G_Ruit_Vol.png")
G_Golf_Leeg  = pygame.image.load("G_Golf_Leeg.png")
G_Golf_Gestreept  = pygame.image.load("G_Golf_Gestreept.png")
G_Golf_Vol  = pygame.image.load("G_Golf_Vol.png")
G_Ovaal_Leeg  = pygame.image.load("G_Ovaal_Leeg.png")
G_Ovaal_Gestreept  = pygame.image.load("G_Ovaal_Gestreept.png")
G_Ovaal_Vol  = pygame.image.load("G_Ovaal_Vol.png")
P_Ruit_Leeg = pygame.image.load("P_Ruit_Leeg.png")
P_Ruit_Gestreept  = pygame.image.load("P_Ruit_Gestreept.png")
P_Ruit_Vol  = pygame.image.load("P_Ruit_Vol.png")
P_Golf_Leeg  = pygame.image.load("P_Golf_Leeg.png")
P_Golf_Gestreept  = pygame.image.load("P_Golf_Gestreept.png")
P_Golf_Vol  = pygame.image.load("P_Golf_Vol.png")
P_Ovaal_Leeg  = pygame.image.load("P_Ovaal_Leeg.png")
P_Ovaal_Gestreept  = pygame.image.load("P_Ovaal_Gestreept.png")
P_Ovaal_Vol  = pygame.image.load("P_Ovaal_Vol.png")



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

"""Functies om kaarten met 2 en 3 vormen te maken, met de posities het midden 
van de kaart"""
def vormen2(vorm, positiex, positiey):
    WIN.blit(vorm,(positiex, positiey + 25) )
    WIN.blit(vorm, (positiex, positiey - 25))

def vormen3(vorm, positiex, positiey):
    WIN.blit(vorm, (positiex, positiey +50))
    WIN.blit(vorm, (positiex, positiey))
    WIN.blit(vorm, (positiex, positiey -50))
    

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
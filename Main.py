# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:50:46 2023

@author: Fenna
"""

import pygame
import random
import os
pygame.init()

WIN = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Set")
FPS = 60

#Kleuren RGB
WHITE = (255, 255, 255)
LILA = 	(210,175,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (255,0,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

#Alle vorm en vulling combinaties
R_Ruit_Leeg = pygame.image.load("Assets/R_Ruit_Leeg.png")
R_Ruit_Gestreept  = pygame.image.load("Assets/R_Ruit_Gestreept.png")
R_Ruit_Vol  = pygame.image.load("Assets/R_Ruit_Vol.png")
R_Golf_Leeg  = pygame.image.load("Assets/R_Golf_Leeg.png")
R_Golf_Gestreept  = pygame.image.load("Assets/R_Golf_Gestreept.png")
R_Golf_Vol  = pygame.image.load("Assets/R_Golf_Vol.png")
R_Ovaal_Leeg  = pygame.image.load("Assets/R_Ovaal_Leeg.png")
R_Ovaal_Gestreept  = pygame.image.load("Assets/R_Ovaal_Gestreept.png")
R_Ovaal_Vol  = pygame.image.load("Assets/R_Ovaal_Vol.png")
G_Ruit_Leeg = pygame.image.load("Assets/G_Ruit_Leeg.png")
G_Ruit_Gestreept  = pygame.image.load("Assets/G_Ruit_Gestreept.png")
G_Ruit_Vol  = pygame.image.load("Assets/G_Ruit_Vol.png")
G_Golf_Leeg  = pygame.image.load("Assets/G_Golf_Leeg.png")
G_Golf_Gestreept  = pygame.image.load("Assets/G_Golf_Gestreept.png")
G_Golf_Vol  = pygame.image.load("Assets/G_Golf_Vol.png")
G_Ovaal_Leeg  = pygame.image.load("Assets/G_Ovaal_Leeg.png")
G_Ovaal_Gestreept  = pygame.image.load("Assets/G_Ovaal_Gestreept.png")
G_Ovaal_Vol  = pygame.image.load("Assets/G_Ovaal_Vol.png")
P_Ruit_Leeg = pygame.image.load("Assets/P_Ruit_Leeg.png")
P_Ruit_Gestreept  = pygame.image.load("Assets/P_Ruit_Gestreept.png")
P_Ruit_Vol  = pygame.image.load("Assets/P_Ruit_Vol.png")
P_Golf_Leeg  = pygame.image.load("Assets/P_Golf_Leeg.png")
P_Golf_Gestreept  = pygame.image.load("Assets/P_Golf_Gestreept.png")
P_Golf_Vol  = pygame.image.load("Assets/P_Golf_Vol.png")
P_Ovaal_Leeg  = pygame.image.load("Assets/P_Ovaal_Leeg.png")
P_Ovaal_Gestreept  = pygame.image.load("Assets/P_Ovaal_Gestreept.png")
P_Ovaal_Vol  = pygame.image.load("Assets/P_Ovaal_Vol.png")



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

"""Functies om kaarten vormen te maken, van de linker boven hoek van de kaarten"""
def vormen1(vorm, positiex, positiey):
    x = positiex+10
    y = positiey+120
    WIN.blit(vorm, (x,y))

def vormen2(vorm, positiex, positiey): #nog nodig hoekpunten kaart
    x = positiex+10
    y = positiey+120
    WIN.blit(vorm,(x, y + 25) ) #nog aan aanpassen met hoekputen kaart
    WIN.blit(vorm, (x, y - 25))

def vormen3(vorm, positiex, positiey):  #nog nodig hoekpunten kaart
    x = positiex+10
    y = positiey+120
    WIN.blit(vorm, (x, y +50)) #nog aan aanpassen met hoekputen kaart
    WIN.blit(vorm, (x, y))
    WIN.blit(vorm, (x, y -50))
    

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


"""Functie voor grit visualiseren"""
def Grit15():
    font = pygame.font.SysFont("Times New Roman", 50, True, False)
    service = font.render( "." , True, (BLACK))
    lijn = font.render( "|" , True, (BLACK))
    WIN.blit(lijn, (150,0))
    WIN.blit(service, (175, 0))
    WIN.blit(service, (275, 0))
    WIN.blit(service, (300, 0))
    WIN.blit(service, (400, 0))
    WIN.blit(service, (425, 0))
    WIN.blit(service, (525, 0))
    WIN.blit(service, (550, 0))
    WIN.blit(service, (650, 0))
    WIN.blit(service, (675, 0))
    WIN.blit(service, (775, 0))
    WIN.blit(lijn, (150,200))
    WIN.blit(service, (175, 200))
    WIN.blit(service, (275, 200))
    WIN.blit(service, (300, 200))
    WIN.blit(service, (400, 200))
    WIN.blit(service, (425, 200))
    WIN.blit(service, (525, 200))
    WIN.blit(service, (550, 200))
    WIN.blit(service, (650, 200))
    WIN.blit(service, (675, 200))
    WIN.blit(service, (775, 200))
    WIN.blit(lijn, (150,225))
    WIN.blit(service, (175, 225))
    WIN.blit(service, (275, 225))
    WIN.blit(service, (300, 225))
    WIN.blit(service, (400, 225))
    WIN.blit(service, (425, 225))
    WIN.blit(service, (525, 225))
    WIN.blit(service, (550, 225))
    WIN.blit(service, (650, 225))
    WIN.blit(service, (675, 225))
    WIN.blit(service, (775, 225))
    WIN.blit(lijn, (150,425))
    WIN.blit(service, (175, 425))
    WIN.blit(service, (275, 425))
    WIN.blit(service, (300, 425))
    WIN.blit(service, (400, 425))
    WIN.blit(service, (425, 425))
    WIN.blit(service, (525, 425))
    WIN.blit(service, (550, 425))
    WIN.blit(service, (650, 425))
    WIN.blit(service, (675, 425))
    WIN.blit(service, (775, 425))
    WIN.blit(lijn, (150,450))
    WIN.blit(service, (175, 450))
    WIN.blit(service, (275, 450))
    WIN.blit(service, (300, 450))
    WIN.blit(service, (400, 450))
    WIN.blit(service, (425, 450))
    WIN.blit(service, (525, 450))
    WIN.blit(service, (550, 450))
    WIN.blit(service, (650, 450))
    WIN.blit(service, (675, 450))
    WIN.blit(service, (775, 450))
    WIN.blit(service, (25, 450))
    WIN.blit(service, (125, 450))
    WIN.blit(lijn, (150,650))
    WIN.blit(service, (175, 650))
    WIN.blit(service, (275, 650))
    WIN.blit(service, (300, 650))
    WIN.blit(service, (400, 650))
    WIN.blit(service, (425, 650))
    WIN.blit(service, (525, 650))
    WIN.blit(service, (550, 650))
    WIN.blit(service, (650, 650))
    WIN.blit(service, (675, 650))
    WIN.blit(service, (775, 650))
    WIN.blit(service, (25, 650))
    WIN.blit(service, (125, 650))


"""Een fuctie die een afbeedling pixel voor pixel van kleur veranderd"""
def set_color(img, color):
    r, g, b = color
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            a = img.get_at((x, y))[3]
            img.set_at((x, y), (r,g,b,a))  # Set the color of the pixel.

#dingen testen
DVD = pygame.image.load(os.path.join('Assets', 'DVDWHITE.png'))
set_color(DVD, BLACK)


"""Een functie om alles op het scherm te tekenen"""
def Draw():
    WIN.fill(LILA)
    text("Set")
    Grit15()
    vormen1(R_Ovaal_Gestreept, 175, 225)
    vormen2(G_Golf_Vol, 175, 0)
    vormen3(P_Ruit_Leeg, 175, 450)
    pygame.display.update()

    
"""Main funcitie die alle functies los oproept"""
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Draw()
    pygame.quit()

if __name__ == "__main__":
    main()
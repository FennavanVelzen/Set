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
PURPLE = (75,0,130)

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

#andere afbeeldingen
achterkant = pygame.image.load("Assets/Achterkant.png")
Achterkant = pygame.transform.scale(achterkant, (150,230))
legekaart = pygame.image.load("Assets/Blank-Playing-Card.png")
Legekaart = pygame.transform.scale(legekaart, (155,240))
voorbeelden = pygame.image.load("Assets/Voorbeelden.jpg")
Voorbeelden1 = pygame.transform.scale(voorbeelden, (600,450))
Voorbeelden = pygame.transform.rotate(Voorbeelden1, 90)


"""Functie om alle combinatie mogelijkheden voor kaarten te genereren.
Deze functie neemt steeds een eigenschap uit een lijst en voegt hier alle 
overige mogelijkheden van combinaties van andere lijsten aan toe."""

def Kaarten():
    Kleuren = ['Rood', 'Groen', 'Paars'] #lijsten met eigenschap mogelijkheden van de kaarten
    Vormen = ['Ruit', 'Ovaal', 'Golf']
    Hoeveelheid = [1,2,3]
    Vulling = ['Leeg', 'Gestreept' , 'Vol']
    Kaarten = []                        #lijst om alle kaart combinaties in toe te voegen
    for kleur in Kleuren:
        for vorm in Vormen:
            for aantal in Hoeveelheid:
                for inhoud in Vulling:
                    Kaart = [kleur, vorm, inhoud, aantal]
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

def text(Text, positie, kleur,lettergrote):
    font = pygame.font.SysFont("Times New Roman", lettergrote, True, False)
    service = font.render( Text , True, kleur)
    WIN.blit(service, positie)

"""Functies om kaarten vormen te maken, van de linker boven hoek van de kaarten"""
def vormen1(vorm, locatie):
    positiex, positiey = locatie
    x = positiex+6
    y = positiey+110
    WIN.blit(vorm, (x,y))

def vormen2(vorm, locatie): #nog nodig hoekpunten kaart
    positiex, positiey = locatie
    x = positiex +6
    y = positiey +110
    WIN.blit(vorm,(x, y + 25) ) #nog aan aanpassen met hoekputen kaart
    WIN.blit(vorm, (x, y - 25))

def vormen3(vorm, locatie):  #nog nodig hoekpunten kaart
    positiex, positiey = locatie
    x = positiex+6
    y = positiey+110
    WIN.blit(vorm, (x, y +50)) #nog aan aanpassen met hoekputen kaart
    WIN.blit(vorm, (x, y))
    WIN.blit(vorm, (x, y -50))
    
"""functie voor het schrijven van de nummers in de hoeken van de kaarten"""
def Nummeriek(a, positiex, positiey):
    x = positiex+10
    y = positiey+40
    text(a, (x, y), (BLACK) , 30)

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
def Grit12():
    font = pygame.font.SysFont("Times New Roman", 50, True, False)
    service = font.render( "." , True, (BLACK))
    lijn = font.render( "|" , True, (BLACK))
    a = 0
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))
    a = 200
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))
    a = 225
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))
    a = 425
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))
    a = 450
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))
    a =650
    WIN.blit(lijn, (150,a))
    WIN.blit(service, (200, a))
    WIN.blit(service, (300, a))
    WIN.blit(service, (350, a))
    WIN.blit(service, (450, a))
    WIN.blit(service, (500, a))
    WIN.blit(service, (600, a))
    WIN.blit(service, (650, a))
    WIN.blit(service, (750, a))


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

def regels():
    text("Elke kaart heeft 4 eigenschappen, te weten een hoeveelheid, een kleur," ,(20,150),BLACK,25)
    text("een vorm en een vulling. Er zijn drie varienten van elke eigenschap",(20,175),BLACK,25)
    text("Een SET bestaat uit 3 kaarten waarvan voor alle 4 eigenschappen ",(20,200),BLACK,25)
    text("afzonderlijk geldt dat de variant ervan precies gelijk of volledig",(20,225),BLACK,25)
    text("verschillend moeten zijn. Bij elke combinatie van 3 kaarten stel je jezef" ,(20,250),BLACK,25)
    text("steeds voor elke eigenschap apart de vraag: is de variant van deze",(20,275),BLACK,25)
    text("eigenschap op alle kaarten precies gelijk of volledig verschillend? ",(20,300),BLACK,25)
    text("Kan je deze vraag voor alle eigenschappen met JA beantwoorden, dan",(20,325),BLACK,25)
    text("heb je een set gevonden.",(20,350),BLACK,25)
    text("Uit handleiding SET, Marsha J. Falco",(20,375),BLACK, 15)    

"""Een fuctie die op basis van de eigenschappen van de kaart en locatie deze kan tekenen"""
#deze functie zou misschien nog ingekort en verbeterd worden.
def DrawKaart(kaart, locatie):
    positiex, positiey = locatie
    x = positiex -15
    y = positiey +15
    WIN.blit(Legekaart, (x,y))
    if kaart[0] == 'Rood':                              #alles voor rood
        if kaart[1] == 'Ruit':                          #alles voor ruit en rood
            if kaart[2] == 'Leeg':                      #alles voor ruit en rood en leeg
                if kaart[3] == 1:
                    vormen1(R_Ruit_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ruit_Leeg, locatie)
                else:
                    vormen3(R_Ruit_Leeg, locatie)
            elif kaart[2] == 'Gestreept':               #alles voor ruit en rood en gestreept
                if kaart[3] == 1:
                    vormen1(R_Ruit_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ruit_Gestreept, locatie)
                else:
                    vormen3(R_Ruit_Gestreept, locatie)
            elif kaart[2] == 'Vol':                     #alles voor ruit en rood en vol
                if kaart[3] == 1:
                    vormen1(R_Ruit_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ruit_Vol, locatie)
                else:
                    vormen3(R_Ruit_Vol, locatie)
        if kaart[1] == 'Ovaal':                         #het vorige harhaald door de rest van de functie
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(R_Ovaal_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ovaal_Leeg, locatie)
                else:
                    vormen3(R_Ovaal_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(R_Ovaal_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ovaal_Gestreept, locatie)
                else:
                    vormen3(R_Ovaal_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(R_Ovaal_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Ovaal_Vol, locatie)
                else:
                    vormen3(R_Ovaal_Vol, locatie)
        if kaart[1] == 'Golf':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(R_Golf_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Golf_Leeg, locatie)
                else:
                    vormen3(R_Golf_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(R_Golf_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Golf_Gestreept, locatie)
                else:
                    vormen3(R_Golf_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(R_Golf_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(R_Golf_Vol, locatie)
                else:
                    vormen3(R_Golf_Vol, locatie)
    if kaart[0] == 'Paars':
        if kaart[1] == 'Ruit':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(P_Ruit_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ruit_Leeg, locatie)
                else:
                    vormen3(P_Ruit_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(P_Ruit_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ruit_Gestreept, locatie)
                else:
                    vormen3(P_Ruit_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(P_Ruit_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ruit_Vol, locatie)
                else:
                    vormen3(P_Ruit_Vol, locatie)
        if kaart[1] == 'Ovaal':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(P_Ovaal_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ovaal_Leeg, locatie)
                else:
                    vormen3(P_Ovaal_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(P_Ovaal_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ovaal_Gestreept, locatie)
                else:
                    vormen3(P_Ovaal_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(P_Ovaal_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Ovaal_Vol, locatie)
                else:
                    vormen3(P_Ovaal_Vol, locatie)
        if kaart[1] == 'Golf':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(P_Golf_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Golf_Leeg, locatie)
                else:
                    vormen3(P_Golf_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(P_Golf_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Golf_Gestreept, locatie)
                else:
                    vormen3(P_Golf_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(P_Golf_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(P_Golf_Vol, locatie)
                else:
                    vormen3(P_Golf_Vol, locatie)
    if kaart[0] == 'Groen':
        if kaart[1] == 'Ruit':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(G_Ruit_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ruit_Leeg, locatie)
                else:
                    vormen3(G_Ruit_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(G_Ruit_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ruit_Gestreept, locatie)
                else:
                    vormen3(G_Ruit_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(G_Ruit_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ruit_Vol, locatie)
                else:
                    vormen3(G_Ruit_Vol, locatie)
        if kaart[1] == 'Ovaal':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(G_Ovaal_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ovaal_Leeg, locatie)
                else:
                    vormen3(G_Ovaal_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(G_Ovaal_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ovaal_Gestreept, locatie)
                else:
                    vormen3(G_Ovaal_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(G_Ovaal_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Ovaal_Vol, locatie)
                else:
                    vormen3(G_Ovaal_Vol, locatie)
        if kaart[1] == 'Golf':
            if kaart[2] == 'Leeg':
                if kaart[3] == 1:
                    vormen1(G_Golf_Leeg, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Golf_Leeg, locatie)
                else:
                    vormen3(G_Golf_Leeg, locatie)
            elif kaart[2] == 'Gestreept':
                if kaart[3] == 1:
                    vormen1(G_Golf_Gestreept, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Golf_Gestreept, locatie)
                else:
                    vormen3(G_Golf_Gestreept, locatie)
            elif kaart[2] == 'Vol':
                if kaart[3] == 1:
                    vormen1(G_Golf_Vol, locatie)
                elif kaart[3] == 2:
                    vormen2(G_Golf_Vol, locatie)
                else:
                    vormen3(G_Golf_Vol, locatie)
                

"""Functie om alle kaarten op het scherm te tekenen, houd ook rekening met wannneer er 
minder dan 12 kaarten zijn"""
def DrawKaarten(geschud):
    if len(geschud) >= 12:
        DrawKaart(geschud[0], (200,0))
        DrawKaart(geschud[1], (350,0))
        DrawKaart(geschud[2], (500,0))
        DrawKaart(geschud[3], (650,0))
        DrawKaart(geschud[4], (200,225))
        DrawKaart(geschud[5], (350,225))
        DrawKaart(geschud[6], (500,225))
        DrawKaart(geschud[7], (650,225))
        DrawKaart(geschud[8], (200,450))
        DrawKaart(geschud[9], (350,450))
        DrawKaart(geschud[10], (500,450))
        DrawKaart(geschud[11], (650,450))
    elif len(geschud) == 9:
        DrawKaart(geschud[0], (200,0))
        DrawKaart(geschud[1], (350,0))
        DrawKaart(geschud[2], (500,0))
        DrawKaart(geschud[3], (200,225))
        DrawKaart(geschud[4], (350,225))
        DrawKaart(geschud[5], (500,225))
        DrawKaart(geschud[6], (200,450))
        DrawKaart(geschud[7], (350,450))
        DrawKaart(geschud[8], (500,450))
    elif len(geschud) == 6:
        DrawKaart(geschud[0], (200,0))
        DrawKaart(geschud[1], (350,0))
        DrawKaart(geschud[2], (200,225))
        DrawKaart(geschud[3], (350,225))
        DrawKaart(geschud[4], (200,450))
        DrawKaart(geschud[5], (350,450))
    elif len(geschud) == 3:
        DrawKaart(geschud[0], (200,0))
        DrawKaart(geschud[1], (200,225))
        DrawKaart(geschud[2], (200,450))
              
"""Functie om alle nummers/ symbolen op het scherm te tekenen op de kaarten, 
houd ook rekening met wannneer er minder dan 12 kaarten zijn"""
def Positie_kaarten(geschud):
    if len(geschud)>=12:
        Nummeriek("1",200, 0)
        Nummeriek("2",350, 0)
        Nummeriek("3",500, 0)
        Nummeriek("4",650, 0)
        Nummeriek("5",200, 225)
        Nummeriek("6",350, 225)
        Nummeriek("7",500, 225)
        Nummeriek("8",650, 225)
        Nummeriek("9",200, 450)
        Nummeriek("0",350, 450)
        Nummeriek("-",500, 450)
        Nummeriek("=",650, 450)
    elif len(geschud) == 9:
        Nummeriek("1",200, 0)
        Nummeriek("2",350, 0)
        Nummeriek("3",500, 0)
        Nummeriek("4",200, 225)
        Nummeriek("5",350, 225)
        Nummeriek("6",500, 225)
        Nummeriek("7",200, 450)
        Nummeriek("8",350, 450)
        Nummeriek("9",500, 450)
    elif len(geschud) == 6:
        Nummeriek("1",200, 0)
        Nummeriek("2",350, 0)
        Nummeriek("3",200, 225)
        Nummeriek("4",350, 225)
        Nummeriek("5",200, 450)
        Nummeriek("6",350, 450)
    elif len(geschud) == 3:
        Nummeriek("1",200, 0)
        Nummeriek("2",200, 225)
        Nummeriek("3",200, 450)

"""Functie voor interactie met de kaarten"""
#misschien ook een check dat er niet 3 keer dezefde kaart geselecteerd kan worden
def KaartenSelect(geschud, kaart1, kaart2, kaart3, aantal, run, start):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            return run, aantal, kaart1, kaart2 , kaart3, start
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                start = False
            if event.key == pygame.K_1:
                if kaart1 == False:
                    kaart1 = geschud[0]
                    kaart1.append(0)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[0]
                    kaart2.append(0)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[0]
                    kaart3.append(0)
                    aantal +=1
            elif event.key == pygame.K_2:
                if kaart1 == False:
                    kaart1 = geschud[1]
                    kaart1.append(1)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[1]
                    kaart2.append(1)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[1]
                    kaart3.append(1)
                    aantal +=1
            elif event.key == pygame.K_3:
                if kaart1 == False:
                    kaart1 = geschud[2]
                    kaart1.append(2)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[2]
                    kaart2.append(2)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[2]
                    kaart3.append(2)
                    aantal +=1
            elif event.key == pygame.K_4:
                if kaart1 == False:
                    kaart1 = geschud[3]
                    kaart1.append(3)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[3]
                    kaart2.append(3)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[3]
                    kaart3.append(3)
                    aantal +=1
            elif event.key == pygame.K_5:
                if kaart1 == False:
                    kaart1 = geschud[4]
                    kaart1.append(4)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[4]
                    kaart2.append(4)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[4]
                    kaart3.append(4)
                    aantal +=1
            elif event.key == pygame.K_6:
                if kaart1 == False:
                    kaart1 = geschud[5]
                    kaart1.append(5)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[5]
                    kaart2.append(5)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[5]
                    kaart3.append(5)
                    aantal +=1
            elif event.key == pygame.K_7:
                if kaart1 == False:
                    kaart1 = geschud[6]
                    kaart1.append(6)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[6]
                    kaart2.append(6)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[6]
                    kaart3.append(6)
                    aantal +=1
            elif event.key == pygame.K_8:
                if kaart1 == False:
                    kaart1 = geschud[7]
                    kaart1.append(7)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[7]
                    kaart2.append(7)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[7]
                    kaart3.append(7)
                    aantal +=1
            elif event.key == pygame.K_9:
                if kaart1 == False:
                    kaart1 = geschud[8]
                    kaart1.append(8)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[8]
                    kaart2.append(8)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[8]
                    kaart3.append(8)
                    aantal +=1
            elif event.key == pygame.K_0:
                if kaart1 == False:
                    kaart1 = geschud[9]
                    kaart1.append(9)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[9]
                    kaart2.append(9)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[9]
                    kaart3.append(9)
                    aantal +=1
            elif event.key == pygame.K_MINUS:
                if kaart1 == False:
                    kaart1 = geschud[10]
                    kaart1.append(10)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[10]
                    kaart2.append(10)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[10]
                    kaart3.append(10)
                    aantal +=1
            elif event.key == pygame.K_EQUALS:
                if kaart1 == False:
                    kaart1 = geschud[11]
                    kaart1.append(11)
                    aantal +=1
                elif kaart2 == False:
                    kaart2 = geschud[11]
                    kaart2.append(11)
                    aantal +=1
                elif kaart3 == False:
                    kaart3 = geschud[11]
                    kaart3.append(11)
                    aantal +=1
    return run, aantal, kaart1, kaart2 , kaart3, start

"""Functie die op basis van 3 kaarten checkt of het een SET of CapSet is"""
def SETcheck(kaart1, kaart2, kaart3, geschud , seconden):
    if kaart1[0] == kaart2[0] == kaart3[0] or kaart1[0] != kaart2[0] != kaart3[0]:
        if kaart1[1] == kaart2[1] == kaart3[1] or kaart1[1] != kaart2[1] != kaart3[1]:
            if kaart1[2] == kaart2[2] == kaart3[2] or kaart1[2] != kaart2[2] != kaart3[2]:
                if kaart1[3] == kaart2[3] == kaart3[3] or kaart1[3] != kaart2[3] != kaart3[3]:
                    print('SET')
                    aantal = 0
                    seconden = 0
                    if kaart1[4] > kaart2[4]:
                        if kaart2[4] > kaart3[4]:
                            del geschud[kaart1[4]]
                            del geschud[kaart2[4]]
                            del geschud[kaart3[4]]
                        elif kaart2[4] < kaart3[4]:
                            del geschud[kaart1[4]]
                            del geschud[kaart3[4]]
                            del geschud[kaart2[4]]
                    elif kaart2[4] > kaart1[4]:
                        if kaart1[4]> kaart3[4]:
                            del geschud[kaart2[4]]
                            del geschud[kaart1[4]]
                            del geschud[kaart3[4]]
                        elif kaart1[4] < kaart3[4]:
                            del geschud[kaart2[4]]
                            del geschud[kaart3[4]]
                            del geschud[kaart1[4]]
                    elif kaart3[4] > kaart1[4]:
                        if kaart1[4] > kaart2[4]:
                            del geschud[kaart3[4]]
                            del geschud[kaart1[4]]
                            del geschud[kaart2[4]]
                        elif kaart1[4] < kaart2[4]:
                            del geschud[kaart3[4]]
                            del geschud[kaart2[4]]
                            del geschud[kaart1[4]]
                                               
                    kaart1 = False                #een aantal keer dezefde kaart geselecteerd
                    kaart2 = False                #en moet zoizo op False gezet worden
                    kaart3 = False
                    
                    return aantal, kaart1, kaart2, kaart3, seconden
                else: 
                    print('Capset')
                    aantal = 0
                    kaart1 = False
                    kaart2 = False
                    kaart3 = False
                    return aantal, kaart1, kaart2, kaart3, seconden
            else:
                print('Capset')
                aantal = 0
                kaart1 = False
                kaart2 = False
                kaart3 = False
                return aantal, kaart1, kaart2, kaart3, seconden
        else:
            print('Capset')
            aantal = 0
            kaart1 = False
            kaart2 = False
            kaart3 = False
            return aantal, kaart1, kaart2, kaart3, seconden
    else:
        print('Capset')
        aantal = 0
        kaart1 = False
        kaart2 = False
        kaart3 = False
        return aantal, kaart1, kaart2, kaart3, seconden


"""Funcite die na 30 seconden de 1e drie kaarten vananderd"""
#misschien nog kijken naar wanneer er minder dan 12 kaarten zijn.
def timer(geschud, seconden, kaart1 , kaart2, kaart3):
    seconden +=1
    if seconden >= 1800:    #1800 omdat FPS is 60 en 60x30 = 1800
        if len(geschud)>12:
            WillekeurigGetal = random.randint(12,(len(geschud)-1))
            geschud[1], geschud[WillekeurigGetal] = geschud[WillekeurigGetal], geschud[1]
            WillekeurigGetal = random.randint(12,(len(geschud)-1))
            geschud[2], geschud[WillekeurigGetal] = geschud[WillekeurigGetal], geschud[2]
            WillekeurigGetal = random.randint(12,(len(geschud)-1))
            geschud[0], geschud[WillekeurigGetal] = geschud[WillekeurigGetal], geschud[0]
            seconden = 0
            kaart1 = False
            kaart2 = False
            kaart3 = False
    return geschud, seconden, kaart1 , kaart2, kaart3

"""Een functie om alles op het scherm te tekenen, voor tijdens het spel"""
def DrawSpel(geschud):
    WIN.fill(LILA)
    text("Set",(0, 0),(BLACK),50)
#    Grit12()
    DrawKaarten(geschud)
    Positie_kaarten(geschud)
    WIN.blit(Achterkant, (10, 475))
    pygame.display.update()

"""Een functie om alles op het scherm te tekenen, voor het startscherm"""
def DrawStart():
    WIN.fill(LILA)
    text("Set",(325, 250),(PURPLE),100)
    text(" |Klik op spatie om te beginnen|", (75,350),(BLACK),50)
    text(" |Klik op r voor de regels|", (75,400),(BLACK),50)
    pygame.display.update()
    
"""Een functie om alles op het scherm te tekenen, voor het regelscherm"""  
def Drawrules():
    WIN.fill(LILA)
    text("Regels", (0,0),(BLACK),50)
    text("Klik b om terug te gaan", (0,50),(BLACK),40)
    text("Klik v naar voorbeelden te gaan", (0,100), (BLACK),40)
    regels()
                
    pygame.display.update()

"""Een functie om alles op het scherm te tekenen, voor het voorbeeldenscherm"""  
def Drawvoorbeeld():
    WIN.fill(LILA)
    text("Set",(0, 0),(BLACK),50)
    text("Klik b om terug te gaan", (0,625),(BLACK),30)
    WIN.blit(Voorbeelden, (175,0))
    pygame.display.update()
    
"""functie voor het kunnen aanroepen van een quit voor wanneer er een loop is""" 
def Quit():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run


"""Funcite voor het navigeren tussen de verschillende schermen
b - back, spatie-start, r -regels, v-voorbeelden"""
def navigatie(run):
    start = False
    rules = False
    voorbeeld = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
                kaarten = Kaarten()
                geschud = Schudden(kaarten)
                aantal = 0
                kaart1 = False
                kaart2 = False
                kaart3 = False
                seconden = 0
            if event.key == pygame.K_r:
                rules = True

    while start and run:                            #Startscherm
        DrawSpel(geschud)
        run, aantal, kaart1, kaart2 , kaart3, start = KaartenSelect(geschud, kaart1, kaart2, kaart3, aantal, run, start)
        if aantal == 3:
            aantal, kaart1, kaart2, kaart3, seconden = SETcheck(kaart1, kaart2, kaart3, geschud, seconden)
        geschud, seconden, kaart1 , kaart2, kaart3 = timer(geschud, seconden, kaart1 , kaart2, kaart3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_b:
                    #start = False
        
    while rules and run:                            #Regelscherm
        Drawrules()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    voorbeeld = True
                    rules = False
                if event.key == pygame.K_b:
                    rules = False
    while voorbeeld and run:                        #Voorbeeldenscherm
        Drawvoorbeeld()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    rules = True
                    voorbeeld = False
    return run

"""Main funcitie die alle functies los oproept"""
def main():
    global run
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        DrawStart()
        run = navigatie(run)
                
    pygame.quit()

if __name__ == "__main__":
    main()
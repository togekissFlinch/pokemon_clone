
run = True 

import pygame

import time

pygame.init()
class creer_pokemon(pygame.sprite.Sprite):
    def __init__(self, nom, x, y):
        self.nom = nom
        self.sprite = pygame.image.load(nom + ".png")
        self.x = x
        self.y = y
class creer_objet(pygame.sprite.Sprite):
       def __init__(self, nom, x, y):
           self.nom = nom
           self.sprite = pygame.image.load(nom + ".png")
           self.x = x
           self.y = y
font = pygame.font.Font("ARCADECLASSIC.TTF", 50)

def afficher(text, x, y):
    texxte = font.render(text, True, (0,0,0))
    screen.blit(texxte, (x,y))
screen = pygame.display.set_mode((900, 700))
screen.fill("lightgreen")
pygame.display.set_caption("Pokemon Clone") 
pickachu = creer_pokemon("Pickachu", 350, 100)
bulbizzare = creer_pokemon("bulbizzare", -50, 300)
barre = creer_objet("barre",0, 500)
while run:    
    pygame.display.flip()
    screen.blit(pickachu.sprite, (pickachu.x, pickachu.y))
    screen.blit(bulbizzare.sprite, (bulbizzare.x, bulbizzare.y))
    screen.blit(barre.sprite, (barre.x, barre.y))
    afficher("Thomas sent out " + pickachu.nom + " !!!!", 30, 550)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("goodbye")

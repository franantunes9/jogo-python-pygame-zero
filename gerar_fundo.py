import random
import pygame

pygame.init()
random.seed(7)
fundo = pygame.Surface((600, 400))
fundo.fill((20, 20, 50))
for _ in range(80):
    x = random.randint(0, 599)
    y = random.randint(0, 399)
    brilho = random.randint(120, 255)
    tamanho = random.choice([1, 1, 2])
    pygame.draw.circle(fundo, (brilho, brilho, brilho), (x, y), tamanho)
pygame.image.save(fundo, "images/fundo.png")
print("Fundo criado em images/fundo.png")

import math
import pygame

pygame.init()

# Jogador: bolinha laranja com olhos
j = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(j, (255, 165, 0), (20, 20), 20)
pygame.draw.circle(j, (255, 255, 255), (13, 15), 5)
pygame.draw.circle(j, (255, 255, 255), (27, 15), 5)
pygame.draw.circle(j, (0, 0, 0), (13, 15), 2)
pygame.draw.circle(j, (0, 0, 0), (27, 15), 2)
pygame.image.save(j, "images/jogador.png")

# Estrela amarela de 5 pontas
e = pygame.Surface((24, 24), pygame.SRCALPHA)
pontos = []
for i in range(10):
    angulo = -math.pi / 2 + i * math.pi / 5
    raio = 11 if i % 2 == 0 else 4.5
    pontos.append((12 + raio * math.cos(angulo), 12 + raio * math.sin(angulo)))
pygame.draw.polygon(e, (255, 230, 0), pontos)
pygame.image.save(e, "images/estrela.png")

# Obstaculo: bola vermelha com borda escura
o = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(o, (220, 30, 30), (15, 15), 15)
pygame.draw.circle(o, (120, 0, 0), (15, 15), 15, 3)
pygame.image.save(o, "images/obstaculo.png")

print("Imagens criadas em images/")

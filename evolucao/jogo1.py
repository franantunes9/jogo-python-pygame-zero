from random import randint

WIDTH = 600
HEIGHT = 400

jogador = Rect((280, 180), (40, 40))
estrela = Rect((100, 100), (20, 20))
pontos = 0

def draw():
    screen.fill((30, 30, 60))
    screen.draw.filled_rect(jogador, "orange")
    screen.draw.filled_rect(estrela, "yellow")
    screen.draw.text(f"Pontos: {pontos}", topleft=(10, 10), fontsize=30)

def update():
    global pontos
    if keyboard.left and jogador.left > 0:
        jogador.x -= 5
    if keyboard.right and jogador.right < WIDTH:
        jogador.x += 5
    if keyboard.up and jogador.top > 0:
        jogador.y -= 5
    if keyboard.down and jogador.bottom < HEIGHT:
        jogador.y += 5

    if jogador.colliderect(estrela):
        pontos += 1
        estrela.x = randint(0, WIDTH - 20)
        estrela.y = randint(0, HEIGHT - 20)

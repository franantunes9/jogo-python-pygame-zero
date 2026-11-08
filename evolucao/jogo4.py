from random import randint

WIDTH = 600
HEIGHT = 400

jogador = Actor("jogador", pos=(300, 200))
estrela = Actor("estrela", pos=(100, 100))
obstaculo = Actor("obstaculo", pos=(300, -15))
pontos = 0
tempo = 30
fim = False

def draw():
    screen.fill((30, 30, 60))
    if fim:
        screen.draw.text("Fim de jogo!", center=(300, 140), fontsize=60)
        screen.draw.text(f"Pontos: {pontos}", center=(300, 200), fontsize=40)
        screen.draw.text("Aperte ESPACO para jogar de novo", center=(300, 260), fontsize=28)
        return
    jogador.draw()
    estrela.draw()
    obstaculo.draw()
    screen.draw.text(f"Pontos: {pontos}", topleft=(10, 10), fontsize=30)
    screen.draw.text(f"Tempo: {tempo}", topright=(590, 10), fontsize=30)

def contar_tempo():
    global tempo, fim
    if not fim:
        tempo -= 1
        if tempo <= 0:
            fim = True

clock.schedule_interval(contar_tempo, 1.0)

def novo_obstaculo():
    obstaculo.pos = (randint(15, WIDTH - 15), -15)

def reiniciar():
    global pontos, tempo, fim
    pontos = 0
    tempo = 30
    fim = False
    jogador.pos = (300, 200)
    novo_obstaculo()

def update():
    global pontos
    if fim:
        if keyboard.space:
            reiniciar()
        return
    if keyboard.left and jogador.left > 0:
        jogador.x -= 5
    if keyboard.right and jogador.right < WIDTH:
        jogador.x += 5
    if keyboard.up and jogador.top > 0:
        jogador.y -= 5
    if keyboard.down and jogador.bottom < HEIGHT:
        jogador.y += 5

    obstaculo.y += 4
    if obstaculo.top > HEIGHT:
        novo_obstaculo()

    if jogador.colliderect(estrela):
        pontos += 1
        estrela.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))

    if jogador.colliderect(obstaculo):
        pontos = max(0, pontos - 1)
        novo_obstaculo()

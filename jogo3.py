from random import randint

WIDTH = 600
HEIGHT = 400

jogador = Rect((280, 180), (40, 40))
estrela = Rect((100, 100), (20, 20))
obstaculo = Rect((300, 0), (30, 30))
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
    screen.draw.filled_rect(jogador, "orange")
    screen.draw.filled_rect(estrela, "yellow")
    screen.draw.filled_rect(obstaculo, "red")
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
    obstaculo.x = randint(0, WIDTH - 30)
    obstaculo.y = 0

def reiniciar():
    global pontos, tempo, fim
    pontos = 0
    tempo = 30
    fim = False
    jogador.topleft = (280, 180)
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
        estrela.x = randint(0, WIDTH - 20)
        estrela.y = randint(0, HEIGHT - 20)

    if jogador.colliderect(obstaculo):
        pontos = max(0, pontos - 1)
        novo_obstaculo()

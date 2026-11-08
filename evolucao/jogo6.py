from random import randint, shuffle, sample

WIDTH = 600
HEIGHT = 400
RAIO = 25
CORES = ["tomato", "deepskyblue", "limegreen", "orange", "violet"]

jogador = Actor("jogador", pos=(300, 350))
pontos = 0
tempo = 60
fim = False
alvo = 1
numeros = []

def sortear():
    global alvo, numeros
    alvo = randint(1, 5)
    outros = [n for n in range(1, 6) if n != alvo]
    escolhidos = [alvo] + sample(outros, 2)
    posicoes = [100, 300, 500]
    shuffle(posicoes)
    numeros = []
    for valor, x in zip(escolhidos, posicoes):
        numeros.append({"valor": valor, "x": x, "y": randint(80, 260)})

sortear()

def draw():
    screen.fill((30, 30, 60))
    if fim:
        screen.draw.text("Fim de jogo!", center=(300, 140), fontsize=60)
        screen.draw.text(f"Pontos: {pontos}", center=(300, 200), fontsize=40)
        screen.draw.text("Aperte ESPACO para jogar de novo", center=(300, 260), fontsize=28)
        return
    for n in numeros:
        screen.draw.filled_circle((n["x"], n["y"]), RAIO, CORES[n["valor"] - 1])
        screen.draw.text(str(n["valor"]), center=(n["x"], n["y"]), fontsize=40, color="white")
    jogador.draw()
    screen.draw.text(f"Pegue o número {alvo}", center=(300, 45), fontsize=44)
    screen.draw.text(f"Pontos: {pontos}", topleft=(10, 10), fontsize=30)
    screen.draw.text(f"Tempo: {tempo}", topright=(590, 10), fontsize=30)

def contar_tempo():
    global tempo, fim
    if not fim:
        tempo -= 1
        if tempo <= 0:
            fim = True
            sounds.fim.play()

clock.schedule_interval(contar_tempo, 1.0)

def reiniciar():
    global pontos, tempo, fim
    pontos = 0
    tempo = 60
    fim = False
    jogador.pos = (300, 350)
    sortear()

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

    for n in numeros:
        if jogador.distance_to((n["x"], n["y"])) < RAIO + 20:
            if n["valor"] == alvo:
                pontos += 1
                sounds.ponto.play()
            else:
                pontos = max(0, pontos - 1)
                sounds.erro.play()
            jogador.pos = (300, 350)
            sortear()
            break

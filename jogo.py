# Caça-estrelas: jogo feito com Pygame Zero
# Controles: as setas movem o jogador; ESPAÇO começa e reinicia.
from random import randint

# ---------- Configurações ----------
WIDTH = 600
HEIGHT = 400
TITLE = "Caça-estrelas"
TEMPO_TOTAL = 30          # segundos de cada partida
VELOCIDADE_JOGADOR = 5    # pixels por quadro
MAX_OBSTACULOS = 5        # limite de obstáculos na tela
PONTOS_POR_NIVEL = 5      # a cada 5 pontos, sobe de nível

# ---------- Estado do jogo ----------
estado = "inicio"         # pode ser "inicio", "jogando" ou "fim"
pontos = 0
recorde = 0
tempo = TEMPO_TOTAL
nivel = 1

# ---------- Personagens (Actors) ----------
jogador = Actor("jogador", pos=(300, 350))
estrela = Actor("estrela", pos=(100, 100))


def criar_obstaculo():
    """Cria um obstáculo no topo da tela, numa posição horizontal aleatória."""
    return Actor("obstaculo", pos=(randint(15, WIDTH - 15), -15))


obstaculos = [criar_obstaculo()]


def reposicionar(obstaculo):
    """Devolve um obstáculo para o topo da tela."""
    obstaculo.pos = (randint(15, WIDTH - 15), -15)


def draw():
    """Desenha a tela de acordo com o estado do jogo."""
    screen.fill((30, 30, 60))
    if estado == "inicio":
        screen.draw.text("Caça-estrelas", center=(300, 120), fontsize=64, color="yellow")
        screen.draw.text("Mova-se com as setas e pegue as estrelas", center=(300, 200), fontsize=28)
        screen.draw.text("Desvie das bolas vermelhas", center=(300, 235), fontsize=28)
        screen.draw.text("Aperte ESPAÇO para começar", center=(300, 320), fontsize=32)
        return
    if estado == "fim":
        screen.draw.text("Fim de jogo!", center=(300, 120), fontsize=60)
        screen.draw.text(f"Pontos: {pontos}", center=(300, 190), fontsize=40)
        screen.draw.text(f"Recorde: {recorde}", center=(300, 230), fontsize=32)
        screen.draw.text("Aperte ESPAÇO para jogar de novo", center=(300, 310), fontsize=28)
        return
    jogador.draw()
    estrela.draw()
    for obstaculo in obstaculos:
        obstaculo.draw()
    screen.draw.text(f"Pontos: {pontos}", topleft=(10, 10), fontsize=30)
    screen.draw.text(f"Nível: {nivel}", midtop=(300, 10), fontsize=30)
    screen.draw.text(f"Tempo: {tempo}", topright=(590, 10), fontsize=30)


def contar_tempo():
    """Roda a cada segundo. Diminui o tempo e termina a partida em zero."""
    global tempo, estado, recorde
    if estado == "jogando":
        tempo -= 1
        if tempo <= 0:
            estado = "fim"
            recorde = max(recorde, pontos)
            sounds.fim.play()


clock.schedule_interval(contar_tempo, 1.0)


def iniciar():
    """Zera tudo e começa uma nova partida."""
    global estado, pontos, tempo, nivel, obstaculos
    pontos = 0
    tempo = TEMPO_TOTAL
    nivel = 1
    jogador.pos = (300, 350)
    estrela.pos = (randint(20, WIDTH - 20), randint(60, 250))
    obstaculos = [criar_obstaculo()]
    estado = "jogando"


def update():
    """Roda várias vezes por segundo: movimento, colisões e níveis."""
    global pontos, nivel

    # Nas telas de início e de fim, só espera o ESPAÇO.
    if estado != "jogando":
        if keyboard.space:
            iniciar()
        return

    # Movimento do jogador, sem sair da tela.
    if keyboard.left and jogador.left > 0:
        jogador.x -= VELOCIDADE_JOGADOR
    if keyboard.right and jogador.right < WIDTH:
        jogador.x += VELOCIDADE_JOGADOR
    if keyboard.up and jogador.top > 0:
        jogador.y -= VELOCIDADE_JOGADOR
    if keyboard.down and jogador.bottom < HEIGHT:
        jogador.y += VELOCIDADE_JOGADOR

    # O nível depende dos pontos; quanto maior, mais rápido caem os obstáculos.
    nivel = pontos // PONTOS_POR_NIVEL + 1
    velocidade = 3 + nivel
    if len(obstaculos) < min(nivel, MAX_OBSTACULOS):
        obstaculos.append(criar_obstaculo())

    # Obstáculos: descem, voltam ao topo e tiram 1 ponto se baterem no jogador.
    for obstaculo in obstaculos:
        obstaculo.y += velocidade
        if obstaculo.top > HEIGHT:
            reposicionar(obstaculo)
        if jogador.colliderect(obstaculo):
            pontos = max(0, pontos - 1)
            sounds.erro.play()
            reposicionar(obstaculo)

    # Estrela: dá 1 ponto e muda de lugar.
    if jogador.colliderect(estrela):
        pontos += 1
        sounds.ponto.play()
        estrela.pos = (randint(20, WIDTH - 20), randint(60, HEIGHT - 20))

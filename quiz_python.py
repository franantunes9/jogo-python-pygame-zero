import random

WIDTH = 700
HEIGHT = 450

perguntas = [
    {"texto": "Qual função mostra um texto na tela?",
     "opcoes": ["input()", "print()", "show()"],
     "certa": 1},
    {"texto": "Qual função lê o que a pessoa digita no terminal?",
     "opcoes": ["input()", "print()", "read()"],
     "certa": 0},
    {"texto": "O que faz o código x = 5?",
     "opcoes": ["Compara x com 5", "Mostra o número 5", "Guarda o valor 5 na variável x"],
     "certa": 2},
    {"texto": 'Qual é o tipo do valor "10" (com aspas)?',
     "opcoes": ["int", "float", "str"],
     "certa": 2},
    {"texto": "Qual destas linhas cria um dicionário?",
     "opcoes": ['["nome", "Ana"]', '{"nome": "Ana"}', '("nome": "Ana")'],
     "certa": 1},
    {"texto": "Qual palavra testa uma segunda condição depois do if?",
     "opcoes": ["elif", "else", "then"],
     "certa": 0},
    {"texto": "Qual operador exige que as duas condições sejam verdadeiras?",
     "opcoes": ["or", "and", "not"],
     "certa": 1},
    {"texto": "Qual loop repete enquanto uma condição for verdadeira?",
     "opcoes": ["for", "if", "while"],
     "certa": 2},
    {"texto": "Quantas vezes o print roda em: for i in range(3): print(i)?",
     "opcoes": ["3 vezes", "2 vezes", "4 vezes"],
     "certa": 0},
    {"texto": "Qual é o índice do primeiro item de uma lista?",
     "opcoes": ["1", "0", "-1"],
     "certa": 1},
    {"texto": "Qual palavra cria uma função em Python?",
     "opcoes": ["function", "func", "def"],
     "certa": 2},
    {"texto": "Em Pygame Zero, qual função desenha os objetos na tela?",
     "opcoes": ["draw()", "update()", "on_mouse_down()"],
     "certa": 0},
]

caixas = [Rect((100, 160 + i * 80), (500, 60)) for i in range(3)]

indice = 0
pontos = 0
fim = False
mensagem = ""

random.shuffle(perguntas)

def draw():
    screen.fill((30, 30, 60))
    if fim:
        screen.draw.text("Fim do quiz!", center=(350, 150), fontsize=60)
        screen.draw.text(f"Você acertou {pontos} de {len(perguntas)}", center=(350, 220), fontsize=36)
        screen.draw.text("Clique para jogar de novo", center=(350, 290), fontsize=28)
        return
    p = perguntas[indice]
    screen.draw.text(f"Pergunta {indice + 1} de {len(perguntas)}", topleft=(10, 10), fontsize=26)
    screen.draw.text(f"Pontos: {pontos}", topright=(690, 10), fontsize=26)
    screen.draw.text(p["texto"], center=(350, 90), fontsize=34, width=620)
    for i, caixa in enumerate(caixas):
        screen.draw.filled_rect(caixa, "royalblue")
        screen.draw.text(p["opcoes"][i], center=caixa.center, fontsize=30, color="white")
    if mensagem:
        screen.draw.text(mensagem, center=(350, 420), fontsize=28)

def on_mouse_down(pos):
    global indice, pontos, fim, mensagem
    if fim:
        indice = 0
        pontos = 0
        fim = False
        mensagem = ""
        random.shuffle(perguntas)
        return
    for i, caixa in enumerate(caixas):
        if caixa.collidepoint(pos):
            certa = perguntas[indice]["certa"]
            if i == certa:
                pontos += 1
                mensagem = "Correto!"
                sounds.ponto.play()
            else:
                mensagem = "Errado. A certa era: " + perguntas[indice]["opcoes"][certa]
                sounds.erro.play()
            indice += 1
            if indice >= len(perguntas):
                fim = True
                sounds.fim.play()
            break

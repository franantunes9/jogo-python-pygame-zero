# Jogos em Python com Pygame Zero

Projeto de estudo com dois jogos feitos em Python usando a biblioteca Pygame Zero: um jogo de coletar estrelas e um quiz sobre Python básico. Eu criei para praticar programação e para mostrar, de um jeito divertido, conceitos de quem está começando.

## Jogo 1: Caça-estrelas (`jogo.py`)

Mova o personagem com as setas do teclado e pegue as estrelas. Cada estrela vale 1 ponto. Bolas vermelhas caem e tiram 1 ponto se baterem em você.

O jogo começa numa tela de início (aperte Espaço), dura 30 segundos e guarda o recorde da sessão. A cada 5 pontos o nível sobe: os obstáculos caem mais rápido e aparece mais um, até o máximo de 5.

## Jogo 2: quiz de Python (`quiz_python.py`)

Quiz com 12 perguntas de múltipla escolha, respondidas com o mouse. Os temas são print e input, variáveis e tipos de dados, dicionários, condições (if, elif, else), operadores lógicos, loops for e while, listas, funções e o básico do Pygame Zero. O jogo mostra se você acertou, toca um efeito sonoro e mostra a pontuação no final.

## Como rodar

Instale o Python 3 e depois o Pygame Zero:

    pip install pgzero

Com o terminal aberto na pasta do projeto, rode um dos jogos:

    pgzrun jogo.py
    pgzrun quiz_python.py

## Conceitos de Python usados

- Variáveis e constantes, como `TEMPO_TOTAL` e `VELOCIDADE_JOGADOR`.
- Funções com `def`, como `iniciar()`, `contar_tempo()` e `criar_obstaculo()`.
- Listas (`obstaculos`) e dicionários (as perguntas do quiz).
- Condições com `if` e laços com `for`.
- Números aleatórios com `randint` e textos com f-strings.
- Estados do jogo (início, jogando e fim) controlados por uma variável.

## Como adicionar perguntas ao quiz

Cada pergunta é um dicionário dentro da lista `perguntas` do arquivo `quiz_python.py`. Exemplo:

    {"texto": "Qual função mostra um texto na tela?",
     "opcoes": ["input()", "print()", "show()"],
     "certa": 1},

O campo `certa` é a posição da resposta certa: 0 é a primeira opção, 1 é a segunda e 2 é a terceira.

## Como o código funciona

- `draw()` desenha tudo na tela a cada quadro.
- `update()` (no Caça-estrelas) atualiza posições, pontos, colisões e níveis.
- `on_mouse_down(pos)` (no quiz) roda a cada clique e verifica em qual caixa o clique caiu.
- `Actor` carrega uma imagem e já traz um retângulo para detectar colisões. `Rect` é só a caixa, sem imagem.
- `clock.schedule_interval` chama a função do tempo a cada segundo.

## Estrutura da pasta

    jogo.py              jogo Caça-estrelas
    quiz_python.py       quiz de Python
    images/              imagens do personagem, da estrela e do obstáculo
    sounds/              efeitos sonoros de acerto, erro e fim de jogo
    gerar_imagens.py     cria as imagens por código
    gerar_sons.py        cria os efeitos sonoros por código
    evolucao/            as versões 1 a 6 do projeto, em ordem

## Evolução do projeto

O `jogo.py` da raiz é a versão mais recente. A pasta `evolucao/` guarda as etapas anteriores, para mostrar como o jogo foi crescendo. Para rodar uma versão:

    cd evolucao
    pgzrun jogo5.py

- `jogo1.py`: quadrado que se move com as setas e coleta uma estrela.
- `jogo2.py`: tempo limite e tela de fim de jogo.
- `jogo3.py`: obstáculo que cai e tira pontos.
- `jogo4.py`: imagens no lugar dos quadrados, com `Actor`.
- `jogo5.py`: efeitos sonoros de acerto, erro e fim.
- `jogo6.py`: jogo de pegar o número pedido.

## Imagens e efeitos sonoros

Todas as imagens e todos os efeitos sonoros foram gerados pelo código (`gerar_imagens.py` e `gerar_sons.py`), sem usar arquivos de terceiros.

## Autora

Fran. Projeto de estudo em Python.

import math
import os
import struct
import wave

os.makedirs("sounds", exist_ok=True)
TAXA = 44100

def tom(freq, duracao, volume=0.4):
    n = int(TAXA * duracao)
    amostras = []
    for i in range(n):
        envelope = 1 - i / n
        valor = math.sin(2 * math.pi * freq * i / TAXA) * volume * envelope
        amostras.append(int(valor * 32767))
    return amostras

def salvar(nome, amostras):
    with wave.open("sounds/" + nome + ".wav", "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(TAXA)
        f.writeframes(struct.pack("<" + "h" * len(amostras), *amostras))

salvar("ponto", tom(660, 0.08) + tom(880, 0.12))
salvar("erro", tom(180, 0.3))
salvar("fim", tom(523, 0.15) + tom(392, 0.15) + tom(262, 0.35))
print("Sons criados em sounds/")

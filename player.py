from mapas import Maps
from map import draw_map, search_map
from memory import last_plays

Map = "Mario"
posicoes = search_map(Map)
tentativa = 1

def load_memory(memory):
    checkpoint = []
    if memory:
        steps = len(memory[-1]['steps'])
        for i in memory:
            if len(i['steps']) == steps:
                checkpoint.append(i['steps'])
        return checkpoint
    else:
        return checkpoint

def step(player, posicoes, attemp, tentativa):
    checkpoint = load_memory(last_plays)
    last_attemps_here = []
    if checkpoint:  # Verifica se checkpoint não está vazio
        for i in checkpoint:
            if isinstance(i, (list, tuple)) and len(i) > 0:
                last_attemps_here.append(i[-1])
            else:
                break

    for i in range(-1,2):
        if i not in last_attemps_here:
            escolha = i

    if escolha == posicoes[player+1]:
        attemp.append(escolha)
        player+=1
    else:
        last_plays.append({'attemp':tentativa,'steps':attemp})
        player = 0

while True:
    checkpoint = 0
    player = 0
    attemp = []
    if posicoes:
        while True:
            if player==len(posicoes):
                break
            else:
                step(player, posicoes, attemp, tentativa)
        if player==len(posicoes):
            print(f"Você venceu na tentativa {tentativa}")
            break   

    else:
        print(f"Mapa {Map} não foi encontrado")
        break


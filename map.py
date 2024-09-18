from random import randint

Maps = []

def creat_map(name, num_positions):
    positions = []
    for i in range(0,num_positions):
        positions.append(randint(-1,1))
    Map = {
        'nome':name,
        'posicoes':positions
    }
    Maps.append(Map)
    print(f"Mapa {name} criado!")

def search_map(name_map):
    for item in Maps:
        if item['nome'] == name_map:
           return item['posicoes']
    return None

def draw_map(name_map):
    positions = search_map(name_map)
    if positions:
        print("===" * len(positions))
        draw_line(positions,1,"___")
        draw_line(positions,0,"___")
        draw_line(positions,-1,"___")
        print("===" * len(positions))
    else:
        print("Mapa não encontrado")


def draw_line(positions, condition, line_type):
    for i in positions:
        if i == condition:
            print(line_type,end="")
        else:
            print(" " * len(line_type),end="")
    print()




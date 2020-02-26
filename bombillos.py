import copy
import numpy

qty_bulb_min = 9999999
all_matriz = []
numero_de_bombillos = []

matriz = []
# matriz_file = open("matriz_enana.txt", "r")

# Leer el caso de prueba
matriz_file = open("matriz.txt", "r")
# matriz_file = open("matriz_grande.txt", "r")
for line in matriz_file:
    matriz.append([number for number in line[:-1]])

def imprimir_matriz(matriz):
    for x_pos in range(0, len(matriz)-1):
        for y_pos in range(0, len(matriz[x_pos])-1):
            print(matriz[x_pos][y_pos], end='')
        print()

def contain_zeros(matriz):
    for row in matriz:
        if "0" in row:
            return True
    return False

def exist_matriz(matriz):
    global qty_bulb_min
    if matriz in all_matriz:
        return True
    matriz_in_numpy = numpy.matrix(matriz)
    qty_bulb = numpy.count_nonzero(matriz_in_numpy == 'B')
    all_matriz.append(matriz)
    numero_de_bombillos.append(qty_bulb)
    if qty_bulb < qty_bulb_min:
        qty_bulb_min = qty_bulb
    return False

def current_bulb_is_minor(matriz):
    global qty_bulb_min
    matriz_in_numpy = numpy.matrix(matriz)
    qty_bulb = numpy.count_nonzero(matriz_in_numpy == 'B')
    if qty_bulb < qty_bulb_min:
        return True
    return False

def alumbrar(matriz, x_pos, y_pos):
    matriz[x_pos][y_pos] = "B"
    x = x_pos -1
    y = y_pos - 1
    y_wall = False
    x_wall = False
    x_1 = x_pos + 1
    y_1 = y_pos + 1
    x_wall_1 = False
    y_wall_1 = False
    while(x > -1 or y > -1 or x_1 < len(matriz)):
        if y > -1 and not x_wall and matriz[x_pos][y] == "0":
            matriz[x_pos][y] = "L"
        y -= 1
        if y > -1 and matriz[x_pos][y] == "1":
            x_wall = True

        if x > -1 and not y_wall and matriz[x][y_pos] == "0":
            matriz[x][y_pos] = "L"
        x -= 1
        if x > -1 and matriz[x][y_pos] == "1":
            y_wall = True

        if x_1 < len(matriz) and matriz[x_1][y_pos] == "0" and not x_wall_1:
            matriz[x_1][y_pos] = "L"
        x_1 += 1
        if x_1 < len(matriz) and matriz[x_1][y_pos] == "1":
            x_wall_1 = True

        if y_1 < len(matriz[x_pos]) and matriz[x_pos][y_1] == "0" and not y_wall_1:
            matriz[x_pos][y_1] = "L"
        y_1 += 1
        if y_1 < len(matriz[x_pos]) and matriz[x_pos][y_1] == "1":
            y_wall_1 = True

def put_bulb(matriz):
    is_full = False
    for x_pos in range(len(matriz)):
        for y_pos in range(len(matriz[x_pos])):
            if matriz[x_pos][y_pos] == "0":

                matriz_cache = copy.deepcopy(matriz)
                alumbrar(matriz, x_pos, y_pos)

                if not contain_zeros(matriz):
                    exist_matriz(matriz)
                    is_full = True
                    break
                else:
                    if current_bulb_is_minor(matriz):
                        put_bulb(matriz)
                    matriz = matriz_cache
        if is_full:
            break

put_bulb(matriz)

for i in range(len(numero_de_bombillos)):
    if numero_de_bombillos[i] == qty_bulb_min:
        print(numero_de_bombillos[i])
        imprimir_matriz(matriz)
        print()

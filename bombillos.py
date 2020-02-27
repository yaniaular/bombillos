import copy
import numpy
import sys

# Aqui se guardara la menor cantidad de bombillos
# usados hasta el momento en una de las soluciones
# encontradas.
MINIMO_DE_BOMBILLOS = 9999999

# Se guardaran las posibles soluciones en forma de matriz
# para luego escoger la o las que usen menor cantidad
# de bombillos
POSIBLES_SOLUCIONES = set()

# Las matrices que ya fueron revisadas se guardan acá
REVISADAS = set()

# Aquí se guardará la matriz más óptima hasta el momento
MATRIZ_OPTIMA = []

# Leer el caso de prueba
MATRIZ = []
for line in open(sys.argv[1], "r"):
    MATRIZ.append([number for number in line[:-1]])


def imprimir_matriz(matriz):
    """ Imprime la matriz un poco decente.
    """
    for posx in range(len(matriz)):
        print(matriz[posx])


def contiene_ceros(matriz):
    """ Comprobar si la matriz todavia tiene
    habitaciones oscuras.
    """
    for fila in matriz:
        if "0" in fila:
            return True
    return False


def esta_revisada(matriz):
    if matriz in REVISADAS:
        return True
    return False


def guardar_matriz(matriz, matriz_in_numpy, matriz_tupla):
    """ La matriz que se recibe ya tiene todas
    las habitaciones alumbradas. Entonces, en este
    metodo se quiere guardar la matriz entre las
    posibles soluciones mas optimas. Para luego
    escoger la mejor.
    """
    global MINIMO_DE_BOMBILLOS
    global MATRIZ_OPTIMA
    if matriz_tupla in POSIBLES_SOLUCIONES:
        return True
    POSIBLES_SOLUCIONES.add(matriz_tupla)
    cantidad_bombillos = numpy.count_nonzero(matriz_in_numpy == 'B')
    # Se guarda cual ha sido la menor cantidad de bombillos
    # usados en una matriz con todas las habitaciones
    # iluminadas
    if cantidad_bombillos < MINIMO_DE_BOMBILLOS:
        MINIMO_DE_BOMBILLOS = cantidad_bombillos
        MATRIZ_OPTIMA = matriz
    return False


def chequear_bombillos(matriz_in_numpy):
    """ Si la cantidad de bombillos usados
    en la matriz que recibimos es mayor
    a la mejor solucion encontrada hasta ahora
    entonces se retorna False para que no se siga
    recorriendo esa matriz
    """
    global MINIMO_DE_BOMBILLOS
    cantidad_bombillos = numpy.count_nonzero(matriz_in_numpy == 'B')
    if cantidad_bombillos < MINIMO_DE_BOMBILLOS:
        return True
    return False


def alumbrar_habitaciones(matriz, posx, posy):
    """ Al encontrar una habitacion sin bombillo
    se procede a colocar uno y alumbrar las habitaciones
    que pueda alcanzar a alumbrar.
    """
    matriz[posx][posy] = "B"
    posx_iter = posx - 1
    posy_iter = posy - 1
    y_pared_1 = False
    x_pared_1 = False
    posx_iter_2 = posx + 1
    posy_iter_2 = posy + 1
    x_pared_2 = False
    y_pared_2 = False
    # Sorry si no se entiende este codigo, la verdad, antes eran
    # 4 ciclos for, pero decidi hacerlo en un while para mejorar
    # los tiempos. Estoy alumbrando las habitaciones y si ya
    # llegue al final en alguna direccion, entonces marco los booleanos
    # como que ya llegue a la pared para que ya no siga recorriendo
    # en esa direccion
    while(posx_iter > -1 or posy_iter > -1 or posx_iter_2 < len(matriz)):
        if posy_iter > -1 and not x_pared_1 and matriz[posx][posy_iter] == "0":
            matriz[posx][posy_iter] = "L"
        if posy_iter > -1 and matriz[posx][posy_iter] == "1":
            x_pared_1 = True
        posy_iter -= 1

        if posx_iter > -1 and not y_pared_1 and matriz[posx_iter][posy] == "0":
            matriz[posx_iter][posy] = "L"
        if posx_iter > -1 and matriz[posx_iter][posy] == "1":
            y_pared_1 = True
        posx_iter -= 1

        if (posx_iter_2 < len(matriz) and
                matriz[posx_iter_2][posy] == "0" and not x_pared_2):
            matriz[posx_iter_2][posy] = "L"
        if posx_iter_2 < len(matriz) and matriz[posx_iter_2][posy] == "1":
            x_pared_2 = True
        posx_iter_2 += 1

        if (posy_iter_2 < len(matriz[posx]) and
                matriz[posx][posy_iter_2] == "0" and not y_pared_2):
            matriz[posx][posy_iter_2] = "L"
        if (posy_iter_2 < len(matriz[posx]) and
                matriz[posx][posy_iter_2] == "1"):
            y_pared_2 = True
        posy_iter_2 += 1


def buscar_bombillos_optimos(matriz):
    """ Backtracking donde se revisa todas las soluciones
    posibles para encontrar la solucion optima. Cada vez
    que se encuentra una habitacion oscura, entonces,
    se procede a alumbrarla y a seguir revisando donde
    hay habitaciones oscuras para alumbrarlas hasta que
    todo este iluminado e ir guardando las soluciones mas
    optimas.
    """
    global REVISADAS
    revisada = False
    for posx in range(len(matriz)):
        for posy in range(len(matriz[posx])):
            if matriz[posx][posy] == "0":
                # Se guarda la matriz antes de alumbrarla
                # para que al seguir con el ciclo, se siga
                # con la matriz sin alumbrar
                matriz_cache = copy.deepcopy(matriz)
                alumbrar_habitaciones(matriz, posx, posy)
                matriz_tupla = tuple([tuple(habitacion) for habitacion in matriz])
                matriz_in_numpy = numpy.matrix(matriz)
                if not contiene_ceros(matriz_tupla):
                    # Si no hay ceros, guardamos la solucion
                    # encontrada.
                    guardar_matriz(matriz, matriz_in_numpy, matriz_tupla)
                elif chequear_bombillos(matriz_in_numpy):
                    # Si la matriz ha usado menos bombillos
                    # que la solucion mas optima hasta el
                    # momento, entonces seguimos recorriendo
                    if not esta_revisada(matriz_tupla):
                        buscar_bombillos_optimos(matriz)
                        REVISADAS.add(matriz_tupla)
                    else:
                        revisada = True
                matriz = matriz_cache
            if revisada:
                break
        if revisada:
            break

# Llamada al backtracking
buscar_bombillos_optimos(MATRIZ)

# Imprimir todas las soluciones con la menor
# cantidad de bombillos
print("B: Las habitaciones que tienen bombillo.\n"
      "L: Las habitaciones que tienen luz por algun bombillo.\n"
      "1: Las habitaciones con paredes.\n")

print("Bombillos usados: ", MINIMO_DE_BOMBILLOS)
for item in MATRIZ_OPTIMA:
    for item2 in item:
        if item2 == "1":
            sys.stdout.write("\033[1;30;40m%s\033[m" % item2)
        elif item2 == "L":
            sys.stdout.write("\033[2;30;43m%s\033[m" % item2)
        else:
            sys.stdout.write("\033[1;33;43m%s\033[m" % item2)
    print()

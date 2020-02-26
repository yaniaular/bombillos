import copy
import numpy

all_matrix = []
all_matrix_number = []

all_matrix_checked = []

matrix = []
# matrix_file = open("matriz_enana.txt", "r")
matrix_file = open("matriz.txt", "r")
# matrix_file = open("matriz_grande.txt", "r")
for line in matrix_file:
    matrix.append([number for number in line[:-1]])

def print_matrix(matrix):
    for x_pos in range(0, len(matrix)-1):
        for y_pos in range(0, len(matrix[x_pos])-1):
            print(matrix[x_pos][y_pos], end='')
        print("\n")

def contain_zeros(matrix):
    for row in matrix:
        if "0" in row:
            return True
    return False

def exist_matrix(matrix):
    if matrix in all_matrix:
        return True
    print_matrix(matrix)
    print("*************")
    matrix_in_numpy = numpy.matrix(matrix)
    qty_bulb = numpy.count_nonzero(matrix_in_numpy == 'B')
    all_matrix.append(matrix)
    all_matrix_number.append(qty_bulb)
    return False


def was_checked(posx, posy, matrix):
    matrix_in_numpy = numpy.matrix(matrix)
    for m in all_matrix_checked:
        if m[0] == posx and m[1] == posy and (matrix_in_numpy == m[2]).all():
            return True
    return False

def save_like_checked(posx, posy, matrix):
    all_matrix_checked.append((posx, posy, matrix))

def alumbrar(matrix, x_pos, y_pos):
    matrix[x_pos][y_pos] = "B"
    x = x_pos -1
    y = y_pos - 1
    y_wall = False
    x_wall = False
    x_1 = x_pos + 1
    y_1 = y_pos + 1
    x_wall_1 = False
    y_wall_1 = False
    while(x > -1 or y > -1 or x_1 < len(matrix)):
        if y > -1 and not x_wall and matrix[x_pos][y] == "0":
            matrix[x_pos][y] = "L"
        y -= 1
        if y > -1 and matrix[x_pos][y] == "1":
            x_wall = True

        if x > -1 and not y_wall and matrix[x][y_pos] == "0":
            matrix[x][y_pos] = "L"
        x -= 1
        if x > -1 and matrix[x][y_pos] == "1":
            y_wall = True

        if x_1 < len(matrix) and matrix[x_1][y_pos] == "0" and not x_wall_1:
            matrix[x_1][y_pos] = "L"
        x_1 += 1
        if x_1 < len(matrix) and matrix[x_1][y_pos] == "1":
            x_wall_1 = True

        if y_1 < len(matrix[x_pos]) and matrix[x_pos][y_1] == "0" and not y_wall_1:
            matrix[x_pos][y_1] = "L"
        y_1 += 1
        if y_1 < len(matrix[x_pos]) and matrix[x_pos][y_1] == "1":
            y_wall_1 = True

def put_bulb(matrix):
    is_full = False
    for x_pos in range(len(matrix)):
        for y_pos in range(len(matrix[x_pos])):
            if matrix[x_pos][y_pos] == "0":

                matrix_cache = copy.deepcopy(matrix)
                alumbrar(matrix, x_pos, y_pos)

                if not contain_zeros(matrix):
                    exist_matrix(matrix)
                    is_full = True
                    break
                else:
                    put_bulb(matrix)
                    matrix = matrix_cache
        if is_full:
            break

put_bulb(matrix)
from pprint import pprint
for i in range(len(all_matrix_number)):
    pprint(all_matrix_number[i])
    pprint(all_matrix[i])

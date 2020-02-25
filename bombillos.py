import copy
import numpy

all_matrix = []
all_matrix_checked = []

matrix = []
matrix_file = open("matriz_grande.txt", "r")
# matrix_file = open("matriz.txt", "r")
for line in matrix_file:
    matrix.append([number for number in line[:-1]])

def print_matrix(matrix):
    for x_pos in range(0, len(matrix)-1):
        for y_pos in range(0, len(matrix[x_pos])-1):
            print(matrix[x_pos][y_pos], end='')
        print("\n")

def contain_zeros(matrix):
    matrix_in_numpy = numpy.matrix(matrix)
    if numpy.count_nonzero(matrix_in_numpy == '0') == 0:
        return False
    return True

def exist_matrix(matrix):
    matrix_in_numpy = numpy.matrix(matrix)
    for m in all_matrix:
        if (matrix_in_numpy == m[1]).all():
            return True
    qty_bulb = numpy.count_nonzero(matrix_in_numpy == 'B')
    all_matrix.append((qty_bulb, matrix_in_numpy))
    return False

def already_checked(posx, posy, matrix):
    matrix_in_numpy = numpy.matrix(matrix)
    for m in all_matrix_checked:
        if m[0] == posx and m[1] == posy and (matrix_in_numpy == m[2]).all():
            return True
    all_matrix_checked.append((posx, posy, matrix_in_numpy))
    return False

def put_bulb(matrix):
    position = False
    for x_pos in range(len(matrix)):
        for y_pos in range(len(matrix[x_pos])):
            if matrix[x_pos][y_pos] == "0":

                matrix_cache = copy.deepcopy(matrix)
                if already_checked(x_pos, y_pos, matrix):
                    continue

                matrix[x_pos][y_pos] = "B"
                for fill in range(y_pos+1, len(matrix[x_pos])):
                    if matrix[x_pos][fill] == "0":
                        matrix[x_pos][fill] = "L"
                    elif matrix[x_pos][fill] == "1":
                        break

                for fill in range(y_pos-1, -1, -1):
                    if matrix[x_pos][fill] == "0":
                        matrix[x_pos][fill] = "L"
                    elif matrix[x_pos][fill] == "1":
                        break

                for fill in range(x_pos+1, len(matrix)):
                    if matrix[fill][y_pos] == "0":
                        matrix[fill][y_pos] = "L"
                    elif matrix[fill][y_pos] == "1":
                        break

                for fill in range(x_pos-1, -1, -1):
                    if matrix[fill][y_pos] == "0":
                        matrix[fill][y_pos] = "L"
                    elif matrix[fill][y_pos] == "1":
                        break

                if x_pos == len(matrix)-1 and y_pos == len(matrix[x_pos])-1 and not contain_zeros(matrix) and not exist_matrix(matrix):
                    print("************************************")
                    # print_matrix(matrix)

                put_bulb(matrix)
                matrix = matrix_cache

put_bulb(matrix)

from pprint import pprint
print(pprint(all_matrix))

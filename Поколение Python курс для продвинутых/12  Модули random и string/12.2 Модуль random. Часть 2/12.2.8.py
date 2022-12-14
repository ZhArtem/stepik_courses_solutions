# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).

# Примечание. Выводить содержимое матрицы не нужно.


import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
l = []
for row in matrix:
    for num in row:
        l.append(num)
random.shuffle(l)
n, m = len(matrix[0]), len(matrix)
matrix = [[l[i + j * m] for i in range(m)] for j in range(n)]


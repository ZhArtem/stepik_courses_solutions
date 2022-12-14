# Снежинка
# На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её символами . . Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.

# Формат входных данных
# На вход программе подается нечетное натуральное число n, \, (n \ge 3)n,(n≥3) — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.

# Тестовые данные 🟢
# Sample Input 1:

# 5
# Sample Output 1:

# * . * . *
# . * * * .
# * * * * *
# . * * * .
# * . * . *
# Sample Input 2:

# 7
# Sample Output 2:

# * . . * . . *
# . * . * . * .
# . . * * * . .
# * * * * * * *
# . . * * * . .
# . * . * . * .
# * . . * . . *
# Sample Input 3:

# 11
# Sample Output 3:

# * . . . . * . . . . *
# . * . . . * . . . * .
# . . * . . * . . * . .
# . . . * . * . * . . .
# . . . . * * * . . . .
# * * * * * * * * * * *
# . . . . * * * . . . .
# . . . * . * . * . . .
# . . * . . * . . * . .
# . * . . . * . . . * .
# * . . . . * . . . . *


n = int(input())
matrix = [['.'] * n for _ in range(n)]
center = n // 2
for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i == center or j == center:
            matrix[i][j] = '*'
        print(matrix[i][j], end=' ')
    print()

    
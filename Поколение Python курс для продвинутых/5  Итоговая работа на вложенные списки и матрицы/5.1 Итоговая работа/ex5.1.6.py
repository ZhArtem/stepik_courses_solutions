#  Латинский квадрат 🌶️
# Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

# Тестовые данные 🟢
# Sample Input 1:

# 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# Sample Output 1:

# YES
# Sample Input 2:

# 3
# 1 2 3
# 3 2 1
# 2 3 4
# Sample Output 2:

# NO


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = 'YES'
matrix2 = [[0] * n for _ in range(n)]
for i in range(n):
    if sorted(matrix[i]) != list(range(1, n + 1)):
      flag = 'NO'
      break
    for j in range(n):
      matrix2[j][-i - 1] = matrix[i][j]
for row in matrix2:
    if sorted(row) != [*range(1, n + 1)]:
        flag = 'NO'
        break
print(flag)

# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.

# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

# Тестовые данные 🟢
# Sample Input 1:

# 2 2
# 1 2
# 3 2

# 2 2
# 3 2
# 1 1
# Sample Output 1:

# 5 4
# 11 8
# Sample Input 2:

# 3 2
# 2 5
# 6 7
# 1 8

# 2 3
# 1 2 1
# 0 1 0
# Sample Output 2:

# 2 9 2
# 6 19 6
# 1 10 1
# Sample Input 3:

# 3 3
# 2 4 6
# 1 3 5
# 0 4 8

# 3 3
# 6 3 1
# 9 6 3
# 0 2 0
# Sample Output 3:

# 48 42 14
# 33 31 10
# 36 40 12


n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(m)]
matrix3 = [[0] * k for _ in range(n)]

for i in range(n):
  for j in range(k):
    for q in range(m):
      matrix3[i][j] += matrix1[i][q] * matrix2[q][j]
  print(*matrix3[i])

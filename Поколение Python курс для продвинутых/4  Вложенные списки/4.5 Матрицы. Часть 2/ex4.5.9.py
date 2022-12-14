# Магический квадрат 🌶️
# Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n 
# 2
#   так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

# Тестовые данные 🟢
# Sample Input 1:

# 3
# 8 1 6
# 3 5 7
# 4 9 2
# Sample Output 1:

# YES
# Sample Input 2:

# 3
# 8 2 6
# 3 5 7
# 4 9 1
# Sample Output 2:

# NO
# Sample Input 3:

# 3
# 4 9 2
# 3 5 7
# 8 1 6
# Sample Output 3:

# YES


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

def ismagic(matrix):
  all = []
  total = sum(matrix[0])
  for row in matrix:
    if sum(row) != total:
      return False
    all.extend(row)
  for i in range(1, n*n + 1):
    if i not in all:
      return False
  counter1, counter2, counter3 = 0, 0, 0
  for i in range(n):
    counter3 = 0
    counter1 += matrix[i][i]
    counter2 += matrix[i][n - i - 1]
    for j in range(n):
      counter3 += matrix[i][j]
    if counter3 != total:
      return False
  if counter1 != total or counter2 != total:
    return False
  return True

print('YES' if ismagic(matrix) else 'NO')
    

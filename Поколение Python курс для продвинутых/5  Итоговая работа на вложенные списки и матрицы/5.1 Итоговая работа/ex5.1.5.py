# Симметричная матрица
# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.

# Тестовые данные 🟢
# Sample Input 1:

# 3
# 0 3 10
# 4 9 3
# 7 4 0
# Sample Output 1:

# YES
# Sample Input 2:

# 3
# 0 1 2
# 1 2 7
# 2 3 4
# Sample Output 2:

# NO
# Sample Input 3:

# 2
# 1 2
# 3 4
# Sample Output 3:

# NO
# Sample Input 4:

# 2
# 4 2
# 3 4
# Sample Output 4:

# YES


n = int(input())
matrix = [input().split() for _ in range(n)]
flag = 'YES'
for i in range(n):
  for j in range(n):
    if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
      flag = 'NO'
      break
  if flag == 'NO':
    break
print(flag)


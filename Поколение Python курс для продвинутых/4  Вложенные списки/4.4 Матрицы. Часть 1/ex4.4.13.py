# Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

# Примечание. Элементы диагоналей также учитываются.

# Тестовые данные 🟢
# Sample Input 1:

# 3
# 1 4 5
# 6 7 8
# 1 1 6
# Sample Output 1:

# 8
# Sample Input 2:

# 4
# 0 1 4 6
# 0 0 2 5
# 0 0 0 7
# 0 0 0 0
# Sample Output 2:

# 7
# Sample Input 3:

# 2
# 6 0
# 7 9
# Sample Output 3:

# 9


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
mx = matrix[0][0]
for i in range(n):
  for j in range(n):
    if j <= i <= n - j - 1 or n - j- 1 <= i <= j:
      if matrix[i][j] > mx:
        mx = matrix[i][j]
print(mx)
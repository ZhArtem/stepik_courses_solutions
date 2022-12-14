# Заполнение змейкой
# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "змейкой" в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Тестовые данные 🟢
# Sample Input 1:

# 3 5
# Sample Output 1:

# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15
# Sample Input 2:

# 5 5
# Sample Output 2:

# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
# Sample Input 3:

# 2 2
# Sample Output 3:

# 1  2
# 4  3


n, m = [int(i) for i in input().split()]
matrix = [[1 + i * m + j for j in range(m)] for i in range(n)]
for i in range(1, n, 2):
  matrix[i].reverse()
for row in matrix:
  for dig in row:
    print(str(dig).ljust(3), end='')
  print()
  
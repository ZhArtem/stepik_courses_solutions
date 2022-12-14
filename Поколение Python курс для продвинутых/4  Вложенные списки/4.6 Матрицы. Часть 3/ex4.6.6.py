#     Заполнение 4
# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

# Тестовые данные 🟢
# Sample Input 1:

# 5
# Sample Output 1:

# 1  1  1  1  1
# 0  1  1  1  0
# 0  0  1  0  0
# 0  1  1  1  0
# 1  1  1  1  1
# Sample Input 2:

# 7
# Sample Output 2:

# 1  1  1  1  1  1  1
# 0  1  1  1  1  1  0
# 0  0  1  1  1  0  0
# 0  0  0  1  0  0  0
# 0  0  1  1  1  0  0
# 0  1  1  1  1  1  0
# 1  1  1  1  1  1  1
# Sample Input 3:

# 4
# Sample Output 3:

# 1  1  1  1
# 0  1  1  0
# 0  1  1  0
# 1  1  1  1


n = int(input())
matrix = [['1' if i <= j <= n - i - 1 or n - i - 1 <= j <= i else '0' for j in range(n)] for i in range(n)]
for row in matrix:
  for num in row:
    print(num.ljust(3), end='')
  print()

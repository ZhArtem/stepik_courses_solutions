# Треугольник Паскаля 1 🌶️
# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

# Формат входных данных
# На вход программе подается число n \, (n \ge 0)n (n≥0).

# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.

# Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает соответствующую строку треугольника Паскаля.

# Примечание 2. Графическая иллюстрация формирования треугольника Паскаля.



# Примечание 3. Подробнее прочитать о треугольнике Паскаля можно тут. 

# Тестовые данные 🟢
# Sample Input 1:

# 0
# Sample Output 1:

# [1]
# Sample Input 2:

# 1
# Sample Output 2:

# [1, 1]
# Sample Input 3:

# 2
# Sample Output 3:

# [1, 2, 1]
# Sample Input 4:

# 3
# Sample Output 4:

# [1, 3, 3, 1]


n = int(input())
l = [[int('1') for j in range(1, i + 1)] for i in range(1, n + 2)]
for i in range(2, n + 1):
  for j in range(1, i):
    l[i][j] = l[i - 1][j - 1] + l[i - 1][j]
print(l[n])

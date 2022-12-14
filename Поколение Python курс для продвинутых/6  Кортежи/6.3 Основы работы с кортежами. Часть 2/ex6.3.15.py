# Последовательность Трибоначчи
# Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.

# Формат входных данных
# На вход программе подается одно число n\,  (n \le 100)n (n≤100) – количество членов последовательности.

# Формат выходных данных
# Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

# Примечание. Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
# 1, \, 1,  \, 1, \,  3, \,  5, \,  9, \,  17, \,  31, \,  57, \,  105 \ldots
# 1,1, 1, 3, 5, 9, 17, 31, 57, 105 …

# Тестовые данные 🟢
# Sample Input 1:

# 10
# Sample Output 1:

# 1 1 1 3 5 9 17 31 57 105
# Sample Input 2:

# 1
# Sample Output 2:

# 1
# Sample Input 3:

# 2
# Sample Output 3:

# 1 1


n = int(input())
t1, t2, t3 = 1, 1, 1
for i in range(n):
  print(t1, end=' ')
  t1, t2, t3 = t2, t3, t1 + t2 + t3

  
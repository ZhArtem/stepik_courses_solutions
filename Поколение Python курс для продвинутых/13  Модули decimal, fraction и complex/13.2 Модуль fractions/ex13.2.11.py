# Сумма дробей 2
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 
# \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \dfrac{1}{4!} + \ldots + \dfrac{1}{n!}
# 1!
# 1
# ​
#  + 
# 2!
# 1
# ​
#  + 
# 3!
# 1
# ​
#  + 
# 4!
# 1
# ​
#  +…+ 
# n!
# 1
# ​
 

# Формат входных данных
# На вход программе подается натуральное число nn.

# Формат выходных данных
# Программа должна вывести ответ на задачу.

# Примечание 1. Результирующая дробь должна быть несократимой.

# Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.

# Тестовые данные 🟢
# Sample Input 1:

# 1
# Sample Output 1:

# 1
# Sample Input 2:

# 2
# Sample Output 2:

# 3/2
# Sample Input 3:

# 3
# Sample Output 3:

# 5/3
# Sample Input 4:

# 4
# Sample Output 4:

# 41/24
# Sample Input 5:

# 5
# Sample Output 5:

# 103/60


from fractions import Fraction
from math import factorial

print(sum(Fraction(1, factorial(i)) for i in range(1, int(input()) + 1)))





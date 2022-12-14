# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств:

# \begin{cases} -2\le x \le 2\\ -2\le y \le 2\\ x^3+y^4 + 2 \ge 0\\ 3x+y^2 \le 2 \end{cases}
# ⎩
# ⎨
# ⎧
# ​
  
# −2≤x≤2
# −2≤y≤2
# x 
# 3
#  +y 
# 4
#  +2≥0
# 3x+y 
# 2
#  ≤2
# ​
 


import random

n = 10**6       # количество испытаний
k = 0
s0 = 16
for i in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:
        k += 1
s = k / n * s0
print(k / n * s0)



# Внутри шара
# На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (xx), ординат (yy) и аппликат (zz) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными координатами внутри либо на поверхности шара с центром в начале координат и радиусом R = 2R =2.

# Формат входных данных
# На вход программе подаются три строки текста с вещественными числами, разделенными символом пробела – абсциссы, ординаты и аппликаты точек в трехмерной системе координат.

# Формат выходных данных
# Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара и False, если вне.

# Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

# Примечание 2. Уравнение поверхности шара (сферы) имеет вид x^2+y^2+z^2 = R^2x 
# 2
#  +y 
# 2
#  +z 
# 2
#  =R 
# 2
#  .

# Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

# Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.

# Примечание 5. Указанный шар имеет вид:



# Тестовые данные 🟢
# Sample Input 1:

# 0.0 1.0 2.0
# 0.0 0.0 1.1
# 0.0 1.0 1.5
# Sample Output 1:

# False
# Sample Input 2:

# 0.0 0.0
# 1.5 0.0
# 1.1 1.1
# Sample Output 2:

# True
# Sample Input 3:

# 0.637 -0.411 -0.247 1.658 0.061
# -0.78 -1.374 0.762 0.306 -0.614
# -1.317 -0.444 -0.572 -0.341 0.295
# Sample Output 3:

# True


abscissas = [float(i) for i in input().split()]
ordinates = [*map(float, input().split())]
applicates = [*map(float, input().split())]
dots = zip(abscissas, ordinates, applicates)
print(all(map(lambda dot: dot[0]**2 + dot[1]**2 + dot[2]**2 <= 4, dots)))

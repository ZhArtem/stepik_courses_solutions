# Хороший пароль
# Хороший пароль по условиям этой задачи состоит как минимум из 77 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

# Формат входных данных
# На вход программе подаётся одна строка текста.

# Формат выходных данных
# Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.

# Тестовые данные 🟢
# Sample Input 1:

# abcABC9
# Sample Output 1:

# YES
# Sample Input 2:

# abAB34
# Sample Output 2:

# NO
# Sample Input 3:

# DFSDFSDFSDsdfjsdfnsm
# Sample Output 3:

# NO


s = input()
print('YES' if len(s) >= 7 and all([any([c.isdigit() for c in s]), any([c.isupper() for c in s]), any([c.islower() for c in s])]) else 'NO')





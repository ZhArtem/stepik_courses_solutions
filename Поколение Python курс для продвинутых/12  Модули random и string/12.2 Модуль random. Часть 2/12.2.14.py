# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

# Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

# Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
# Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.

# Для отладки кода 🟡
# Тестовые данные 🟢
# Sample Input 1:

# 9
# 7
# Sample Output 1:

# iHnPg7q
# Njj9m3N
# tQ9v5ut
# 6qPZ3tV
# 6gVScya
# kU8ncAY
# 5CKX9Da
# UTQRve4
# FyRe8NN
# Sample Input 2:

# 15
# 3
# Sample Output 2:

# 7qB
# 4Wp
# r2V
# Zq3
# Y5q
# iL3
# M9v
# 7Hy
# 8tW
# 5Jz
# a4K
# 3Kt
# cN6
# 7Tk
# Pg5
# Sample Input 3:

# 20
# 4
# Sample Output 3:

# 4buF
# Ci32
# 4zXK
# p3By
# pQs9
# aP8n
# 7tGb
# QV2e
# 98Eu
# 8BbG
# R9sr
# c8Uv
# tt4H
# 66Cq
# J8mW
# kCm8
# k8PH
# 7EWp
# DH4q
# E5wF


import random
import string

LETTERS = {
    'up': [i for i in string.ascii_uppercase if i not in 'OI'],
    'low': [i for i in string.ascii_lowercase if i not in 'ol'],
    'digs': list(string.digits[2:])
}

def generate_password(length):
    s = LETTERS['up'] + LETTERS['low'] + LETTERS['digs']
    password = [random.choice(LETTERS[key]) for key in LETTERS] + [random.choice(s) for _ in range(length - 3)]
    random.shuffle(password)
    return ''.join(password)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


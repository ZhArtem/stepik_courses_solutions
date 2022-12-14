# Камень, ножницы, бумага, ящерица, Спок 🌶️
# Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

# Формат выходных данных
# Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

# Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.



# Тестовые данные 🟢
# Sample Input 1:

# ящерица
# камень
# Sample Output 1:

# Руслан
# Sample Input 2:

# Спок
# камень
# Sample Output 2:

# Тимур
# Sample Input 3:

# ножницы
# ножницы
# Sample Output 3:

# ничья


t, r = input(), input()
a = ['камень', 'бумага', 'ножницы', 'Спок', 'ящерица']
b = ['ничья', 'Руслан', 'Тимур']
dist = (a.index(t) - a.index(r)) % len(a)
print(b[dist and dist % 2 + 1])


# или

# t, r = input(), input()
# a = ['камень', 'бумага', 'ножницы', 'Спок', 'ящерица']
# print('ничья' if t == r else 'Руслан' if (a.index(t) - a.index(r)) in [2, 4, -1, -3] else 'Тимур')
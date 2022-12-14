# Длинные строки
# Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

# Примечание 2. Используйте менеджер контекста 🙂.

# Примечание 3. Если бы файл lines.txt содержал строки:

# One
# Twenty one
# Two
# Twenty two
# то результатом будет:

# Twenty one
# Twenty two
# Примечание 4. Указанный файл можно скачать по ссылке. 


with open('lines.txt') as f:
  lines = [i.strip() for i in f.readlines()]
  print(*filter(lambda x: len(x) == len(max(lines, key=len)), lines), sep='\n')





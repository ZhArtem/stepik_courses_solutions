# Входная строка
# Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него считанную строку текста.

# Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.


with open('output.txt', 'w') as f:
  print(input(), file=f)





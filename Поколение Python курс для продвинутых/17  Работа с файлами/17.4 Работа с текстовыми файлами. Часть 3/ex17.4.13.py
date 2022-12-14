# Конкатенация файлов 🌶️
# На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

# Формат входных данных
# На вход программе подается натуральное число nn и nn строк названий существующих файлов.

# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

# Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.


files = [input() for _ in range(int(input()))]
for file in files:
    with open(file) as file_inp, open('output.txt', 'a') as file_out:
        print(file_inp.read(), file=file_out, end='')

        
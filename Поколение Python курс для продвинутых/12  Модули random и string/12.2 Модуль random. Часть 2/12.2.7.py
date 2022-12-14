# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

# Примечание 1. Пример правильного (неправильного) индекса Латверии:

# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.

# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.


import random, string
def letter():
    return string.ascii_uppercase[random.randrange(len(string.ascii_uppercase))]
def number():
    return str(random.randrange(100))
def generate_index():
    return letter() + letter() + number() + '_' + number() + letter() + letter()
    
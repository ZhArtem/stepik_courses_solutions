# Покупки в интернет-магазине 🌶️
# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.

# Формат входных данных
# На вход программе подается число nn — количество строк в базе данных о продажах интернет-магазина. Далее следует nn строк с записями вида покупатель товар количество, где покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара (натуральное число).

# Формат выходных данных
# Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя — двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.

# Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает суммарное количество товара по данной позиции.

# Тестовые данные 🟢
# Sample Input 1:

# 5
# Руслан Пирог 1
# Тимур Карандаш 5
# Руслан Линейка 2
# Тимур Тетрадь 12
# Руслан Хлеб 3
# Sample Output 1:

# Руслан:
# Линейка 2
# Пирог 1
# Хлеб 3
# Тимур:
# Карандаш 5
# Тетрадь 12
# Sample Input 2:

# 7
# Вячеслав Ручка 1
# Филипп Ручка 1
# Виктория Перо 3
# Вячеслав Линейка 4
# Виктория Тетрадь 7
# Вячеслав Ручка 29
# Филипп Циркуль 1
# Sample Output 2:

# Виктория:
# Перо 3
# Тетрадь 7
# Вячеслав:
# Линейка 4
# Ручка 30
# Филипп:
# Ручка 1
# Циркуль 1
# Sample Input 3:

# 5
# Максим Пирог 5
# Максим Печенье 55
# Максим Свеча 3
# Максим Тарелки 10
# Максим Торт 1
# Sample Output 3:

# Максим:
# Печенье 55
# Пирог 5
# Свеча 3
# Тарелки 10
# Торт 1


d = {}
for i in range(int(input())):
    name, product, num = input().split()
    num = int(num)
    if name not in d:
        d[name] = {product: num}
    else:
        if product in d[name]:
            d[name][product] = d[name][product] + num
        else:
            d[name].update({product: num})

for name in sorted(d):
    print(name + ':')
    for k, v in sorted(d[name].items()):
        print(k, v)

        
# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

# Тестовые данные 🟢
# Sample Input 1:

# 12.1244354689
# Sample Output 1:

# 10
# Sample Input 2:

# 0.1244354689
# Sample Output 2:

# 9


from decimal import *

num = Decimal(input())
digits = num.as_tuple().digits
print(max(digits) if -num.as_tuple().exponent == len(digits) else sum((max(digits), min(digits))))

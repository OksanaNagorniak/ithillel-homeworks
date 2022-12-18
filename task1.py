# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

# Решение:

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('yes')
else:
    print('no')

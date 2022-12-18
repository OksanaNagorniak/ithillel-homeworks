# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

# Решение:

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a>b and a>c:
    print ("a=max")
elif b>a and b>c:
    print ("b=max")
elif c>a and c>b:
    print ("c=max")

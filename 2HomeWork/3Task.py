#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

value_N = int(input("Введите число N: "))

degree_value_two = 0

if (value_N ==0 or value_N ==1):
    print(f"Целой степени двойки меньше {value_N} не существует")
    exit(0)

for i in range(0, value_N):
    number = 2
    number = number ** i
    if (number < value_N):
        print(number)
    else:
        exit(0)

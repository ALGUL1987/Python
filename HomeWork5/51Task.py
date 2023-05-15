# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(x, y):
    if x == 0:
        return 0
    elif x == 1 or y == 0:
        return 1
    elif y == 1:
        return x
    return x*degree(x,y-1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(degree(A, B))

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def easy(n,div=2):
    if div==n//2+1:
        print("Yes")
    elif n%div==0:
        print("No")
    else:
        easy(n, div+1)

value = int(input("Введите число: "))
easy(value)

def is_simple(num: int) -> bool:
    if num in [1,2]: # проверка -> если 1 или 2 то число простое
        return True
    elif num%2==0: # проверка -> если число четное то оно не простое
        return False
    else:
        for i in range (3, num//2+1,2): # условие -> от числа 3 до половины числа с шагом 2
            if num%i==0:
                return False
    return True

print(is_simple(value))

    
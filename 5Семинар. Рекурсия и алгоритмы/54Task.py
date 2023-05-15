# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def value (n: int)-> None:
#     print(n, end=' ')
#     if n == 0:
#         return
#     else:
#         value(n-1)

# X = int(input("Введите число: "))
# value(X)

def value (n: int, s='')-> str:
    if n != 0:
        return value(n-1,s+str(n)+' ')
    else:
        return s

X = int(input("Введите число: "))
print(value(X))

def reverse(n: int):
    if n==1:
        return n
    else:
        return f"{n} {reverse(n-1)}"
    
print(reverse(X))

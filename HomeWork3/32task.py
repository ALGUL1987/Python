# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random, sys

N = int(input("Введите размер списка: "))
X = int(input("Введите искомое число: "))
list = []
step = 1
nearby_value = set()
count = 0

for i in range(N):
    list.append(random.randint(0,10))
    if (list[i]+step == X or list[i]-step == X):
        nearby_value.add(list[i])

for i in range(N):
    if (list[i]+1 == X or list[i]-1 == X):
        count+=1

if (count==0):
    print(list)
    print(f"Ближайшиx чисел с шагом {step} к Х={X} нет в списке")
    sys.exit()

print(f"Длина списка -> {N}")
print(list)
print(f"Ближайшие числа с шагом {step} к Х={X} -> {nearby_value}")

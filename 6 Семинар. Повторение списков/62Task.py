# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

import random

# N = int(input('Введите длину списка: '))

# list_1 = [random.randint(0,10) for _ in range(N)]

# print(list_1:=[random.randint(0,10) for _ in range(N)])

# count=0

# for i in range(1, len(list_1)-1):
#     if (list_1[i-1]<list_1[i]>list_1[i+1]):
#         count+=1

# print(count)

print(list_1:=[random.randint(0,10) for _ in range(int(input('Введите длину списка: ')))])
print(len([i for i in range(1, len(list_1)-1) if (list_1[i-1]<list_1[i]>list_1[i+1])]))
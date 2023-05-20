# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

print(list_1:=[random.randint(0,10) for _ in range(int(input('Введите длину списка: ')))])

minvalue = int(input())
maxvalue = int(input())

for i in range(len(list_1)):
  if (minvalue<list_1[i]<maxvalue):
    print(i)
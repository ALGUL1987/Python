# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random
list = [random.randint(-10,10) for i in range(int(input("Введите длину списка: ")))]
print(list)

temp = 0

for i in range(1, len(list)):
#    comparison = list[i]>list[i-1]
#    if comparison == False:
    if (list[i]>list[i-1]):
        temp+=1

print(temp)

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import random
list = [random.randint(0,10) for i in range(int(input("Введите длину списка: ")))]
print(list)

shifting = int(input("Введите число К: "))

for i in range(shifting):
    list.insert(0, list.pop())

print(list)

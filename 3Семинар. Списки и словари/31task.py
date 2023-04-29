# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

length = int(input("Введите длину списка: "))
list = []
temp = 0

for i in range(length):
    list.append(random.randint(0,10))
print(list)

# input_list_1 = [random.randint(0,10) for i in range(int(input("Введите длину списка: ")))]
# print(input_list_1)

# input_list_2 = [random.randint(0,10) for i in range(length)]
# print(input_list_2)

# print(len(set(input().split())))

colors = set(list)
print(len(colors))

print(len(set(list)))

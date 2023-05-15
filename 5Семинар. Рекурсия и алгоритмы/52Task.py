# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random, sys

n = int(input("Введите кол-во оценок: "))

log_true = []
for i in range(n):
    log_true.append(random.randint(1,5))

print(log_true)

log_false = log_true
for i in range(n):
    if (log_false[i]>=4):
        log_false[i]=1

print(log_false)
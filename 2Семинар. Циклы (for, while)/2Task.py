# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

value = int(input('Введите число А: '))

count_fibonacci = 2
number_fibonacci = 0
first_number_fibonacci = 0
second_number_fibonacci = 1

while (number_fibonacci < value):
    number_fibonacci = first_number_fibonacci + second_number_fibonacci
    first_number_fibonacci=second_number_fibonacci
    second_number_fibonacci=number_fibonacci
    count_fibonacci+=1

print(number_fibonacci)

if (number_fibonacci != value):
    print(f"Число А={value} => не является числом Фибоначчи")
    print(-1)
else:
    print(f"Число А={value} => является {count_fibonacci} по порядку числом Фибоначчи")

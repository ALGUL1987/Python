# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random, sys

n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))

first_multiplicity={random.randint(0,10) for i in range(n)}

second_multiplicity={random.randint(0,10) for i in range(m)}

union_multiplicity = set.union(first_multiplicity,second_multiplicity)

print(first_multiplicity)
print(second_multiplicity)
print(union_multiplicity)

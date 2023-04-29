# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

number = int(input('Введите значение N: '))
factorial = 1
i = 1

# while i <= number:
#     factorial *=i
#     i+=1

for i in range (1, number+1):
    factorial *=i

print(factorial)

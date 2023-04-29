# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum_value = int(input('Введите сумму двух чисел: '))
prod_value = int(input('Введите произведение двух чисел: '))

first_value_x = 0
second_value_y = 0

discrim_x = sum_value**2 - 4*prod_value

if (discrim_x > 0):
    first_value_x1 = (sum_value + discrim_x**(0.5))/2
    first_value_x2 = (sum_value - discrim_x**(0.5))/2
    if (first_value_x1%2==0 and first_value_x2%2==0):
        print(f"Число X = {first_value_x1} либо {first_value_x2}")
    else:
        print(f"Числа {sum_value} и {prod_value} заданы неверно")

elif (discrim_x < 0):
    print(f"Числа {sum_value} и {prod_value} заданы неверно")
else:
    first_value_x = sum_value/2
    if (first_value_x%2==0):
        print(f"Число X = {first_value_x}")
    else:
        print(f"Числа {sum_value} и {prod_value} заданы неверно")

discrim_y = sum_value**2 - 4*prod_value

if (discrim_y > 0):
    first_value_y1 = (sum_value + discrim_y**(0.5))/2
    first_value_y2 = (sum_value - discrim_y**(0.5))/2
    if (first_value_y1%2==0 and first_value_y2%2==0):
        print(f"Число Y = {first_value_y1} либо {first_value_y2}")
    else:
        print(f"Числа {sum_value} и {prod_value} заданы неверно")
elif (discrim_y < 0):
    print('Числа заданы неверно')
else:
    first_value_y = sum_value/2
    if (first_value_y%2==0):
        print(f"Число Y = {first_value_y}")
    else:
        print(f"Числа {sum_value} и {prod_value} заданы неверно")

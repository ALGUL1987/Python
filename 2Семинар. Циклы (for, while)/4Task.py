# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
quantity_watermelon = int(input('Введите кол-во арбузов: '))
min_weight = 30000
max_weight = 1
for i in range(quantity_watermelon):
    weight_watermelon = random.randint(5,20)
    print(weight_watermelon)
    if (weight_watermelon>max_weight):
        max_weight = weight_watermelon
    if (weight_watermelon<min_weight):
        min_weight = weight_watermelon
print(min_weight, max_weight)

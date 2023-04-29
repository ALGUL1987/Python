# List Comprehension
# У каждого ЯП есть свои особенности и преимущества. Для Python - list comprehension (генератор списков).
# list comprehension - это упрощенный поход к созданию списка, который задействует цикл for,
# а также инструкции if-else для определения того, что должно быть в финальном списке

list_1 = [i for i in range(1,101)]
print(list_1)

list_2 = [i for i in range(1,101) if i%2==0] #-только четные
print(list_2)

list_3 = [i*2 for i in range(10) if i%2==0] #-пример с математическими операциями
print(list_3)

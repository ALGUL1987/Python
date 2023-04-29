# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

firstClass = int(input('Введите количестов учащихся в классе №1: '))
secondClass = int(input('Введите количестов учащихся в классе №2: '))
thirdClass = int(input('Введите количестов учащихся в классе №3: '))

maxClass = None
if firstClass>secondClass and firstClass>thirdClass:
    maxClass = firstClass
elif secondClass>firstClass and secondClass>>thirdClass:
    maxClass = secondClass
else:
    maxClass = thirdClass

if maxClass%2==0:
    print(f"Количество парт необходимо -> {(maxClass//2)}")
else:
    print(f"Количество парт необходимо -> {(maxClass//2+1)}")

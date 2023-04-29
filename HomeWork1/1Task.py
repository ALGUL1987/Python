# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

value = int(input('Введите трехзначное число: '))
if value>99 and value<1000:
    print(f"Число {value} -> трехзначное")
else:
    print(f"Число {value} -> НЕ трехзначное! Введите трехзначное число")

firstNumber = value//100
secondNumber = (value%100)//10
thirdNumber = value%10
sum = firstNumber+secondNumber+thirdNumber
print(f"Сумма цифр {firstNumber}, {secondNumber}, {thirdNumber} в числе {value} равна {sum}")

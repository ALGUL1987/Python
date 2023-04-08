# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите номер билета: '))

firstNumber = ticket//100000
secondNumber = (ticket%100000)//10000
thirdNumber = (ticket%10000)//1000
fourthNumber = (ticket%1000)//100
fifthNumber = (ticket%100)//10
sixthNumber = ticket%10

sum1 = firstNumber+secondNumber+thirdNumber
sum2 = fourthNumber+fifthNumber+sixthNumber

if ticket < 100000 or ticket > 999999:
    print(f"В вашем городе все билеты несчастны")
elif sum1 == sum2:
    print(f"Билет {ticket} c цифрами {firstNumber}, {secondNumber}, {thirdNumber}, {fourthNumber}, {fifthNumber}, {sixthNumber} счастливый")
else:
    print(f"Билет {ticket} c цифрами {firstNumber}, {secondNumber}, {thirdNumber}, {fourthNumber}, {fifthNumber}, {sixthNumber} не совсем счастливый")

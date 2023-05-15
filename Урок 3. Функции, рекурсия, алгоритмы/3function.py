#Необходимо созать функцию sum_Numbers(n), которая будет считать сумму всех элементов от 1 до n.
# Правило функций и процедур - сколько аргументов мы принимаем, столько аргументов мы передаем и наоборот
def sum_Numbers(n): #обяъвление функции
    sum=0
    for i in range(1, n+1):
        sum+=i
    print(sum)

sum_Numbers(5) #вызов функции

#через return

def sum_Numbers(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum
    print('stop') #после return программа завершает работу - поэтому stop не выводится на экран

print(sum_Numbers(5))

#через переменную

def sum_Numbers(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum

a=sum_Numbers(5)
print(a)

#ввод через 2 аргумента

def sum_Numbers(n, m='Hello'): #если аргументу "m" далее в программе не задаем значение, то на экран будет выводится значение по умолчанию
    print(m)
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum

a=sum_Numbers(5)
print(a)

def sum_str(*args): #с помощью *args - можно передавать неограниченное количество аргументов
    res = ''
    for i in args:
        res+=i
    return res

print(sum_str('H', 'e', 'l', 'l', 'o'))
print(sum_str('H', 'e', 'l', 'l', 'o', ' ', 'w','o','r','l','d'))
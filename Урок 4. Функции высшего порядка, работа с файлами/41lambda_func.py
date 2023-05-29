# def f(x):
#     return x*x
# print(f(5))
# a = f # переменная а которая хранит ссылку на переменную f
# print(a(5))

# def calculate1(a,b):
#     return a+b

# def calculate2(a,b):
#     return a*b

# def math(op,x,y):
#     print(op(x,y))

# math(calculate1,5,45)

def math(op,x,y):
     print(op(x,y))

# calk1= lambda a,b:a+b
# math(calk1,5,45)

math(lambda a,b:a+b,5,45)

# Итак:
# 1. Сначала мы избавились от классического описания функций.
# 2. Затем научились описывать лямбды, присваивая результат какой-то переменной.
# 3. После избавились от этой переменной, пробрасывая всю лямбду в качестве функции.

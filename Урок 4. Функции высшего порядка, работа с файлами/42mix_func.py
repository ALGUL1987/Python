# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]

# def sqrt(x):
#     return x*x

# print(my_dict:={my_list[i]: sqrt(my_list[i]) for i in range(len(my_list)) if my_list[i]%2==0})

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in my_list:
#     if (i%2==0):
#         res.append((i, i**2))
# print(res)

def map(f, col):
    return [f(x) for x in col]

def filter(f,col):
    return [x for x in col if f(x)]

my_list = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, my_list)
print(res)
res = filter(lambda x:x%2==0,res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)
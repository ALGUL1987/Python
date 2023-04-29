a = {1,2,3,4,5,6,7}
b = {2,3,4,5,6,7,8}
c = a.copy() # - копирование множетсва
u = a.union(b) # - объединение множетсва
print(u)

i = a.intersection(b) # - нахождение пересечения в 2-х множетсвах
print(i)

x = a.difference(b) # - нахождение разницы в 2-х множетсвах
print(x)

y = a.union(b).difference(a.intersection(b)) # - в функции 1действие будет - a.intersection(b), далее - по порядку
print(y)

a = {1,8,6}
b = frozenset(a) # - заморозить множество. Такое множество не поддается изменениям
print(b)

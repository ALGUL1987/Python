# Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных.
# Эта функция работает со списками, кортежами, множествами и словарями для создания списков или кортежей, включающих все эти данные.

# В Python есть несколько встроенных функций, которые позволяют перебирать данные. Одна из них — zip.
# Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных.

# У функции zip() множество сценариев применения. Например, она пригодится, если нужно создать набор словарей из двух массивов,
# каждый из которых содержит имя и номер сотрудника.

#Функция zip Пример:
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

#Функция zip () пробегает по минимальному входящему набору:
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

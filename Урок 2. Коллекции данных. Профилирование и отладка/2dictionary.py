# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу
# В списках в качестве ключа используется индекс элемента. В словаре для определения элемента используется значение ключа (строка, число)

d = {} #  = для создания словари используются фигурные скобки
d = dict() #  = либо так
d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)
print(d['q'])

# Вправо (→) — Alt и 2 6.
# Влево (←) — Alt и 2 7.
# Вниз (↓) — Alt и 2 5.
# Вверх (↑) — Alt и 2 4.
# Вверх-вниз (↕) — Alt и 1 8.
# Влево-вправо (↔) — Alt и 2 9.

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'rigth': '→'}
print(dictionary)


# dictionary[895] = 989898
# print(dictionary)

#del dictionary['left'] #  = удаление ключа 'left'

for i in dictionary:
    print(i)
    print(f"{i}, {dictionary[i]}")

# dictionary.items() -
print(dictionary.items())
for (k, v) in dictionary.items(): # k - ключ, v - значение
    print(k,v)

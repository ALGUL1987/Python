# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
quantity_coins = random.randint(2, 21)

side_coin = None
eagle_coin = 0
tail_coin = 0

for i in range(quantity_coins):
    side_coin = random.randint(0, 2)
    if (side_coin==0):
        eagle_coin +=1
    else:
        tail_coin +=1

print(f"Орел - {eagle_coin}")
print(f"Решка - {tail_coin}")

if (eagle_coin>tail_coin):
    print(f"Минимальное кол-во переворотов монеток на одну сторону равно {tail_coin}")
else:
    print(f"Минимальное кол-во переворотов монеток на одну сторону равно {eagle_coin}")

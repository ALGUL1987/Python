# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s = input("Введите текст: ")
list_of_chars=list(s) # преобразование строки в список
letter_to_count = dict() # создается пустой словарь
for c in list_of_chars: # в словарь загоняется список, где ключи - значения индексов списка, значения - пусто
    if (c in letter_to_count): # создается условие на проверку повторения ключей
        letter_to_count[c]=letter_to_count[c]+1 # если есть повтор, значение ключа +1
    else:
        letter_to_count[c]=0 # в обратном случае = 0
    count_of_repeats=letter_to_count[c] # создается переменная для ниже операций
    print(f"{c}_{count_of_repeats}" if count_of_repeats>0 else c, end=' ') # в тернарном операторе создается условие если кол-во повторений больше чем 0 вернется count_of_repeats, иначе вернется с. end=' ' - прописывает каждый раз условие через пробел в одну строку, а не каждый раз выводит в новую строку



dict_count={}
for letter in list_of_chars:
    dict_count[letter]=dict_count.get(letter,0)+1 # каждый проход мы перезаписываем значение ключа на +1
    print(letter if dict_count.get(letter)==1 else f'{letter}_{dict_count.get(letter)-1},', end = ' ')

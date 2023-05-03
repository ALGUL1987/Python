# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

import string

str_split = input("Введите текст: ").replace('.','').lower().split() # replace  - замена точкм на пустоту, lower  - все буквы строчные, split - разделитель по пробелу

str_count={}

for i in str_split:
    str_count[i]=str_count.get(i,0)+1

print(f'Number of words in text is: {len(str_count)}')
print(str_count)

# for ch in string.punctuation: # циклом for проходимся по всему тексту в поисках знаков пунктуации и заменяем с помощью replace на пробелы
#     str_split=str_split.replace(ch, ' ')

# print(string.punctuation) #знаки пунктуации
# print(string.digits) #цифры
# print(string.printable) #все печатные символы
# print(string.ascii_letters) #англ алфавит верхний и нижний регистр
# print(string.ascii_lowercase) #англ алфавит нижний регистр
# print(string.ascii_uppercase) #англ алфавит верхний регистр
# print(string.hexdigits) #16тиричная система

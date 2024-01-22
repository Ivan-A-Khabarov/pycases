stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'



poems = stroka.split()
num_vowels = []

for poem in poems:
    words = poem.split('-')
    num_vowels.append(sum(1 for word in words for char in word if char.lower() in 'аеёиоуыэюя'))  # подсчет числа гласных и добавление в список

if len(num_vowels) > 1:
    if len(set(num_vowels)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
else:
    print('Количество фраз должно быть больше одной!')
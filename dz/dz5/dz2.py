def sum(a, b):
    if b == 0:  # базовый случай, если одно из чисел равно 0, то просто возвращаем другое число
        return a
    else:
        return sum(a + 1, b - 1)  # рекурсивный случай, увеличиваем первое число на 1, уменьшаем второе число на 1

print(sum(2, 2))  # выводит 4
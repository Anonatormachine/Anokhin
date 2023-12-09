# 1. Дан одномерный массив из 10 целых чисел. Вывести пары отрицательных чисел, стоящих рядом.

N = 10
array = []

for n in range(10):
    array.append(int(input(f"Введите элемент {n}: "))) 

for idx, n in enumerate(array):
    if n < 0 and array[idx + 1] < 0:
        print(f"({n}, {array[idx + 1]})")

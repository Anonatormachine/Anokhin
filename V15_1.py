#  Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран эти значения.

N = 10
array = []
for n in range(10):
    array.append(int(input(f"Введите элемент {n}: "))) 


print(f"Исходный массив - {array}") 

new_array = [] 

for elem in array: 
    if array.count(elem) > 1 and elem not in new_array: 
        new_array.append(elem)


print(f"Повторяющиеся значения - {new_array}") 

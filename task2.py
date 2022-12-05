# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

num_list = [0] * int(input('Введите длину списка: '))
for i in range(len(num_list)):
    num_list[i] = int(input('Введите число: '))
print(num_list)

def multi_pairs(n_list: list):
    i = 0
    while i < len(n_list) / 2:
        multi = num_list[i] * num_list[len(num_list) - 1 - i]
        print(multi, end= ' ')
        i += 1

multi_pairs(num_list)
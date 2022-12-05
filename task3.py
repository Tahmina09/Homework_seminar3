# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 10.01] => 0.19

float_list = []

_len = int(input('Введите длину списка: '))

for i in range(_len):
    float_list.append(float(input('Введите число: ')))
print(float_list)

def max_min_differ(nList: list):
        
    for i in range(len(nList)):
        nList[i] = round(nList[i] % 1, 3)
    
    print(nList, end= ' ')
    
    differ = max(nList) - min(nList)
    print(f'=>', round(differ, 3))
    

max_min_differ(float_list)
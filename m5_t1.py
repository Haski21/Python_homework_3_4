'''
Задача №1. Шахматная доска
Вход: размер шахматной доски (NxN), где N - число от 0 до 20.
Выход: вывести на экран эту доску, заполняя поля нулями и единицами

Пример:
Вход: 5
Выход:
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
'''
num = int(input('Enter num: '))
count = 0
while count < num:
    print('')
    for var in range(num):
        print('1', end ='') if var % 2 else print('0', end ='')
    count += 1
    print('')
    if count < num:
        for var in range(num):
           print('0', end ='') if var % 2 else print('1', end ='')
        count += 1

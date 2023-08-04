# Урок 6. Повторение списков

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

def fillArr(n:int):
    return [randint(-200, 200) for i in range(n)]

def indxMinMax(arrList:list):
    return [i for i in range(len(arrList)) if (arrList[i] > min and arrList[i] < max)]

min = int(input("Задайте минимум min: "))
max = int(input("Задайте максимум max: "))

n = int(randint(7, 10))
arr_list = fillArr(n)
print(f"{n} элементов в диапазоне [-200 : 200] - {arr_list}")
print(f"Индексы элементов диапазона  [{min} : {max}] - {indxMinMax(arr_list)}")
# Найти номера минимального и максимального элементов первой половины списка.
import random

myArr = []

for x in range(100):
    myArr.append(random.randint(1, 999))

minInt = 999
maxInt = 0

for x in range(int(len(myArr) / 2)):
    if (myArr[x] > maxInt):
        maxInt = myArr[x]
    if (myArr[x] < minInt):
        minInt = myArr[x]

print(f"Минимальное значение первой половины массива {minInt}\n")
print(f"Максимальное значение первой половины массива {maxInt}\n")

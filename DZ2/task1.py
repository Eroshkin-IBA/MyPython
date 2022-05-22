# Вариант 3
# Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.

import random

A = []
for i in range(200):
    A.append(random.randint(-50, 100))
print(A)

# Найдите сумму отрицательных элементов списка
negativeSum = 0
for a in range(len(A)):
    if (A[a] < 0):
        negativeSum += A[a]

print(f"Сумма отрицательных значений списка {negativeSum}")

# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.
try:
    sum = 0
    firstNull = A.index(0)
    secondNull = A.index(0, firstNull + 1)
    for a in range(firstNull,secondNull):
        sum += A[a]
    print(f"суммa элементов списка между двумя первыми нулями {sum}")
except:
    print("Значения ноль нет")


import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def ShakerSort(A):
    for i in range( int(len(A) / 2)):
        for j in range( len(A) - 1 - i):
            if (A[j] > A[j + 1]):
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i + 1,-1):
            if (A[j] < A[j - 1]):
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


table = prettytable.PrettyTable(["Размер списка", "Время шейкера"])
x = []
y0 = []

for N in range(10, 100, 10):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    print("\n-----------------------------------------before")
    print(A)
    t1 = datetime.datetime.now()
    ShakerSort(A)
    print("\n-----------------------------------------after")
    print(A)
    t2 = datetime.datetime.now()
    y0.append((t2 - t1).total_seconds())
    print("Шейкерная сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    table.add_row(
        [str(N), str((t2 - t1).total_seconds())])
print(table)

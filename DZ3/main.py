import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def ShakerSort(A):
    for i in range(int(len(A) / 2)):
        for j in range(len(A) - 1 - i):
            if (A[j] > A[j + 1]):
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A) - 2 - i, i + 1, -1):
            if (A[j] < A[j - 1]):
                a = A[j]
                A[j] = A[j - 1]
                A[j - 1] = a


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время шейкера", "Время быстрой"])
x = []
y0 = []
y1 = []
y2 = []

for N in range(1000, 15001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    # print(B)
    C = B.copy()

    # BubbleSort(A)
    # print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)

    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")
    # print(C)
    # print("-----------------------------")
    t5 = datetime.datetime.now()
    ShakerSort(C)
    # print(C)
    t6 = datetime.datetime.now()
    y0.append((t6 - t5).total_seconds())
    print("Шейкерная сортировка   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t6 - t5).total_seconds()), str((t4 - t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y0, "C2")
plt.show()

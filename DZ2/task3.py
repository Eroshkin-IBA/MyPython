import random

import numpy as np

A = np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
              [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
              [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
              [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]])

print(len(A))

rows = len(A[:, 0])
cols = len(A[0])

counter = 0
maxi = sum(A[0])

for x in range(cols + 1):
    if maxi < sum(A[x]):
        maxi = sum(A[x])
        counter = x

print(A)
print(f"в строке №{counter+1} сумма чисел максимальна\n {A[counter]} = {sum(A[counter])}")


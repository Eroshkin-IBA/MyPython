#Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент. 
#Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные. 

import random

A = []
for i in range(50):
    A.append(random.randint(-50, 100))
print(A)

#Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
minEven = []
for a in range(len(A)):
    if(A[a]!=0 and A[a]%2==0):
        minEven.append(A[a])


print(f"наименьший четный элемент списка {min(minEven) if len(minEven)>0 else A[0]}")

#Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

A.append(None)
A.append(None)
A.append(None)
print(A)

noneList = []

for a in range(len(A)):
    if(A[a]== None):
        noneList.append(A[a])

finishList = noneList + sorted(list(filter(lambda x: (x != None),A)))

print(f"Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные\n{finishList}")








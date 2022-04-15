# Натуральное число, записанное в десятичной системе счисления, называется сверхпростым, если оно остается
# простым при любой перестановке своих цифр. Определить все сверхпростые числа до n.


arrNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Введите чило n\n"))
arrSuper = []
strNumber = ""


for x in range(len(arrNumber)):
    for i in range(len(str(n))):
        strNumber += str(arrNumber[x])
        if(int(strNumber)<=n and len(strNumber)>1):
            arrSuper.append(int(strNumber))
    strNumber = ""


print(f"Все сверхпростые числа до числа {n}")
arrSuper = sorted(arrSuper)
for x in range(len(arrSuper)):
    print(arrSuper[x])


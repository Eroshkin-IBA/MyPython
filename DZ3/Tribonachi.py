a = 0

def tribonachi(i):
    global a
    a +=1

    print(a)
    if(i==1 or i==2):
        return 0
    if(i==3 or i==4):
        return 1
    return tribonachi(i-1)+tribonachi(i-2)+tribonachi(i-3)


b = []
#s = int(input("Введите число "))
for i in range(1,20):
    b.append(tribonachi(i))

print(b)
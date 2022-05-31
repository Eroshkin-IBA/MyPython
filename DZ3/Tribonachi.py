def tribonachi(i):
    if(i==1 or i==2):
        return 0
    if(i==3 or i==4):
        return 1
    return tribonachi(i-1)+tribonachi(i-2)+tribonachi(i-3)
a=[]
#s = int(input("Введите число "))
for i in range(1,35):
    a.append(tribonachi(i))

print(a)
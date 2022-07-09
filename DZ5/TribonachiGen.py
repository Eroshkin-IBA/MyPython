def tribanachi_generator(val):
    first = 0
    second = 0
    third = 1
    counter = 0
    while counter <= val:
        counter += 1
        if counter == 1 or counter == 2:
            yield 0
        elif counter == 3:
            yield 1
        else:
            sum = first + second + third
            first = second
            second = third
            third = sum
            yield sum

iter = tribanachi_generator(20)
list =[]
for x in iter:
    list.append(x)

print(list)
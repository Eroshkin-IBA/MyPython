a = int(input("Введите длинну прямоугольника "))
b = int(input("Введите ширину прямоугольника "))

def rectangleCount(a, b):

    if a == b:
        count = 1
        print('Квадрат с длиной стороны = ', a)
    elif a > b:


        count = rectangleCount(a - b, b) + 1
        print('Квадрат с длиной стороны = ', b)
    else:
        return 0
    return count

print('Количество квадратов которые можно вписать в прямоугольник со сторонами ' +
      str(a) + ' и ' + str(b) + ' равно: ' + str(rectangleCount(a, b)))
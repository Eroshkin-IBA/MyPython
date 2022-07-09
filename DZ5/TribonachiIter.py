class tribonIterator:
    first = 0
    second = 0
    third = 1

    def __init__(self, value):
        self.counter = 0
        self.size = value

    def __next__(self):
        if self.counter <= self.size:
            self.counter += 1
            if (self.counter == 1 or self.counter == 2): return 0
            if (self.counter==3): return 1
            else:
                sum = self.first + self.second + self.third
                self.first = self.second
                self.second = self.third
                self.third = sum
                return sum
        else: raise StopIteration

    def __iter__(self): return self


tribonachi = tribonIterator(30)
list = []
for x in tribonachi:
    list.append(x)

print(list)
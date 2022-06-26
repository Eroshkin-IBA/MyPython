class Table:
    couter = 0

    def __init__(self, mass):
        self.__mass = mass
        couter += 1
    def getMass(self):
        return self.__mass

class Truck:
    __checker = 0
    tables = []
    def __init__(self, loadCapacity):
        self.__loadCapacity = loadCapacity

    def add(self, table):
        for x in self.tables:
            self.__checker += x.getMass()
        if(self.__checker + table.getMass() > self.__loadCapacity):
            print("Truck is overeloaded")
            return
        self.tables.append(table)
        print("table added")
        print(f"current mass {self.__checker + table.getMass()}")

        return


truck = Truck(250)
truck.add(Table(15))
truck.add(Table(15))
truck.add(Table(19))
truck.add(Table(15))
truck.add(Table(17))
truck.add(Table(17))
truck.add(Table(17))

print(Table.couter)

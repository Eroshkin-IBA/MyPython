class Car:
    def __init__(self, id, mark, model, carYear, color, coast, number):
        if (carYear < 1886 or carYear > 2022):
            raise Exception("Incorrect year")
        else:
            self.__id = id
            self.__mark = mark
            self.__model = model

            self.__carYear = carYear
            self.__color = color
            self.__coast = coast
            self.__number = number

    def getId(self):
        return self.__id
    def getMark(self):
        return self.__mark
    def getModel(self):
        return self.__model
    def getCarYear(self):
        if(self.__carYear < 1886):
            raise Exception("Incorrect year")
            return
        return self.__carYear
    def getColor(self):
        return self.__color
    def getCoast(self):
        return self.__coast
    def getNumber(self):
        return self.__number


    def setId(self, id):
        self.__id = id
        return
    def setMark(self, mark):
        self.__mark = mark
        return
    def setModel(self, model):
        self.__model = model
        return
    def setCarYear(self,year):
        if(year < 1886):
            raise Exception("Incorrect year")
            return
        self.__carYear = year
        return
    def setColor(self, color):
        self.__color = color
        return
    def setCoast(self, coast):
        self.__coast = coast
        return
    def setNumber(self, number):
        self.__number = number
        return

    @staticmethod
    def compareYear(car1, car2):
        firstName = car1.getMark()
        secName = car2.getMark()
        if int(car1.getCarYear()) < int(car2.getCarYear()):
            print(f"{firstName} старше {secName}")
        else:
            print(f"{secName} старше {firstName}")

    @staticmethod
    def findByBrend(carList, brand):
        print("===========================")
        print(f"Машины бренда {brand}")
        for x in carList:
            if (x.getMark() == brand):
                print(f"{x.getMark()} {x.getModel()}")
        print("===========================")

    @staticmethod
    def findByYear(carList, year):
        print("===========================")
        print(f"Машины старше {2022 - year} лет")
        for x in carList:
            if (x.getCarYear() <= year):
                print(f"{x.getMark()} год {x.getCarYear()}")
        print("===========================")




carList = []




car1 = Car(12,"BMW", "M5", 1998, "Black", 15_000, "mb145-98")
car2 = Car(12,"Mercedez", "benz", 2005, "Black", 25_000, "mb145-98")
car3 = Car(12,"mazda", "benz", 2020, "Black", 25_000, "mb145-98")
car4 = Car(12,"opel", "benz", 2007, "Black", 25_000, "mb145-98")
car5 = Car(12,"fiat", "benz", 2015, "Black", 25_000, "mb145-98")
car6 = Car(12,"siat", "benz", 2018, "Black", 25_000, "mb145-98")
car7 = Car(12,"BMW", "benz", 2019, "Black", 25_000, "mb145-98")
car8 = Car(12,"bugatti", "benz", 2022, "Black", 25_000, "mb145-98")


carList.append(car1)
carList.append(car2)
carList.append(car3)
carList.append(car4)
carList.append(car5)
carList.append(car6)
carList.append(car7)
carList.append(car8)




Car.findByBrend(carList, "BMW")
Car.findByYear(carList, 2015)

Car.compareYear(car1,car2)







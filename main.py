from account import Account
from car import Car
from cash import Cash
from uberConfort import UberConfort
from uberX import UberX


if __name__ == "__main__":

    car = Car("PBO5555", Account("estefany Suntaxi", "1727737924"))
    print(vars(car))
    print(vars(car.driver))

    uberX = UberX("PCC-12345", Account("Gabriel", "777777777"), "Chevrolet", "Spark")
    print(vars(uberX))
    print(vars(uberX.driver))

    uberConfort = UberConfort("PJK-4561", Account("Julian", "1717196560"), "Dodge", "Cuero", "7")
    print(vars(uberConfort))
    print(vars(uberConfort.driver))

    #pagoDinero = Cash("1", "14-7-2022", "20", "Cash")
    #print(vars(pagoDinero))
    #print(pagoDinero.date)
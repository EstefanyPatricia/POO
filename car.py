from lib2to3.pgen2 import driver
from pyexpat import model


class Car :
    id              =int
    driver          =str
    passaggers      =str
    brand           =str
    model           =str

    def __init__(self, driver, passaggers, brand, model):
        self.driver     = driver
        self.passaggers = passaggers
        self.brand      = brand
        self.model      = model
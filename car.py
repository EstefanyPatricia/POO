
from pyexpat import model
from account import Account


class Car:
    id              = int
    #Cambiamos tipo de dato driver por Account (primero inportar la informacion)
    driver          = Account("","")
    passaggers      = str
    brand           = str
    model           = str
    license         = str

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver
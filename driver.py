from ast import Str
from account import Account


class Driver (Account):
    id          = int
    license     = str

    def __init__(self, idDriver, license, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)
        self.idDriver   = idDriver
        self.license    = license
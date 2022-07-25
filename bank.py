from payment import Payment


class Bank(Payment):
    banName         = str
    identification  = str
    numberAccount   = int

    def __init__(self, id, ammount, bankName, numberAccount, indentification):
        super.__init__(id, ammount)
        self.bankName           = bankName
        self.identification     = indentification
        self.numberAccount      = numberAccount
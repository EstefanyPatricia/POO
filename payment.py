class Payment :
    id              = int
    ammount         = int
    date            = str
    typePayment     = []
    
    def __str__(self, id, ammount, typePayment):
        self.id             = id
        self.ammount        = ammount
        self.typePayment    = typePayment


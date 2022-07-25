from car import Car

class UberPromo(Car):
    brand   = str
    model   = str
    
    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        super.brand     = brand
        super.model     = model
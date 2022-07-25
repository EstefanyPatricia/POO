from car import Car


class UberFlash(Car):
    brand       = str
    model       = str
    locadSize   = []
    loadWeight   = int

    def __init__(self, license, driver, brand, model, loadZize, loadWeight):
        super.__init__(license,driver) 
        self.brand      = brand
        self.model      = model
        self.loadZize   = loadZize
        self.loadWeight = loadWeight

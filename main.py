from pprint import pprint
from account import Account
from car import Car
from driver import Driver
from payment import Payment
from route import Route
from user import User

if __name__ == "__main__":
        print("Hola mundo")

        carro = Car()
        carro.id                = 5
        carro.brand             = "TOYOTA"
        carro.driver            = "Estefany"
        carro.passaggers        = 10

        print(vars(carro))

        carro2 = Car()
        carro.id                = 7
        carro.brand             = "MAZDA"
        carro.driver            = "Estefany"
        carro.passaggers        = 17

        print(vars(carro))
        print(vars(carro2))

        cuenta = Account()
        cuenta.id               = 3
        cuenta.name             = "Alex Israel"
        cuenta.document         = 1727737924
        cuenta.email            ="pati@gmail.com"
        cuenta.password         ="1234567"

        print(vars(carro))
        print(vars(carro2))
        print(vars(cuenta))

        pago = Payment()
        pago.id         = 5
        pago.ammouny    = 40

        print(vars(pago))

        ruta = Route()
        ruta.id         = 10
        ruta.star       = "Quito"
        ruta.end        = "Cuenca"

        print(vars(ruta))



        usuario = User()
        usuario.id              = 20
        usuario.name            = "Santiago"
        usuario.lastname        = "Tonato"

        print(vars(usuario))


        conductor = Driver()
        conductor.id            = 12
        conductor.name          = "Julian"
        conductor.document      = 1002944476
        conductor.email         = "julian@gmail.com"
        conductor.password      = "julian123"

        print(vars(conductor))
class cuenta:
    def __init__(self, nombre_ban, nombre, moneda, dinero):
        self.__nombre_ban = nombre_ban
        self.__nombre = nombre
        self.__moneda = moneda
        self.__dinero = dinero
        self.esta_retirando = False

    def retirar(self):
        self.esta_retirando = True
        print("Esta retirando dinero")

    def get_Nombre_banco(self):
        return self.__nombre_ban

    def get_Nombre(self):
        return self.__nombre

    def get_Moneda(self):
        return self.__moneda

    def get_Dinero(self):
        return self.__dinero

    def set_Dinero(self, dinero):
        self.__dinero = dinero


cuenta1 = cuenta("bancolombia", "juan andres",
                 "peso colombiano", "3.450.000 pesos colombianos")
print("El banco es:", cuenta1.get_Nombre_banco())
print("El propientario de la cuenta es:", cuenta1.get_Nombre())
print("La divisa es:", cuenta1.get_Moneda())
print("la cuenta tiene", cuenta1.get_Dinero())
cuenta1.retirar()
print("El propientario retiro 500.000 pesos colombianos")
cuenta1.set_Dinero("2.950.000 pesos colombianos")
print("La cuenta tiene", cuenta1.get_Dinero())

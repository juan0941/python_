print("                                ")
print("LA BEBIDA 1")


class Drinks:
    def __init__(self, mark, taste):
        self.mark = mark
        self.taste = taste
        self.the_ingredients = False
        self.the_prices = False

    def ingredients(self):
        self.the_ingredients = True
        print("los ingredientes de la bebida son: Agua carbonatada, azúcar, colorante: caramelo, acidulante: ácido fosfórico, aromatizantes")

    def prices(self):
        self.the_prices = True
        print("Los precios son entre: 3000 y 9000")


Drinks1 = Drinks("Coca-Cola", "Cola")
print("la marca de la bebida es:", Drinks1.mark)
print("El sabor de la bebida es:", Drinks1.taste)
Drinks1.ingredients()
Drinks1.prices()

print("                                ")
print("LA BEBIDA 2")
print("                                ")


class water(Drinks):
    def __init__(self, mark, taste, ingredients_contain):
        super().__init__(mark, taste)
        self.ingredients_contain = ingredients_contain

    def contain(self):
        print(f"los ingredientes que contiene son: {self.ingredients_contain}")


class energy_drink(Drinks):
    def __init__(self, mark, taste, logo_drawing):
        super().__init__(mark, taste)
        self.logo_drawing = logo_drawing

    def logo(self):
        print(f"el dibujo que tiene el logo es: {self.logo_drawing}")


water1 = water("H2O", "maracuya",
               "AGUA CARBONATADA, ACIDULANTES (ACIDO CİTRICO Y ÁCIDO MÁLICO), SABORIZANTE NATURAL")
print("La marca de la bebida es:", water1.mark)
print("El sabor de la bebida es:", water1.taste)
water1.contain()
print("                                ")
print("LA BEBIDA 3")
print("                                ")
energy_drink1 = energy_drink("redbull", "Black Orange", "un toro")
print("La marca de la bebida es:", energy_drink1.mark)
print("EL sabor de la bebida es:", energy_drink1.taste)
energy_drink1.logo()

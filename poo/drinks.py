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

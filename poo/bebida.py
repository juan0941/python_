print("LA BEBIDA 1")
print("                                ")


class Bebidas:
    def __init__(self, marca, sabor):
        self.marca = marca
        self.sabor = sabor
        self.los_ingredientes_son = False
        self.el_precio_de_la_bebida = False

    def ingredientes(self):
        self.los_ingredientes_son = True
        print("los ingredientes de la bebida son: Agua carbonatada, azúcar, colorante: caramelo, acidulante: ácido fosfórico, aromatizantes")

    def precio(self):
        self.el_precio_de_la_bebida = True
        print("Los precios son entre: 3000 y 9000")


bebi = Bebidas("coca-cola", "cola")
print("La marca de la bebida es:", bebi.marca)
print("El sabor de la bebida es:", bebi.sabor)
bebi.ingredientes()
bebi.precio()

print("                                ")
print("LA BEBIDA 2")
print("                                ")


class agua(Bebidas):
    def __init__(self, marca, sabor, que_contiene):
        super().__init__(marca, sabor)
        self.que_contiene = que_contiene

    def contiene(self):
        print(
            f"el agua contiene los sigientes ingredientes {self.que_contiene}")


class bebida_energetica(Bebidas):
    def __init__(self, marca, sabor, que_dibujo_tiene_el_logo):
        super().__init__(marca, sabor)
        self.que_dibujo_tiene_el_logo = que_dibujo_tiene_el_logo

    def logo(self):
        print(
            f"El dibujo que tiene el logo de la bebida es un: {self.que_dibujo_tiene_el_logo}")


agua1 = agua("H2O", "maracuya",
             "AGUA CARBONATADA, ACIDULANTES (ACIDO CİTRICO Y ÁCIDO MÁLICO), SABORIZANTE NATURAL")
print("La marca de la bebida es:", agua1.marca)
print("El sabor de la bebida es:", agua1.sabor)
agua1.contiene()
print("                                ")
print("LA BEBIDA 3")
print("                                ")
bebida_energetica1 = bebida_energetica("redbull", "Black Orange", "un toro")
print("La marca de la bebida es:", bebida_energetica1.marca)
print("EL sabor de la bebida es:", bebida_energetica1.sabor)
bebida_energetica1.logo()

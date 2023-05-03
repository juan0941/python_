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

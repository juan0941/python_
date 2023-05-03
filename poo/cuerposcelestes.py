class Cuerpo_celeste:
    def __init__(self, planeta, color):
        self.planeta = planeta
        self.color = color
        self.pos = False
        self.desc = False
        self.tam = False
        self.rad = False
        self.grav = False

    def posicion(self):
        self.pos = True
        print("Esta en la sexta posicion contando el sol")

    def descripcion(self):
        self.desc = True
        print("Es un planeta grande con un aniño alrededor")

    def tamaño(self):
        self.tam = True
        print("Es el segundo planeta mas grande en tamaño y masa despues de jupiter")

    def radio(self):
        self.rad = True
        print("Tiene un radio de: 58,232 km")

    def gravedad(self):
        self.grav = True
        print("Tiene una gravedad de: 10.44 m/s²")


plane = Cuerpo_celeste("saturno", "amarillo palido")
print("El nombre del planeta es: ", plane.planeta)
print("El color del planeta es: ", plane.color)
plane.posicion()
plane.descripcion()
plane.tamaño()
plane.radio()
plane.gravedad()

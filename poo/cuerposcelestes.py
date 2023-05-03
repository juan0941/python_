class Cuerpo_celeste:
    def __init__(self, planeta, color):
        self.planeta = planeta
        self.color = color
        self.la_posicion_del_planeta = False
        self.la_descripcion_del_planeta = False
        self.el_tamaño_del_planeta = False
        self.el_radio_del_planeta = False
        self.la_gravedad_del_planeta = False

    def posicion(self):
        self.la_posicion_del_planeta = True
        print("Esta en la sexta posicion contando el sol")

    def descripcion(self):
        self.la_descripcion_del_planeta = True
        print("Es un planeta grande con un aniño alrededor")

    def tamaño(self):
        self.el_tamaño_del_planeta = True
        print("Es el segundo planeta mas grande en tamaño y masa despues de jupiter")

    def radio(self):
        self.el_radio_del_planeta = True
        print("Tiene un radio de: 58,232 km")

    def gravedad(self):
        self.la_gravedad_del_planeta = True
        print("Tiene una gravedad de: 10.44 m/s²")


plane = Cuerpo_celeste("saturno", "amarillo palido")
print("El nombre del planeta es: ", plane.planeta)
print("El color del planeta es: ", plane.color)
plane.posicion()
plane.descripcion()
plane.tamaño()
plane.radio()
plane.gravedad()

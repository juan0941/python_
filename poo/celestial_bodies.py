class Celestial_bodies:
    def __init__(self, planet, color):
        self.planet = planet
        self.color = color
        self.is_in_position = False
        self.Planet_description = False
        self.Planet_size = False
        self.Planet_radius = False
        self.Planetary_gravity = False

    def position(self):
        self.is_in_position = True
        print("Esta en la sexta posicion contando el sol")

    def description(self):
        self.Planet_description = True
        print("Es un planeta grande con un aniño alrededor")

    def size(self):
        self.Planet_size = True
        print("Es el segundo planeta mas grande en tamaño y masa despues de jupiter")

    def radio(self):
        self.Planet_radius = True
        print("Tiene un radio de: 58,232 km")

    def gravity(self):
        self.Planetary_gravity = True
        print("Tiene una gravedad de: 10.44 m/s²")


Celestial_bodies1 = Celestial_bodies("saturno", "amarillo palido")
print("El nombre del planeta es:", Celestial_bodies1.planet)
print("El planeta es de color:", Celestial_bodies1.color)
Celestial_bodies1.position()
Celestial_bodies1.description()
Celestial_bodies1.size()
Celestial_bodies1.radio()
Celestial_bodies1.gravity()

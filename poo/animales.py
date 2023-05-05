print("EL PERRO 1")
print("                                ")


class Animales:
    def __init__(self, nombre, raza, años, color):
        self.nombre = nombre
        self.raza = raza
        self.años = años
        self.color = color
        self.se_levanto = False
        self.esta_dormido = False
        self.esta_comiendo = False

    def levantarse(self):
        self.se_levanto = True
        print("El perro se desperto")

    def comiendo(self):
        self.esta_comiendo = True
        print("El perro esta comiendo")

    def dormido(self):
        self.esta_dormido = True
        print("El perro se durmio")


perro = Animales("booster", "Doberman", "7: años", "negro")
print("El nombre del perro es: ", perro.nombre)
print("La raza del perro es: ", perro.raza)
print("El perro tiene ", perro.años)
print("EL perro es de color: ", perro.color)
perro.levantarse()
perro.comiendo()
perro.dormido()
# ///////////////////////////////////
print("                                ")
print("EL GATO")
print("                                ")


class gato(Animales):
    def __init__(self, nombre, raza, años, color, num_de_patas):
        super().__init__(nombre, raza, años, color)
        self.num_de_patas = num_de_patas

    def patas(self):
        print(f"el gato tiene {self.num_de_patas} patas")


class Dog(Animales):
    def __init__(self, nombre, raza, años, color, nom_del_dueno):
        super().__init__(nombre, raza, años, color)
        self.nom_del_dueno = nom_del_dueno

    def dueno(self):
        print(f"{self.nom_del_dueno} es el dueño de", self.nombre)


gato1 = gato("manchas", "persa", "5: años", "blanco y negro", 4)
print("El gato se llama:", gato1.nombre)
print("La raza del gato es:", gato1.raza)
print("El gato tiene,", gato1.años)
print("El gato es de color:", gato1.color)
gato1.patas()
print("                                ")
print("El perro 2")
print("                                ")
Dog1 = Dog("lucas", "chihuahua", "3: años", "cafe", "Daniel")
print("El perro se llama:", Dog1.nombre)
print("La razza del perro es:", Dog1.raza)
print("EL perro tiene", Dog1.años)
print("El color del perro es:", Dog1.color)

Dog1.dueno()

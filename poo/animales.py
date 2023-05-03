class Animales:
    def __init__(self, nombre, raza, años, color):
        self.nombre = nombre
        self.raza = raza
        self.años = años
        self.color = color
        self.levantar = False
        self.dormir = False
        self.comer = False

    def levantarse(self):
        self.levantar = True
        print("El perro se desperto")

    def comiendo(self):
        self.comer = True
        print("El perro esta comiendo")

    def dormido(self):
        self.dormir = True
        print("El perro se durmio")


perro = Animales("booster", "Doberman", "7", "negro")
print("El nombre del perro es: ", perro.nombre)
print("La raza del perro es: ", perro.raza)
print("El perro tiene: ", perro.años, "años")
print("EL perro es de color: ", perro.color)
perro.levantarse()
perro.comiendo()
perro.dormido()

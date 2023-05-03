class Persona:
    def __init__(self, nombre, edad, profecion):
        self.nombre = nombre
        self.edad = edad
        self.profecion = profecion
        self.saludo = False
        self.fue_presentado = False

    def Saludar(self):
        self.saludo = True
        print(self.nombre, ",Esta saludando")

    def presentar(self):
        self.fue_presentado = True
        print("mucho gusto soy, ", self.nombre, "tengo",
              self.edad, " y mi profecion es ", self.profecion)


persona1 = Persona("juan andres", "20 años", "ingeniero informatico")
print(persona1.nombre, persona1.edad, persona1.profecion)


persona1.Saludar()
persona1.presentar()

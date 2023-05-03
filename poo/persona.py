class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.Esta_saludando = False
        self.fue_presentado = False

    def Saludar(self):
        self.Esta_saludando = True
        print(self.nombre, ",Esta saludando")

    def presentar(self):
        self.fue_presentado = True
        print("mucho gusto soy, ", self.nombre, "tengo",
              self.edad, " y mi profecion es ", self.profesion)


persona1 = Persona("juan andres", "20 años", "ingeniero informatico")
print(persona1.nombre, persona1.edad, persona1.profesion)


persona1.Saludar()
persona1.presentar()

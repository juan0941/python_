class Texto:
    def __init__(self, tipo, parrafos):
        self.tipo = tipo
        self.parrafos = parrafos
        self.nom = False
        self.aut = False

    def nombre(self):
        self.nom = True
        print("El titulo del texto es: Ante la ley")

    def autor(self):
        self.aut = True
        print("El autor del tecto es: Franz Kafka")


texto1 = Texto("narrativo", "8 parrarfos")
print("EL texto es de tipo:", texto1.tipo)
print("EL texto tiene", texto1.parrafos)
texto1.nombre()
texto1.autor()

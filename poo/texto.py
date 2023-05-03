class Texto:
    def __init__(self, tipo, parrafos):
        self.tipo = tipo
        self.parrafos = parrafos
        self.titulo_del_texto = False
        self.autor_del_texto = False

    def nombre(self):
        self.titulo_del_texto = True
        print("El titulo del texto es: Ante la ley")

    def autor(self):
        self.autor_del_texto = True
        print("El autor del tecto es: Franz Kafka")


texto1 = Texto("narrativo", "8 parrarfos")
print("EL texto es de tipo:", texto1.tipo)
print("EL texto tiene", texto1.parrafos)
texto1.nombre()
texto1.autor()

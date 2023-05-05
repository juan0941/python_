print("TEXO 1")
print("                                          ")


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
# ////////////////////////////////////////////////////////////
print("                                          ")
print("TEXTO 2")
print("                                          ")


class cuento(Texto):
    def __init__(self, tipo, parrafos, _quien_lo_escibio, nombre_del_cuento):
        super().__init__(tipo, parrafos)
        self.quien_lo_escribio = _quien_lo_escibio
        self.nombre_del_cuento = nombre_del_cuento

    def escritor(self):
        print(f"El autor del cuento es {self.quien_lo_escribio}")

    def cuento(self):
        print(f"El nombre del cuento es {self.nombre_del_cuento}")


cuento1 = cuento("ficcion", "23 parrafos", "Oscar Wilde", "El Príncipe Feliz")
print("El genero del cuento es:", cuento1.tipo)
print("El cuento tiene", cuento1.parrafos)
cuento1.escritor()
cuento1.cuento()

print("Materia 1")
print("                         ")


class Materias:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota
        self.nombre_del_profesor = False
        self.temas_del_curso = False

    def nom_profesor(self):
        self.nombre_del_profesor = True
        print("El nombre del profesor es: Javier Sanchez")

    def temas(self):
        self.temas_del_curso = True
        print("Los temas que nos dan en la materia son: logica de programacion, ciclos, programacion orientada a objetos ")


Materias1 = Materias("programacion web fullstak", "4.5")
print("El nombre de la materia es:", Materias1.materia)
print("La nota sacada en la actividad numero un es:", Materias1.nota)
Materias1.nom_profesor()
Materias1.temas()
# /////////////////////////////////////////////////////
print("                         ")
print("Materia 2")
print("                         ")


class ingles(Materias):
    def __init__(self, materia, nota, nivel_ingles):
        super().__init__(materia, nota)
        self.nivel_ingles = nivel_ingles

    def nivel(self):
        print(f"El estudiante esta en nivel {self.nivel_ingles} de ingles ")


class Matematicas(Materias):
    def __init__(self, materia, nota, nota_parcial):
        super().__init__(materia, nota)
        self.nota_parcial = nota_parcial

    def parcial(self):
        print(f"La nota del parcial es {self.nota_parcial} ")


ingles1 = ingles("ingles", "4,5", "B1")
print("El nombre de la materia es:", ingles1.materia)
print("La nota es: ", ingles1.nota)
ingles1.nivel()
print("                         ")
print("Materia 3")
print("                         ")
Matematicas1 = Matematicas("matematicas", "3,5", "4,5")
print("El nombre de la materia es:", Matematicas1.materia)
print("La nota de la materia es:", Matematicas1.nota)
Matematicas1.parcial()

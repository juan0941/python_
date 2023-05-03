class Materias:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota
        self.porf = False
        self.tem = False

    def nom_profesor(self):
        self.porf = True
        print("El nombre del profesor es: Javier Sanchez")

    def temas(self):
        self.tem = True
        print("Los temas que nos dan en la materia son: logica de programacion, ciclos, programacion orientada a objetos ")


Materias1 = Materias("programacion web fullstak", "4.5")
print("El nombre de la materia es:", Materias1.materia)
print("La nota sacada en la actividad numero un es:", Materias1.nota)
Materias1.nom_profesor()
Materias1.temas()

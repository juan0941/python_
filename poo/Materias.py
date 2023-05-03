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

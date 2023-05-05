print("Materia 1")
print("                         ")


class Courses:
    def __init__(self, course, note):
        self.course = course
        self.note = note
        self.teacher_name = False
        self.course_topics = False

    def teacher(self):
        self.teacher_name = True
        print("El nombre del profesor es: Javier Sanchez")

    def topic(self):
        self.course_topics = True
        print("Los temas que nos dan en la materia son: logica de programacion, ciclos, programacion orientada a objetos ")


Courses1 = Courses("programacion web fullstak", "4.5")
print("El nombre de la materia es:", Courses1.course)
print("La nota sacada en la actividad numero un es:", Courses1.note)
Courses1.teacher()
Courses1.topic()
# /////////////////////////////////////////
print("                         ")
print("Materia 2")
print("                         ")


class English(Courses):
    def __init__(self, course, note, english_level):
        super().__init__(course, note)
        self.english_level = english_level

    def leven(self):
        print(f"La nota del examen final es {self.english_level} ")


class math(Courses):
    def __init__(self, course, note, Final_note):
        super().__init__(course, note)
        self.Final_note = Final_note

    def note_f(self):
        print(f"El estudiante esta en nivel {self.Final_note} de ingles")


English1 = English("ingles", "4,5", "B1")
print("El nombre de la materia es:", English1.course)
print("La nota es: ", English1.note)
English1.leven()
print("                         ")
print("Materia 3")
print("                         ")
math1 = math("matematicas", "3,5", "4,5")
print("El nombre de la materia es:", math1.course)
print("La nota de la materia es:", math1.note)
math1.note_f()

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

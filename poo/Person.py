class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.Its_greetings = False
        self.it_was_presented = False

    def greeting(self):
        self.Its_greetings = True
        print(self.name, ",Esta saludando")

    def presented(self):
        self.it_was_presented = True
        print("mucho gusto soy,", self.name, "tengo",
              self.age, "y mi profecion es", self.profession)


person1 = Person("juan andres", "20 años", "ingeniero informatico")
print("Mi nombre es:", person1.name)
print("Tengo", person1.age)
print("estoy estudiando:", person1.profession)
person1.greeting()
person1.presented()

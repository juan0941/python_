print("EL PERRO 1")
print("                                ")


class Animals:
    def __init__(self, name, race, years, color):
        self.name = name
        self.race = race
        self.years = years
        self.color = color
        self.is_Awake = False
        self.is_Eating = False
        self.is_Asleep = False

    def awake(self):
        self.is_Awake = True
        print("El perro esta despierto")

    def eat(self):
        self.is_Eating = True
        print("El perro esta comiendo")

    def asllep(self):
        self.is_Asleep = True
        print("El perro se durmio")


Animals1 = Animals("boster", "doberman", "7 años", "negro")
print("El nombre del perro es:", Animals1.name)
print("La raza del perro es:", Animals1.race)
print("El perro tiene", Animals1.years)
print("El color del perro es:", Animals1.color)
Animals1.awake()
Animals1.eat()
Animals1.asllep()
# ////////////////////////////////////////////////////////////////////
print("                                ")
print("EL GATO")
print("                                ")


class cat(Animals):
    def __init__(self, name, race, years, color, numbre_leg):
        super().__init__(name, race, years, color)
        self.number_leg = numbre_leg

    def leg(self):
        print(f"El gato tiene {self.number_leg} patas")


class dog(Animals):
    def __init__(self, name, race, years, color, name_owner):
        super().__init__(name, race, years, color)
        self.name_owner = name_owner

    def owner(self):
        print(f"{self.name_owner} es el dueño de", self.name)


cat1 = cat("manchas", "persa", "5: años", "blanco y negro", 4)
print("El gato se llama:", cat1.name)
print("La raza del gato es:", cat1.race)
print("El gato tiene,", cat1.years)
print("El gato es de color:", cat1.color)
cat1.leg()
print("                                ")
print("EL PERRO 2")
print("                                ")
dog1 = dog("lucas", "chihuahua", "3: años", "cafe", "Daniel")
print("El perro se llama:", dog1.name)
print("La razza del perro es:", dog1.race)
print("EL perro tiene", dog1.years)
print("El color del perro es:", dog1.color)
dog1.owner()

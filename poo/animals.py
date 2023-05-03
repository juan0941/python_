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

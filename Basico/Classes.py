# CLASS

class Persona:
    # Constructor
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def fullname (self):
        print(f"Mi nombre completo es: {self.name} {self.surname}")

#p1 = Persona("Adrian", "Belarte")
#p2 = Persona("David", "Peris")
#print(f"{p1.name} {p1.surname}")
#print(f"{p2.name} {p2.surname}")
#p1.fullname()
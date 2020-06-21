class Crow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def caw(self):
        print("CAAAAAW!")


class Murder:
    def __init__(self):
        self.crows = []

    # Magic method to overload + operator
    def __add__(self, crow):
        self.crows.append(crow)

    # Magic method to override len() function
    def __len__(self):
        return len(self.crows)


crow = Crow("Mr. Crow", 7)

murder = Murder()

murder + crow

print(len(murder))

murder.crows[0].caw()


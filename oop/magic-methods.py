class Crow:
    # __init__ is a magic method, or Dunder method.
    # Dunder here means “Double Under (Underscores)”
    # Magic methods start and end with '__'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Magic method to return string of object
    # Like .toString() override in Java
    def __str__(self):
        # f-strings - 'formatted string literals' - can be used for string formatting
        return f"Name: {self.name}, Age: {self.age}"

    def caw(self):
        print("CAAAAAW!")


class Murder:
    def __init__(self):
        self.crows = []

    def add_crow(self, crow):
        self.crows.append(crow)

    # Magic method to override len() function
    def __len__(self):
        return len(self.crows)


crow = Crow("Mr. Crow", 7)
print(crow)  # Calls __str__ method

murder = Murder()
murder.add_crow(crow)
murder.add_crow(crow)

print(len(murder))  # Calls __len__ method

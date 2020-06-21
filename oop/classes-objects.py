class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Crow(Bird):
    # Constructor
    # 'self' is a reference to the created instance of the class
    def __init__(self, name, age):
        super().__init__(name, age)
        self.color = "black"

    # Class method. The 'self' parameter is mandatory
    def caw(self):
        print("CAAAAAW!")


crow = Crow("Mr. Crow", 7)

print(crow.name)
print(crow.age)

crow.caw()


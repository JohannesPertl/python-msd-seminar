class User:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def password(self):
        return "Access denied!"

    @password.setter
    def password(self, value):
        self._password = value


user = User("Max", "Mustermann", "test123")

print(user.full_name)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + " " + self.age

human1 = Human("Ville", "20")
human2 = Human("Pekka", "66")

print(human1)
print(human2)
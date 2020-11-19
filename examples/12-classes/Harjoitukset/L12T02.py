class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return self.name + ", " + self.color
    @classmethod
    def classmethod(cls):
        return "miau"
    
cat1 = Cat("Minttu", "Ruskea")
cat2 = Cat("Paavo", "Beige")

print(cat1, cat1.classmethod())
print(cat2, cat2.classmethod())
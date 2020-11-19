class car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def description(self):
        desc_str = "%s %s, hinta %s" % (self.brand, self.model, self.price)
        return desc_str
    
car1 = car("Skoda", "Octavia", 3000)
car2 = car("Audi", "A4", 4000)
car3 = car("Volvo", "V70", 5000)

print(car1.description())
print(car2.description())
print(car3.description())

yhteenlaskettu = car1.price + car2.price + car3.price
print("Autojen hinta yhteensä on", yhteenlaskettu)

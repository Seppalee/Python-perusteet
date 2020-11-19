import random
car_brands = ["Audi", "BMW", "Ford", "Opel", "Skoda", "Volvo", "Volkswagen"]

class car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def __str__(self):
        return self.brand + ", " + str(self.price)
    

cars = []
for i in range(5):
    carobject = car(random.choice(car_brands), random.randrange(1000,10000))
    cars.append(carobject)

for car in cars:
    print(car)
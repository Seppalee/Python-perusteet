from vehicle import Vehicle

car = Vehicle("Datsun", "100A", 998, 12)
car2 = Vehicle("Toyota", "Celica", 1588, 43)

# print car info
print(car)
print(car2)
print("car power is: ", car.horsepower(), "hp")
print("car2 power is: ", car2.horsepower(), "hp")
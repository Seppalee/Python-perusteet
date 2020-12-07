fruits = ["Orange", "Banana", "Carambola", "Apple"]

try:
    fruits[4] = "Kiwi"
except IndexError:
    print("Cant replace items outside list index!")
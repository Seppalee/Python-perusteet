def show_info():
    print("I'm Utils.info")

def subtract(number1, number2):
    return number1 - number2

def average(lst):
    return sum(lst) / len(lst)

def calc_consumption(kulutus, hinta, matka):
    matka_jaettu = matka / 100
    kokonaiskulutus = matka_jaettu * kulutus
    return kokonaiskulutus * hinta
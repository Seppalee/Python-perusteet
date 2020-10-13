from utils import calc_consumption

matka = float(input("Matkan pituus: "))
kulutus = float(input("Paljonko auton keskikulutus on: "))
hinta = float(input("Polttoaineen hinta per litra: "))

print("Matkaan kuluu", round(calc_consumption(matka, kulutus, hinta)), "euroa")
unit = str(input("Ohjelma muuttaa lämpötilayksikön pyöristäen kahden desimaalin tarkkuuteen. Valitse Celsius (c) tai Fahrenheit (f): "))
if unit == "c":
    temp = float(input("Syötä lämpötila Celsiusasteina: "))
    tulos = float((9 * temp) / 5 + 32)
    print("Antamasi lämpötila Fahrenheiteina on:", round(tulos, 2))
elif unit == "f":
    temp = float(input("Syötä lämpötila Fahrenheiteina: "))
    tulos = float((temp - 32) * 5 / 9)
    print("Antamasi lämpötila Celsiusasteina on", round(tulos, 2))
else:
    print("Väärä syöte, yritä uudelleen")
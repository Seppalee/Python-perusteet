import statistics
arvosanat = []

while True:
    try: 
        inp = int(input("Syötä arvosanoja väliltä 0-5, lopeta tyhjällä syötteellä: "))
    except ValueError:
        break
    else:
        if 0 <= inp <= 5:
            arvosanat.append(inp)
        elif inp > 5:
            print("Syötä lukuja väliltä 0-5")

x = statistics.mean(arvosanat)
y = len(arvosanat)
rounded = round(x, 2)

print("Antamiesi arvosanojen keskiarvo on", rounded, "kahden desimaalin tarkkuudella")
print("Syötit", y, "arvosanaa")
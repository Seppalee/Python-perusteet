saldo = 60
print("Tilisi saldo on", saldo, "euroa")
x = int(input("Kuinka monta euroa tilille lisätään? "))
y = float(input("Kuinka monta senttiä tilille lisätään? "))
b = y / 100
print("Tililläsi on", saldo + x + b)
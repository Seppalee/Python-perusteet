items = ["A", "B", "C", "D", "E"]

print(items)
while True:
    try:
        index = int(input("Mihin kohtaan taulukkoa haluat syöttää uuden tekstin?: "))
        new_text = str(input("Millä tekstillä haluat korvata sen?: "))
        items[index] = new_text
        break
    except IndexError:
        print("Indeksi ei ole kelvollinen, yritä uudestaan")

print(items)

lista=[]
while True:
    answer = input("Syötä oppilaiden nimiä, lopeta tyhjällä syötteellä: ")
    if not answer:
        break
    lista.append(answer)

print(*lista, sep=", ")
print("Nimiä on yhteensä", len(lista))
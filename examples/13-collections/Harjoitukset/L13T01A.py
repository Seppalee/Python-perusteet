rekisteri = []
while True:
    inp = input("Syötä rekisterinumeroita, lopeta tyhjällä syötteellä: ")
    if inp != "":
        rekisteri.append(inp)
    if inp == "":
        break

print(sorted(rekisteri))
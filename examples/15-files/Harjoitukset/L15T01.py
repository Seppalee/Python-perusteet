import pickle
filename = "names.dat"
surnames = []

while True:
    surname_input = input("Anna sukunimiä, lopeta tyhjällä syötteellä: ")
    if surname_input == "":
        try: 
            file = open(filename, "wb")
            pickle.dump(surnames, file, pickle.HIGHEST_PROTOCOL)
        except:
            print("Tiedoston kirjoittaminen ei onnistunut")
        finally:
            file.close()
            surnames.clear()
        try:
            file = open(filename, "rb")
            surnames = pickle.load(file)
        except:
            print("Tiedoston lukeminen epäonnistui")
        finally:
            file.close()
            print(surnames)
            break
    else:
        surnames.append(surname_input)

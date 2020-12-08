import json

numbers = []
floats = []
filename1 = "wholenumbers.txt"
filename2 = "floatnumbers.txt"

while True:
    try:
        given_integer = float(input("Type a number: "))
        if given_integer.is_integer() is True:
            intnumber = int(given_integer)
            numbers.append(given_integer)
            continue
        else:
            floats.append(given_integer)
            continue
    except ValueError:
        print("Antamasi arvo ei sovi")

try:
    file = open(filename1, "w")
    json.dump(numbers, file)
except:
    print("Tiedoston", filename1, "kirjoittaminen epäonnistui")
finally:
    file.close()

try:
    file1 = open(filename2, "w")
    json.dump(floats, file1)
except:
    print("Tiedoston", filename2, "kirjoittaminen epäonnistui")
finally:
    file1.close()
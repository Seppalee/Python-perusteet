number = 0
count = 0

while True:
    try:
        number += int(input("Syötä lukuja, lopeta tyhjällä syötteellä "))
    except (SyntaxError, ValueError):
        break
    count += 1
print("Syötit", count, "lukua ja niiden summa on", number)
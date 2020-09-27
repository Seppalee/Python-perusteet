luku1 = int(input("Anna kokonaisluku "))
luku2 = int(input("Anna toinen kokonaisluku "))
luku3 = int(input("Anna vielä yksi kokonaisluku "))

if luku1 > luku2 and luku1 > luku3:
    print(luku1)

elif luku2 > luku1 and luku2 > luku3:
    print(luku2)

elif luku3 > luku1 and luku3 > luku2:
    print(luku3)
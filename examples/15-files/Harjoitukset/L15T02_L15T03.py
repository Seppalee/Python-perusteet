from collections import Counter

f = open("C://Users/leevi/Documents/Koulu/Ohjelmointi/ttc2030/examples/15-files/Harjoitukset/nimet.txt", "r")
data = f.readline()
f.close()

total = data.split(", ")
print("Nimiä on yhteensä", len(total))

print(Counter(total))

print("Nimet lajiteltuna:")
sort = sorted(data.split(", "))
print(sort)
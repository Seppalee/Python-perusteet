age = int(input("Give me your age: "))

if age < 10:
    print("child")

elif age > 13 and age <= 19:
    print("teen")

elif age > 20 and age <= 65:
    print("adult")

else:
    print("senior")

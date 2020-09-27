number = int(input("Gimme a number: "))

if number == 10:
    print("number is 10")
    print("It really is 10")
elif number < 10:
    print("Number is less than 10")
elif number >= 20:
    print("Number is greater or equal to 20")
else:
    print("Number is in between 11 and 19")

number = int(input("Gimme a number: "))
if number > 0 and number < 10:
    print("number is in between 1 and 9")
elif number >= 10 or number == 0:
    print("number is 10 or greater, or number is 0")


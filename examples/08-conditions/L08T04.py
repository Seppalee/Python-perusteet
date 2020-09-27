arvosana = int(input("Anna oppilaan pistemäärä "))

if arvosana == 0 or arvosana == 1:
    print("0")

elif arvosana == 2 or arvosana == 3:
    print("1")

elif arvosana == 4 or arvosana == 5:
    print("2")

elif arvosana == 6 or arvosana == 7:
    print("3")

elif arvosana == 8 or arvosana == 9:
    print("4")

elif arvosana < 10 or arvosana <= 12:
    print("5")

else:
    print("Pistemäärä invalid")
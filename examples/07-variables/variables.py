number = 5
accountBalance = 110.54
print(number)
print(accountBalance)

number = 55
number2 = number + 2
# value of number 2 is now 57
print ("number2 is ", number2)

name = "Leevi"
lastName = "Seppäläinen"

# add string to string
fullName = name
fullName = name + " " + lastName
print(fullName)

# use Format function
age = 19
fullName = "First name {}. Last name {}. Age {}.".format(name, lastName, age)
print(fullName)

# access characters in a string
text = "ABC"
a = text[0]
b = text[1]
c = text[2]
print("Second char is " + b)

print("Text length is ", str(len(text)), " characters")

text2 = "ABD"
if text == text2:
    print("Texts are identical.")
else:
    print("Texts are NOT identical.")

# read text from console
line= input("Enter your text here: ")
print("You entered: ", line)

# read a number
line = input("Enter a number: ")
number = int(line)
print("Number is ", number)
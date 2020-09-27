number = 10
while number >=0:
    print(number)
    number -= 1

number = 10
while number >= 0 and number >100:
    number -= 1

for i in range(10):
    print("Looping", i)

for i in range(5,10):
    print("Looping 5,10", i)

for i in range(0, 10, 2):
    print("Looping 0,10,2", i)

for c in "Basic of programming with Python":
    print(c)

names = ["John", "Cherry", "Jack"]
for name in names:
    print(name)

# use of break and continue
print("Running while loop with break and continue")
number = 0
while True:
    number = int(input("Enter a number (0 to exit, 100 ignored) "))
    if number == 100:
        print("ingored")
        continue
    if number == 0:
        break

    print("You entered:", number)
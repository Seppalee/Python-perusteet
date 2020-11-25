try: 
    number1 = 100
    number2 = 0
    result = number1 / number2
    print("Result is " + str(result))
except ZeroDivisionError:
    print("Cant divide by zero!")

try: 
    number = int(input("Give a number: "))
    print("You entered: ", number)
except ValueError:
    print("Unable to convert to number")
except:
    print("Something else went wrong :(")

try: 
    numbers = [1, 2, 3, 4, 5]
    print("Last number is ", numbers[5])
except IndexError:
    print("Wrong index used in accessing list")

def safe_division(x, y):
    if y == 0:
        raise Exception("Exception from safe_division")
    return x / y

try:
    result = safe_division(100, 0)
except:
    print("safe_division raised an exception")

def someday_something_here():
    raise NotImplementedError("This function is not implemented currently")

someday_something_here()
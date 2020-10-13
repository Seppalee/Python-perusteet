from helper import sub

def print_info():
    print("info")

def print_and_return_number():
    print("Info - returning 123")
    return 123

def sum(number1, number2):
    return number1 + number2

def modify_text(text):
    text += ", this is added by function"
    print(text)

print("App started")
print_info()

number = print_and_return_number()
print("function returned ", number)

arg1 = 5
arg2 = 11
number = sum(arg1, arg2)
print("sum returned ", number)

text = "About to call modify_text"
modify_text(text)

number = sub(5, 11)
print("sub returned", number)

print("App done")
# use some random numbers to observe in debugger
from random import *

def step():
    print("Inside the 'step' function")
    print("All done here, exiting step function")

# declare couple of int variables
# observe the number2 in debugger to see what number is assigned to it
number1 = 10
number2 = randint(0, 100)

# print the values of our variables
print("value of number1 is ", number1)
print("value of number2 is ", number2)

# quite typical task of swapping value between two variables
# use the debugger to observer how value in variables change while stepping
# thru the code
temp = number1
number1 = number2
number2 = temp

# use the debugger to step over the function call
# then run the debugger again and use the 'Step Into' option instead
# run the debugger one more time, use 'Step Into', and inside the
# function, use 'Step Out' option.
step()

print("debugger.py, all done, exiting.")
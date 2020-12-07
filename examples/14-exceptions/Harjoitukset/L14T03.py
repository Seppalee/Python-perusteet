def isthiszero(num):
    if int(num) == 0:
        return True
    elif num != 0:
        return False
    else:
        return TypeError

try:
    print(isthiszero(0))
except TypeError:
    print("Given parameter is not a number")
    
 

# declare tuple of names and print
nametuple = ("Joe", "Sally", "Liam", "Robert", "Emma", "Isabella")
print("Contents of nametuple is:", nametuple)

# tuple items are accessed with [] operator
# index is zero based
print("Tuple element at index 1 is:", nametuple[1])

# index to access tuple can be negative
# negative index means beginning from the end
print("Tuple element at index -1: ", nametuple[-1])

# index can be also specified as a range
print("Tuple elements at range 2:5: ", nametuple[2:5])

# tuple can be converted to a list
namelist = list(nametuple)
namelist [1] = "Mary"
# and list can be converted to a tuple
nametuple = tuple(namelist)
print("Contents of nametuple is:", nametuple)

# tuple with only one item must be declared with trailing comma
nametuple = ("Joe",)
print("Contents of nametuple is:", nametuple)
print(type(nametuple))

# note that on below the variable is not a tuple
nametuple = ("Joe")
print(type(nametuple))

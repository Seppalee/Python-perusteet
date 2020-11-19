# declare a set of names and print
nameset = {"Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"}
print("Contents of nameset is:", nameset)

# print contents of the set in for loop
for name in nameset:
    print(name)

# use len function to check set length
print("Length of the set is:", len(nameset))

# check if certain item is in the set
name = "Sally"
print(name + " is in set:", name in nameset)

nameset.add("Bella")
print("Contents of nameset after add is:", nameset)

nameset.update({"Harry", "Elisa", "Pochahontas"})
print("Contents of nameset after update is:", nameset)

nameset.remove("Liam")
print("Contents of nameset after remove is:", nameset)

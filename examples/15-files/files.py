import os.path
import pickle

from vehicle import Vehicle

filename = "files-example.txt"
file = open(filename, "w")
file.write("Creating a file with Python!")
file.close()

# trying to write a file to drive root
filename = "files-example.txt"
try:
    file = open("C:\\" + filename, "w")
    file.write("Trying to write to drive root, its not going to work :(")
    file.close()
except:
    print("Failed to create file to drive root")

# get the user home folder, create new subfolder and write the file there
path = os.path.expanduser("~/files-example")
if not os.path.exists(path): os.makedirs(path)
path += "/"

file = open(path + filename, "w")
file.write("Files example, writing file to users home folder")
file.close()

# write multiple lines of text into a file
filename = "multiline-text.txt"
lines = [ "First line\n", "Second line\n", "Third line\n" ]
try: 
    file = open(path + filename, "w")
    file.writelines(lines)
except Exception as e:
    print("Failed to write file: " + filename)
finally:
    file.close()

# read back the text lines from the file
lines = [""]
try:
    file = open(path + filename, "r")
    lines = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

print(lines)

# declare a list of Vehicle objects
vehicles = []
vehicles.append(Vehicle("Datsun", "Sunny", 1197, 29))
vehicles.append(Vehicle("BMW", "m5", 4899, 294))
vehicles.append(Vehicle("Toyota", "Supra", 2999, 200))
vehicles.append(Vehicle("Plymouth", "Cuda", 6845, 597))

# print the contents of vehicle list
for vehicle in vehicles:
    print(vehicle)

# write the list of objects to a binary file
filename = "vehicles.dat"
try:
    file = open(path + filename, "wb")
    pickle.dump(vehicles, file, pickle.HIGHEST_PROTOCOL)
except:
    print("Failed to write file: " + filename)
finally:
    file.close()

# objects are now saved into the file, clear the list
vehicles.clear()
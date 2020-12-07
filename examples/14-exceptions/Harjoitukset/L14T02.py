try:
    open("C:\\", "r")
except FileNotFoundError:
    print("Did not find this file. Please try something else")

filename = "ayho.txt"
try:
    file = open("C:\\" + filename, "w")
    file.write("Ayho")
    file.close()
except PermissionError:
    print("You do not have permission to create a file here")

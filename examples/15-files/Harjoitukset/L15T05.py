import random
import json
filename = "lottery.txt"

lotterynumbers = random.sample(range(1,41), 7)

file = open(filename, "w")
json.dump(lotterynumbers, file)
file.close()


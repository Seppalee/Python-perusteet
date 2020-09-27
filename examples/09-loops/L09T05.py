import random
lottonumerot = random.sample(range(1,40), k=7)
lottonumerot.sort()
print("Numerosi ovat {}, {}, {}, {}, {}, {}, {} ".format(*lottonumerot))
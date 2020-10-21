import datetime

def muutos(n):
    return datetime.timedelta(seconds = n)

n = int(input("Anna aika sekunteina: "))
print(muutos(n))
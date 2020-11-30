cars_list = {
    "ABC-941": "Volkswagen",
    "QOE-182": "Hyundai",
    "MAO-999": "Opel",
    "XXZ-191": "Aston Martin",
    "BBQ-112": "Ford",
    "POS-565": "Ferrari",
    "DAS-414": "Mustang",
    "POE-312": "BMW",
    "YXZ-662": "Volvo",
    "WWW-010": "Renault",
}

print("Lajiteltu Rekisterikilven mukaan")
for k, v in sorted(cars_list.items()):
    print(k, v)

print("Lajiteltu merkin mukaan")
for k, v in sorted(cars_list.items(), key=lambda p:p[1]):
    print(k, v)
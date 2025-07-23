def sort_on(items):
    return items["num"]

vehicles = [
    {"car": 7},
    {"plane": 10},
    {"boat": 2}
]

vehicles.sort(reverse=True, key=sort_on)
print(vehicles)




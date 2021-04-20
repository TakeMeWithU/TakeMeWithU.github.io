import csv

class Meal:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

listMeal = []

# Using readlines()
file1 = open('/home/ble/Desktop/TakeMeWithU.github.io/assets/data/Plats.csv', 'r')
lines = file1.readlines()
lines.pop(0)
for line in lines:
    line = line.replace('\n', '')
    print(line)
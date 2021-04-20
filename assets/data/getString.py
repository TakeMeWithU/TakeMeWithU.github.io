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
    values = line.split(';')
    html = ''
    html += '<div class="col-lg-6 menu-item filter-' + values[3] + '">'
    html += '<img src="assets/img/menu/' + values[3] + '/' + values[6] + '.jpg"' 
    html += 'class="menu-img" alt="' + values[1] + '"/>'
    html += '<div class="menu-content"><a>'
    html += values[1] + '</a><span>' + values[4] + '€</span></div>'
    html += '<div class="menu-ingredients">'+ values[2] + values[5] +'</div></div>'
    print(html)
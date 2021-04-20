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
    
    html = ""
    html += "<div class='col-lg-6 menu-item filter-" + values[2] + "'>"
    html += '<img src="assets/img/menu/'+ values[2] +'/raviolisFrits.jpg" class="menu-img" alt="">'
    html += '<div class="menu-content">'
    html += '<a>'+ values[1] + '</a><span>' + values[3] + '€</span></div>'
    html += '<div class="menu-ingredients">('+ values[4] +'pcs)</div></div>'
    print(html)

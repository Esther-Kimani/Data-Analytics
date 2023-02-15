"""TASK

2. Find The most sold product line per gender
"""
from itertools import count
import pandas as pd

sa = pd.read_excel("supermarket.xlsx")

print(sa)

#getting the productline column for gender and prduct line

gender = sa['Gender'].values

productline = sa['Product line'].values

quantity = sa['Quantity'].values

myList = list(zip(gender, productline, quantity))

print(myList)

#seperate purchases by gender
femalePurchases = [(theGender, category, qty) for theGender, category, qty in myList if theGender == 'Female']

malePurchases = [(theGender, category, qty) for theGender, category, qty in myList if theGender == 'Male']

#
healthandBeauty_total = 0
electronicaccesories_total = 0
homeandlifestyle_total = 0
sportsandtravel_total = 0
foodandbeverages_total = 0
fashionaccessories_total = 0

for theGender, category, qty in femalePurchases:
    if category == "Health and beauty":
        healthandBeauty_total += qty
    elif category == "Electronic accessories":
        electronicaccesories_total += qty  
    elif category == "Home and lifestyle":
        homeandlifestyle_total += qty
    elif category == "Sports and travel":
        sportsandtravel_total += qty
    elif category == "Food and beverages":
        foodandbeverages_total += qty
    elif category == "Fashion accessories":
        fashionaccessories_total += qty 

print(" Female health and beauty total", healthandBeauty_total)  
print("Female electronic accessories total", electronicaccesories_total)
print("Female home and lifestyle total", homeandlifestyle_total)
print("Female sports and travel total", sportsandtravel_total)   
print("Female food and beverage total", foodandbeverages_total)
print("Female fashion accessories total", fashionaccessories_total)         

for theGender, category, qty in malePurchases:
    if category == "Health and beauty":
        healthandBeauty_total +=  qty  
    elif category == "Electronic accessories":
        electronicaccesories_total +=  qty    
    elif category == "Home and lifestyle":
        homeandlifestyle_total +=  qty  
    elif category == "Sports and travel":
        sportsandtravel_total +=  qty  
    elif category == "Food and beverages":
        foodandbeverages_total +=  qty  
    elif category == "Fashion accessories":
        fashionaccessories_total += qty  

print("Male health and beauty total", healthandBeauty_total)  
print("Male electronic accessories total", electronicaccesories_total)
print("Male home and lifestyle total", homeandlifestyle_total)
print("Male sports and travel total", sportsandtravel_total)   
print("Male food and beverage total", foodandbeverages_total)
print("Male fashion accessories total", fashionaccessories_total)    
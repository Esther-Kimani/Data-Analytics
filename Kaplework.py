import pandas as pd

lp = pd.read_excel("supermarket.xlsx")

print(lp)

#getting the productline column

productLine = lp['Product line'].values

print(productLine)

#converting the product line into a list

productlineList = list(productLine)

print(productlineList)

totalList = lp['Total'].values

print(totalList)

#we first convert into a list then zip
zipped = list(zip(productlineList, totalList))

print(zipped)

# to remove duplicates from list 

results = []

[results.append(x) for x in productlineList if x not in results]

#printing list after removal

print("The list after removing duplicates:" + str(results))

#
healthandBeauty_total = 0
electronicaccesories_total = 0
homeandlifestyle_total = 0
sportsandtravel_total = 0
foodandbeverages_total = 0
fashionaccessories_total = 0


for productLine,total in zipped:
    if productLine == "Health and beauty":
        healthandBeauty_total += total
    elif productLine == "Electronic accessories":
        electronicaccesories_total += total  
    elif productLine == "Home and lifestyle":
        homeandlifestyle_total += total  
    elif productLine == "Sports and travel":
        sportsandtravel_total += total
    elif productLine == "Food and beverages":
        foodandbeverages_total += total
    elif productLine == "Fashion accessories":
        fashionaccessories_total += total

print("health and beauty total", healthandBeauty_total)    
print("electronic accessories total", electronicaccesories_total)
print("home and lifestyle total", homeandlifestyle_total)
print("sports and travel total", sportsandtravel_total)   
print("food and beverage total", foodandbeverages_total)
print("fashion accessories total", fashionaccessories_total)        
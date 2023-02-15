# """TASK
# 1. Find all payment method per city
#"""

from itertools import count
import pandas as pd

sa = pd.read_excel("supermarket.xlsx")

print(sa)

#getting the productline column for cities

productlineCities = sa['City'].values

print(productlineCities)

productlinePayment = sa['Payment'].values

print(productlinePayment)

#we first convert into a list then zip
zipped = list(zip(productlineCities, productlinePayment))

print(zipped)

yangonPurchases = [(productlineCities, productlinePayment) for productlineCities, productlinePayment, in zipped if productlineCities == 'Yangon']
mandalayPurchases = [(productlineCities, productlinePayment) for productlineCities, productlinePayment, in zipped if productlineCities == 'Mandalay']
naypyitawPurchases = [(productlineCities, productlinePayment) for productlineCities, productlinePayment, in zipped if productlineCities == 'Naypyitaw']

print(yangonPurchases)
print(mandalayPurchases)
print(naypyitawPurchases)

count = 0
productlinePaymentwallet = 0 
for productlineCities, productlinePayment in yangonPurchases:
    if productlineCities == "Yangon":
        productlinePaymentwallet == "Ewallet"
        count
   

print(productlinePaymentwallet)            
#removing repetiotion within the cities

# citiesSingular = []

# [citiesSingular.append(x) for x in productlineCities if x not in citiesSingular]

# print("The cities in this analysis are:" + str(citiesSingular))

#removing repetiotion from the modes of payment

# modeofPayment = []

# [modeofPayment.append(x) for x in productlinePayment if x not in modeofPayment]

# print("The cities in this analysis are:" + str(modeofPayment))

#Checking what modes of payment were used in the cities
"""acities = {}
for productlineCities,productlinePayment in zip(productlineCities, productlinePayment):
    if productlineCities not in acities:
        acities[productlineCities]= [productlinePayment]
    else:
        acities[productlineCities].append(productlinePayment)
for productlineCities in acities:
        acities[productlineCities] = list(set(acities[productlineCities]))

for citproductlineCitiesy, productlinePayment in acities.items():
    print("city", productlineCities)
    print("payment", productlinePayment)
"""

"""for productlineCities,productlinePayment in zip(productlineCities, productlinePayment):
    if productlineCities == "Yangon":


        ewallet_total =+ productlinePayment
    elif productlinePayment == "Yangon":
        creditcard_total =+ productlinePayment
    elif productlinePayment == "Yangon":
        cash_total =+ productlinePayment     
    
print("Ewallet usage in Yangon",ewallet_total)"""

"""#
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
        fashionaccessories_total += qty    """ 

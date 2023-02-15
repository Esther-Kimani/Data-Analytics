#install pandas
#pip install pandas
#pandas will help us read excel files

#import xlrd
#pip install xlrd

import pandas as pd

#read data from the excel file
dataframe1 = pd.read_excel('Book1.xlsx')

#print(dataframe1)

#read age column
theAges = dataframe1['Age'].values

print(theAges)

#convert the above into a list
agesList = list(theAges)

print(agesList)

#how to find mean 
meanAge = sum(theAges) / len(theAges)
print(meanAge)

#maximum and minimum ages
maxAge = theAges.max()
print(maxAge)

minAge = theAges.min()
print(minAge)

#finding the country with the most users
#read country column
theCountry = dataframe1['Country'].values

print(theCountry)

#changing countries column into a list
countryList = list(theCountry)

print(countryList)

countKenya = countryList.count('Kenya')
countUganda = countryList.count('Uganda')
countZimbabwe = countryList.count('Zimbabwe')

print(countKenya)

countryDistribution = [countKenya, countUganda, countZimbabwe]
print(countryDistribution)

maxValue = max(countryDistribution)


global mostCountry

if maxValue == countKenya:
    mostCountry = "Kenya"
elif maxValue == countUganda:
    mostCountry = "Uganda"
elif maxValue == countZimbabwe:
    mostCountry = "Zimbabwe"
    
print(mostCountry)
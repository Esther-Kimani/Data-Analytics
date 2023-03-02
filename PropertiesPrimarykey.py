import mysql.connector

# create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20August1999",
  database = "propertiesandusers"
)
#create a database
new = mydb.cursor()

#new.execute("CREATE DATABASE propertiesAndusers")

#TO CHECK IF THE DATBASE EXISTS
# new.execute("SHOW DATABASES")
# for x in new:
#     print(x)

# new.execute ("CREATE TABLE userinfo(userid varchar (255),firstname varchar (255),lastname varchar(255),phonenumber int) ")
# sql="INSERT INTO userinfo (userid,firstname, lastname, phonenumber) VALUES (%s,%s,%s,%s)"
# val=[("BA1001","john","kariuki",722140),
#       ("BA1002","james","mwangi",721540),
#       ("BA1003","rose","ann",712303),
#       ("BA1004","jane","mbithe",101239),
#       ("BA1005","ruth","njambi",724390),
#       ("BA1006","joy","mwende",721405), 
#       ("BA10007","james","mwangi",722385),
#       ("BA1008","joan","wanjiku",721380),
#       ("BA1009","job","njenga",720410),
#       ("BA1010","jim","karangi",723398),
#       ]
# new.executemany(sql, val)
# mydb.commit()

# new.execute ("CREATE TABLE propertyowned(userid varchar (255),property varchar (255),town varchar(255))")
# sql="INSERT INTO propertyowned (userid,property,town) VALUES (%s,%s,%s)"
# val=[("BA1001","flat","kiambu"),
#       ("BA1002","land","meru"),
#       ("BA1003","apartment","mombasa"),
#       ("BA1004","townhouse","kisumu"),
#       ("BA1005","land","nakuru"),
#       ("BA1006","flat","nairobi"), 
#       ("BA10007","land","kajiando"),
#       ("BA1008","townhoouse","thika"),
#       ("BA1009","apartment","karen"),
#       ("BA1010","flat","mombasa")
#       ]
# new.executemany(sql, val)
# mydb.commit()

 #from the table userinfo get first/lastnames a nd from the table propertyowned get the infos and join the tabkes if the id's match
# sql = "SELECT userinfo.firstname, userinfo.lastname, propertyowned.property, propertyowned.town  FROM userinfo JOIN  propertyowned ON userinfo.userid = propertyowned.userid "

# new.execute(sql)
# result = new.fetchall()

# for x in result:
#    print(x)

#logic
# create a dict to map users ids to user data
 
# do the joiningh using for loop
# join the data and property data based on user id  
# 
# steps
# retrieve all the data on property from the sql database using seperate SELECT statements
# create a dct "users" that maps user ID's to ser data
# use the dict to join the user data and property data baed on the user id  


# Get the user data from the database
sql = "SELECT * FROM userinfo"
new.execute(sql)
user_result = new.fetchall()


# Get the property data from the database
sql = "SELECT * FROM propertyowned"
new.execute(sql)
property_result = new.fetchall()

users = {}

for row in user_result:
    user_id = row[0]
    users[user_id] = row[1:]  

    
print(users)

property = {} 

for row in property_result:
    user_id = row[0]
   # print(user_id)
    first_name, last_name, phone_number = users[user_id]
    property[user_id] = row[1:]
    property_name = row[1]
    property_town = row[2]
    print(first_name,last_name,"own property, namely:",property_name,"which is located in",property_town)



#new table
# new.execute ("CREATE TABLE loansissued(userid varchar (255),loanissued int,loanpaid int)")
# sql="INSERT INTO loansissued (userid,loanissued,loanpaid) VALUES (%s,%s,%s)"    
# val=[("BA1001","200000","0"),
#       ("BA1002","500000","250000"),
#       ("BA1003","100000","10000"),
#       ("BA1004","650000","150000"),
#       ("BA1005","300000","125000"),
#       ("BA1006","100000","5000"), 
#       ("BA10007","700000","0"),
#       ("BA1008","10000","0"),
#       ("BA1009","700000","250000"),
#       ("BA1010","1000000","750000")
#       ]
# new.executemany(sql, val)
# mydb.commit()  

# Get the loansissued from the database
sql = "SELECT * FROM loansissued"
new.execute(sql)
loansissued_result = new.fetchall()

print(loansissued_result)


users1 = {}

for row in user_result:
    user_id = row[0]
    print(loansissued_result)
    
    users1[user_id] = row[1:]  

#print(users1)

print("hey hey",property)
for row in loansissued_result:
    user_id = row[0]
    #print(loansissued_result)

    first_name, last_name, phone_number = users[user_id]
    property_name, property_town = property[user_id]
    loan_issued = row[1]
    loan_paid = row[2]
    #print(property_name) 
    print("A loan of",loan_issued, "was issued to",first_name, "to buy property in", property_town,
        "and what they have currently settled is",loan_paid)

import mysql.connector

# create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20August1999",
  database = "mydatabase"
)
#create a database
new = mydb.cursor()

#new.execute("CREATE DATABASE primarykey")

#TO CHECK IF THE DATBASE EXISTS
# new.execute("SHOW DATABASES")
# for x in new:
#     print(x)

# new.execute("Create table USERS(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255))")
listVariables = [("Jospeh Gikandi", "Kenya"),("Mary Wambui"," Kenya"),("Lisbet Wako", "Uganda"),("Wafula Nafula", "Tanzania"),
                  ("Roy Kim", "Tanzania"),("Litu Cab", "Uganda"),("Flossin Mauwano", "Kenya"),("Getrude Mwangi", "Uganda"),
                  ("Awino Awino", "Kenya")]

#sql = "INSERT INTO users (name, country) VALUES (%s, %s)"
#val = listVariables
#new.executemany(sql, val)
#mydb.commit

new.execute("SELECT * from USERS")
myresults = new.fetchall()

for x in myresults:
    print(x)


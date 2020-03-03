import requests
import mysql.connector

URL = "https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city=Rivne"

response = requests.get(URL)
print("res Result={0}", response)
data = response.json()

for item in data["devices"]:
    print(item["fullAddressEn"] + "\n" + item["cityEN"] +
          "\n"+item["latitude"]+"\n"+item["longitude"])
    print("===============================================================================================")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS privat")
mycursor.execute("SHOW DATABASES")

#mycursor.execute("USE privat")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="privat"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS devices (id INT AUTO_INCREMENT PRIMARY KEY, fullAddressEn VARCHAR(255), cityEN VARCHAR(255), latitude DECIMAL(8,6), longitude DECIMAL(8,6))")

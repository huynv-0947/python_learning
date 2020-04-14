import mysql.connector

db = mysql.connector.connect(
  host =  "localhost",
  user = "root",
  passwd = "password"
)

cursor = db.cursor()

# some command
cursor.execute("CREATE DATABASE mydatabase")

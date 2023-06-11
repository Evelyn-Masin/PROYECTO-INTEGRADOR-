import mysql.connector

midb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Prueba!123",
    database = "bd_ejemplo_big_bread_sa"
)
print(midb)
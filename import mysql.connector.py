import mysql.connector

midb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Prueba!123",
    database = "proyecto_bigbread"
)
print(midb)


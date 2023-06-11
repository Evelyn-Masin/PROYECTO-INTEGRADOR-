import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host= 'localhost'
        port= '3306'
        user= 'root'
        password='Panda2013'
        db= 'condominio'
        )

    if conexion. is_connected():
        print("conexiòn exitosa")
        cursor=conexion.cursor()
        cursor.execute("SELECT data base();")
        registro=cursor.fetchone()
        print("Conectado a la BD:",registro)
except Error as ex:
    print("Error de conxiòn", ex)
finally:
    if connexion.is_connected():
        connexion.close() # Se cerro conexiòn a la BD

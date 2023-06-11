import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host= 'localhost'
        port= '3306'
        user= 'root'
        password='Panda2013'
        db= 'BD_EJEMPLO_Big_Bread_SA.sql'
        )

    if conexion. is_connected():
        print("conexiòn exitosa")
        cursor=conexion.cursor()
        cursor.execute("SELECT data base();")
        registro=cursor.fetchone()
        print("Conectado a la BD:",registro)
        cursor.execute("SELECT * FROM productos")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila[0], fila [1], fila [2])
        print("Total de registros", cursor.rowcount)
except Error as ex:
    print("Error de conexiòn", ex)
finally:
    if connexion.is_connected():
        connexion.close() # Se cerro conexiòn a la BD

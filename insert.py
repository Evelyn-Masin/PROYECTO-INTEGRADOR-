import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host= 'localhost'
        port= '3306'
        user= 'root'
        password='Panda2013'
        db= 'Base de Panaderia'
        )

    if conexion. is_connected():
        print("conexiòn exitosa")
        cursor=conexion.cursor()
        nombre=input("Ingrese nuevo producto:")
        # cursor.execute("INSERT INTO productos(codigo) VALUES ('pan salvado')")
        sentencia="INSERT INTO productos(codigo) VALUES ('{0}')".format(codigo)
        cursor.execute(sentencia)
        conexion.commit() # Confirma el ingreso del producto
        print("Registro nuevo insertado exitosamente")
except Error as ex:
    print("Error de conexiòn", ex)
finally:
    if connexion.is_connected():
        connexion.close() # Se cerro conexiòn a la BD

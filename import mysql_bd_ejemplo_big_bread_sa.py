import mysql.connector

class Conectar_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect (
                host = "localhost",
                user = "root",
                password = "Prueba!123",
                database = "bd_ejemplo_big_bread_sa"
            )
        except mysql.connector.Error as descripcionError:
            print ("No se conecto a la base de datos.", descripcionError)


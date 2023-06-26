import mysql.connector

class conexion():
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

def inserta_producto(self,codigo, producto, insumos, Produccion_diaria, resetas):
        cur = self.conexion.cursor()
        sql='''INSERT INTO producto (CODIGO, PRODUCTO, INSUMO, PRODUCCION DIARIA,RECETA) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, producto, insumos, Produccion_diaria, resetas)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM producto " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  


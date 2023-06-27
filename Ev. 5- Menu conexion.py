import mysql.connector  

midb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Prueba!123",
    database = "proyecto_bigbread"
)

print(midb)

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
  


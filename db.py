import pymysql

def connection():
    return pymysql.connect(host='localhost',user='root',password='',db='nombre_BD')

#Este es el archivo que nos permite conectar con la base de datos.
#Se debe cambiar las credenciales de acuerdo con las establecidas.
import pymysql

def conectar():
    return pymysql.connect(host='localhost',user='root',password='',db='easy_parking')

#Este es el archivo que nos permite conectar con la base de datos.
#Se debe cambiar las credenciales de acuerdo con las establecidas.
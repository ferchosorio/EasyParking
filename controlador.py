from db import connection()
#En este archivo se ejecutan las acciones que interactuan con la base de datos

def insertar_administracion(nombre,identificacion,telefono,email):
    conexion = connection()
    with conexion.cursor as cursor:
        cursor.execute("INSERT INTO administration(nombre,identificacion,telefono,email) VALUES (%s %s %s %s)",(nombre,identificacion,telefono,email))
        conexion.close()
#Esta función permite insertar los datos adquiridos mediante POST a la base de datos en la tabla administration

#Es solo un ejemplo para tener en cuenta, aún que así funciona.


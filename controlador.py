from db import conectar
#En este archivo se ejecutan las acciones que interactuan con la base de datos

def insertar_administracion(nom,idn,telf,mail,usu,cont):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO administration(nombre,identificacion,telefono,email,usuario,contrasena) VALUES (%s, %s, %s, %s, %s, %s)",(nom,idn,telf,mail,usu,cont))
        conexion.commit()
        conexion.close()
#Esta función permite insertar los datos adquiridos mediante POST a la base de datos en la tabla administration

#Es solo un ejemplo para tener en cuenta, aún que así funciona.


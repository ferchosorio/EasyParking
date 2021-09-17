from flask import Flask, request, render_template, redirect, flash
import controlador
app = Flask(__name__)

@app.route("/")
def EasyParking():
    return render_template("index.html")
#Esta es la página de inicio.
@app.route("/signup")
def signup():
    return render_template("signup.html")
#Página de ingreso de datos para el registro de usarios.

@app.route("/Data_Store", methods=['POST'])
def Data_Store():
    nombre = request.form['nombre']
    dni = request.form['identificacion']
    tel = request.form['telefono']
    mail = request.form['email']
    user = request.form['usuario']
    passw = request.form['contrasena']
    controlador.insertar_administracion(nombre,dni,tel,mail,user,passw)
    return redirect("/")
#Proceso de guardado de los datos adquiridos mediante POST
@app.route("/login")
def login():
    return render_template("login.html")
#Página de ingreso de credenciales para inicio de sesión.

@app.route("/consulta_credenciales", methods=['POST'])
def consulta_credenciales():
    return True
#Se consultará las credenciales proporcionadas con las almacenadas en la BD

@app.route("/controlPanel")
def controlPanel():
    return render_template("controlPanel.html")
#Panel de control de funciones del sistema
#Continuar con funciones del sistema
if __name__ == '__main__':
    app.run(port=3000,debug=True)

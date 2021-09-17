from flask import Flask,Request,render_template
app = Flask(__name__)

@app.route("/")
def EasyParking():
    return render_template("index.html")
#Esta es la página de inicio.
@app.route("/login", methods=['POST'])
def login():
    return render_template("login.html")
#Página de ingreso de credenciales para inicio de sesión.
@app.route("/controlPanel")
def controlPanel():
    return render_template("controlPanel.html")
#Panel de control de funciones del sistema
#Continuar con funciones del sistema
if __name__ == '__main__':
    app.run(port=3000,debug=True)

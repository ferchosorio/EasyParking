from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/easy_parking'
#Credenciales de configuración de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Propiedad para evitar warnings

db = SQLAlchemy(app)
ma = Marshmallow(app)
#Se pasan la configuración de app a el ORM y al esquema de Marshmallow

@app.context_processor
def fecha():
    return {'now': datetime.now()}
#Con esta función obtenemos la fecha actual

class easy_parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    administrador = db.Column(db.String(100))
    numero_plazas = db.Column(db.Integer)
    logotipo = db.Column(db.String(256))

    def __init__(self, administrador,numero_plazas,logotipo):
        self.administrador = administrador
        self.numero_plazas = numero_plazas
        self.logotipo = logotipo
#Clase para la tabla Easy_parking
class easy_parkingSchema(ma.Schema):
    class Meta:
        campos = ('id','administrador','numero_plazas','logotipo')
#Clase para el esquema de la tabla Easy_parking

easy_parking_schema = easy_parkingSchema()
easy_parking_schemas = easy_parkingSchema(many=True)

class administration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    identificacion = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    email = db.Column(db.String(100))
    fecha_registro = db.Column(db.Date)
    usuario = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))

    def __init__(self,nombre,identificacion,telefono,email,fecha_registro,usuario,contrasena):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono
        self.email = email
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        self.contrasena = contrasena
#Clase para la tabla administration
class administrationSchema(ma.Schema):
    class Meta:
        campos = ('id','nombre','identificacion','telefono','email','fecha_registro','usuario','contrasena')
#Clase para el esquema de la tabla administration

administration_schema = administrationSchema()
administration_schemas = administrationSchema(many=True)

class vehicles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipo_de_vehiculo = db.Column(db.String(100))
    plaza = db.Column(db.Integer)
    placa = db.Column(db.String(20))
    color = db.Column(db.String(100))
    propietario = db.Column(db.String(100))
    accesorios = db.Column(db.String(100))
    hora_entrada = db.Column(db.String(100))
    hora_salida = db.Column(db.String(100))
    tiempo_total = db.Column(db.Integer)
    fecha = db.Column(db.String(100))
    valor_a_pagar = db.Column(db.Integer)
    usuario = db.Column(db.String(100))

    def __intit__(self,tipo_de_vehiculo,plaza,placa,color,propietario,accesorios,hora_entrada,hora_salida,tiempo_total,fecha,valor_a_pagar,usuario):
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.plaza = plaza
        self.placa = placa
        self.color = color
        self.propietario = propietario
        self.accesorios = accesorios
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.tiempo_total = tiempo_total
        self.fecha = fecha
        self.valor_a_pagar = valor_a_pagar
        self.usuario = usuario

class vehiclesSchema(ma.Schema):
    class Meta:
        campos = ('id','tipo_de_vehiculo','plaza','placa','color','propietario','accesorios','hora_entrada','hora_salida','tiempo_total','fecha','valor_a_pagar','usuario')

vehicles_schema = vehiclesSchema()
vehicles_schemas = vehiclesSchema(many=True)

class billing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(100))
    entradas = db.Column(db.Integer)
    salidas = db.Column(db.Integer)
    balance = db.Column(db.Integer)

    def __init__(self,fecha,entradas,salidas,balance):
        self.fecha = fecha
        self.entradas = entradas
        self.salidas = salidas
        self.balance = balance

class billingSchema(ma.Schema):
    class Meta:
        campos = ('id','fecha','entradas','salidas','balance')

billing_schema = billingSchema()
billing_schemas = billingSchema(many=True)

db.create_all()
#Ejecutar creación de las tablas
@app.route("/")
def EasyParking():
    return render_template("main.html")
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
    fechaR = request.form['fechaR']
    user = request.form['usuario']
    passw = request.form['contrasena']
    new_administration = administration(nombre,dni,tel,mail,fechaR,user,passw)
    db.session.add(new_administration)
    db.session.commit()
    #flash("Registro exitoso")
    return redirect("/")
#Proceso de guardado de los datos adquiridos mediante POST
@app.route("/login")
def login():
    return render_template("login.html")
#Página de ingreso de credenciales para inicio de sesión.

@app.route("/consulta_credenciales", methods=['GET'])
def consulta_credenciales():
    return True
#Se consultará las credenciales proporcionadas con las almacenadas en la BD

@app.route("/controlPanel")
def controlPanel():
    return render_template("controlPanel.html")
#Panel de control de funciones del sistema
#Continuar con funciones del sistema
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)

import re
from flask import Flask, request, render_template, redirect, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import column_property
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost:5432/easy_parking'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://tnvqatouijtntl:eaf31c805ffcbd53ebc53bd6d6e62672019c78a12f940ce1870d9d5e7b15bd53@ec2-34-205-14-168.compute-1.amazonaws.com:5432/da1hekglelf4b9'
#Credenciales de configuración de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Propiedad para evitar warnings
app.config['SECRET_KEY'] = '123456'
#Define clave secreta para sesión
app.config['UPLOAD_FOLDER'] = "static/assets/images/Subidas"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
#Se pasan la configuración de app a el ORM y al esquema de Marshmallow

flag = 0

@app.context_processor
def fecha():
    return {'now': datetime.now()}
#Con esta función obtenemos la fecha actual
def fechaActual():
    now = datetime.now()
    return now.date()
def horaActual():
    now = datetime.now()
    horas = now.hour
    minutos = now.minute
    segs = now.second
    return f"{horas}:{minutos}:{segs}"

class easy_parking(db.Model):
    __tablename__ = 'easy_parking'
    id = db.Column(db.Integer, primary_key=True)
    administrador = db.Column(db.String(100))
    numero_plazas = db.Column(db.Integer)
    tMoto = db.Column(db.Integer)
    tAuto = db.Column(db.Integer)
    tCamion = db.Column(db.Integer)
    tOtro = db.Column(db.Integer)
    logotipo = db.Column(db.String(256))

    def __init__(self,administrador,numero_plazas,tMoto,tAuto,tCamion,tOtro,logotipo):
        self.administrador = administrador
        self.numero_plazas = numero_plazas
        self.tMoto = tMoto
        self.tAuto = tAuto
        self.tCamion = tCamion
        self.tOtro = tOtro
        self.logotipo = logotipo
#Clase para la tabla Easy_parking
class easy_parkingSchema(ma.Schema):
    class Meta:
        campos = ('id','administrador','numero_plazas','tMoto','tAuto','tCamion','tOtro','logotipo')
#Clase para el esquema de la tabla Easy_parking

easy_parking_schema = easy_parkingSchema()
easy_parking_schemas = easy_parkingSchema(many=True)

class administration(db.Model):
    __tablename__ = 'administration'
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
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key = True)
    tipo_de_vehiculo = db.Column(db.String(100))
    plaza = db.Column(db.Integer)
    placa = db.Column(db.String(20))
    color = db.Column(db.String(100))
    propietario = db.Column(db.String(100))
    accesorios = db.Column(db.String(100))
    hora_entrada = db.Column(db.String(100))
    hora_salida = db.Column(db.String(100))
    tiempo_total = db.Column(db.String(100))
    fecha = db.Column(db.String(100))
    valor_a_pagar = db.Column(db.Integer)
    usuario = db.Column(db.String(100))

    def __init__(self,tipo_de_vehiculo,plaza,placa,color,propietario,accesorios,hora_entrada,hora_salida,tiempo_total,fecha,valor_a_pagar,usuario):
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
    __tablename__ = 'billing'
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

class monthly(db.Model):
    __tablename__ = 'monthly'
    id = db.Column(db.Integer, primary_key=True)
    propietario = db.Column(db.String(100))
    placa = db.Column(db.String(20))
    tipo_de_vehiculo = db.Column(db.String(100))
    color = db.Column(db.String(100))
    fotografia = db.Column(db.String(256))
    plaza = db.Column(db.Integer)
    valor_a_pagar = db.Column(db.Integer)
    fecha_entrada = db.Column(db.String(100))
    fecha_salida = db.Column(db.String(100))

    def __init__(self,propietario,placa,tipo_de_vehiculo,color,fotografia,plaza,valor_a_pagar,fecha_entrada,fecha_salida):
        self.propietario = propietario
        self.placa = placa
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.color = color
        self.fotografia = fotografia
        self.plaza = plaza
        self.valor_a_pagar = valor_a_pagar
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

class monthlySchema(ma.Schema):
    class Meta:
        campos = ('id','propietario','placa','tipo_de_vehiculo','color','fotografia','plaza','valor_a_pagar','fecha_entrada','fecha_salida')

monthly_schema = monthlySchema()
monthly_schemas = monthlySchema(many=True)

db.create_all()
db.session.commit()
#Ejecutar creación de las tablas

@app.route("/panel")
def noPanel():
    return redirect("/")
@app.route("/login")
def noLogin():
    return redirect("/")
@app.route("/Data_Store")
def nodataStore():
    return redirect("/")
@app.route("/configurar")
def noconfig():
    return redirect("/")

@app.route("/")
def EasyParking():
    return render_template("main.html")
#Esta es la página de inicio.
@app.route("/signup")
def signup():
    return render_template("signup.html")
#Página de ingreso de datos para el registro de usarios.

@app.route("/inicioSesion")
def inicioSesion(par = None):
    return render_template("login.html",res = par)

@app.route("/Data_Store", methods=['POST'])
def Data_Store():
    if request.method == "POST":
        try:
            nombre = request.form['nombre']
            dni = request.form['identificacion']
            tel = request.form['telefono']
            mail = request.form['email']
            fechaR = request.form['fechaR']
            user = request.form['usuario']
            passw = request.form['contrasena']
            consulta = db.session.query(administration.identificacion,administration.usuario).filter(
                administration.identificacion == dni
            ).filter(
                administration.usuario == user
            )
            for dato in consulta:
                if dato[0] == dni and dato[1] == user:
                    return inicioSesion(0)
            new_administration = administration(nombre,dni,tel,mail,fechaR,user,passw)
            db.session.add(new_administration)
            db.session.commit()
            return inicioSesion(1)
        except:
            return inicioSesion(0)
#Proceso de guardado de los datos adquiridos mediante POST

@app.route("/configurar", methods=['POST'])
def configurar():
    if request.method == "POST":
        try:
            administrador = session['usu']
            numero_plazas = request.form['numero_plazas']
            tMoto = request.form['tarifaMoto']
            tAuto = request.form['tarifaAuto']
            tCamion = request.form['tarifaCamion']
            tOtro = request.form['tarifaCamion']
            tarMoto = tMoto.replace(".","")
            tarAuto = tAuto.replace(".","")
            tarCamion = tCamion.replace(".","")
            tarOtro = tOtro.replace(".","")
            f = request.files['logotipo']
            if f.filename == '':
                filename = "default_logo.png"
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            first_config = easy_parking(administrador,numero_plazas,tarMoto,tarAuto,tarCamion,tarOtro,filename)
            db.session.add(first_config)
            db.session.commit()
            return redirect(f"/panel/{administrador}")
        except:
            return panel(administrador)

@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        try:
            user = request.form['usuario']
            cont = request.form['contrasena']
            u = db.session.query(administration.usuario,administration.contrasena).filter(
                administration.usuario == user
            ).filter(
                administration.contrasena == cont
            )
            for i in u:
                if i[0] == user and i[1] == cont:
                    session['usu'] = i[0] #Se establece un valor para la sesión
                    ss = session['usu']
                    return redirect(f"/panel/{ss}")
            return inicioSesion(3)
        except:
            return inicioSesion(4)
#Página de ingreso de credenciales para inicio de sesión.

@app.route("/panel/<sesion>")
def panel(sesion):
    conf = 0
    logo = "default_logo.png"
    u = db.session.query(administration.usuario).filter(
        administration.usuario == sesion
    )
    config = db.session.execute("SELECT count(id) as c FROM easy_parking").scalar()
    if config > 0:
        conf = 1
        imagenes = db.session.query(easy_parking.logotipo).all()
        for imgn in imagenes:
            logo = imgn[0]
    for i in u:
        if sesion == i[0]:
            return render_template("panel.html",sesions=sesion,configs = conf,logo = logo)
        else:
            return inicioSesion(2)

@app.route("/vehiculos", methods=['POST'])
def vehiculos():
    if request.method == "POST":
        try:
            tipoVehiculo = request.form['tipoV']
            plaza = request.form['plaza']
            placa = request.form['placa']
            color = request.form['color']
            propietario = request.form['propietario']
            accesorios = request.form['accesorios']
            usuario = session['usu']
            horaEntrada = horaActual()
            horaSalida = "0:0:0"
            tiempoTotal = 0
            fechaA = fechaActual()
            pagar = 0
            newVehicles = vehicles(tipoVehiculo,plaza,placa,color,propietario,accesorios,horaEntrada,horaSalida,tiempoTotal,fechaA,pagar,usuario)
            db.session.add(newVehicles)
            db.session.commit()
            return ingresoVehiculo(1)
        except:
            return ingresoVehiculo(0)

@app.route("/ingresados")
def ingresados():
    ingre = db.session.query(vehicles).all()
    return render_template("ingresados.html",ing = ingre)

@app.route("/salidaVehiculo/<elem>")
def salidaVehiculo(elem):
    if elem:
        horaSalida = horaActual()
        tarf = db.session.query(easy_parking).all()
        for tarifa in tarf:
            tarM = tarifa.tMoto
            tarA = tarifa.tAuto
            tarC = tarifa.tCamion
        consul = db.session.query(vehicles).filter(
            vehicles.id == elem
        )
        for n in consul:
            horaE = n.hora_entrada
            tipoV = n.tipo_de_vehiculo
            c = horaE.split(":")
            s = horaSalida.split(":")
            hE = c[0]
            mE = c[1]
            hS = s[0]
            mS = s[1]
            hors = int(hS)-int(hE)
            mins = int(mS)+int(mE)
            if mins >= 60:
                hors+1
                mins=mins-60
            Thors = hors*60
            Tmins = Thors+mins
            tiempoT = f"{hors}:{mins}"
            if tipoV == "Motocicleta":
                if hors < 1 and mins > 0:
                    valor = tarM
                else:
                    if mins > 30:
                        hors + 1
                    valor = hors/3*tarM
                    if valor < tarM:
                        valor = tarM
            elif tipoV == "Automovil" or tipoV == "Camioneta":
                if hors < 1 and mins > 0:
                    valor = tarA
                else:
                    if mins > 30:
                        hors + 1
                    valor = hors/3*tarA
                    if valor < tarA:
                        valor = tarA
            elif tipoV == "Camion" or tipoV == "Otros":
                if hors < 1 and mins > 0:
                    valor = tarC
                else:
                    if mins > 30:
                        hors + 1
                    valor = hors/3*tarC
                    if valor < tarC:
                        valor = tarC
            n.hora_salida = horaSalida
            n.tiempo_total = tiempoT
            n.valor_a_pagar = round(valor)
            facturacion = billing(fechaActual(),valor,0,valor)
            db.session.add(facturacion)
            #dels = vehicles.query.filter_by(id=elem).first()
            #db.session.delete(dels)
            db.session.commit()
        return principal(valor)
        #return f"Tiempo: {tiempoT} == Minutos: {Tmins} == a pagar ${round(valor)}"

@app.route("/inMensual", methods=['POST'])
def inMensual():
    prop = request.form['propietario']
    pla = request.form['placa']
    tipv = request.form['tipoV']
    colo = request.form['color']
    f = request.files['foto']
    if f.filename == '':
        filename = "default_logo.png"
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    plaz = request.form['plaza']
    valP = request.form['valorPagar']
    fechaSal = request.form['fechaSalida']
    ins = monthly(prop,pla,tipv,colo,filename,plaz,valP,fechaActual(),fechaSal)
    db.session.add(ins)
    db.session.commit()
    return redirect("/mensual")

@app.route("/principal")
def principal(vl=None):
    cos = db.session.query(vehicles).filter(
        vehicles.hora_salida == "0:0:0"
    )
    co = db.session.execute("SELECT count(id) as c FROM vehicles").scalar()
    return render_template("principal.html",vehics=cos,vals = vl,cs = co)

@app.route("/mensual")
def mensualidad():
    consu = db.session.query(monthly).all()
    return render_template("mensual.html",dats = consu)

@app.route("/controlPanel")
def controlPanel():
    return render_template("controlPanel.html")
#Panel de control de funciones del sistema

@app.route("/ingresar_vehiculo")
def ingresoVehiculo(par = None):
    return render_template("ingreso_vehiculo.html", usr = session['usu'],res = par)

#Continuar con funciones del sistema

@app.errorhandler(404)
def no_encontrado(error):
    return render_template("error.html", errors = 404),404

@app.errorhandler(405)
def no_encontrado(error):
    return render_template("error.html", errors = 405),405

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)

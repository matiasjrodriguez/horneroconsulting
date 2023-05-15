from flask import Flask, render_template, url_for, request
from conexionpostgresql import ConexionPostgreSQL
import os


app = Flask(__name__)

conexion = ConexionPostgreSQL(
    os.getenv("rHOST"),
    "5432",
    "contacto",
    "mjrodriguez",
    os.getenv("rPASSWORD")
)

@app.route('/healthz', methods=['GET'])
def healthz():
    return 200

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    nombre = request.form.get('nombre')
    email = request.form.get('mail')
    whatsapp = request.form.get('whatsapp')
    mensaje = request.form.get('mensaje')

    conexion.conectar()
    conexion.insertar_datos(nombre, email, whatsapp, mensaje)
    conexion.desconectar()

    return render_template('index.html', success_message='Gracias por contactarnos', host=os.getenv("rHOST"), password=os.getenv("rPASSWORD"))

@app.route('/favicon.ico')
def favicon():
    import os
    from flask import send_from_directory

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'Pajaro.ico',mimetype='image/vnd.microsoft.icon')
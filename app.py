import random
from flask import Flask, render_template, url_for, request
from flask_cors import CORS
from conexionpostgresql import ConexionPostgreSQL
import os
from generador_citas_inspiradoras.citas_inspiradoras import citasInspiradoras

app = Flask(__name__)
CORS(app)

conexion = ConexionPostgreSQL(
    os.getenv("rHOST"),
    "5432",
    "contacto",
    "mjrodriguez",
    os.getenv("rPASSWORD")
)

@app.route('/healthz', methods=['GET'])
def healthz():
    return 'healthy', 200

@app.route('/favicon.ico')
def favicon():
    import os
    from flask import send_from_directory

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'Pajaro.ico',mimetype='image/vnd.microsoft.icon')

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

    return render_template('index.html', success_message='Gracias por contactarnos')

@app.route('/coffee_games', methods=['GET'])
def coffee_games():
    return render_template('coffee_games.html')

@app.route('/api/citas', methods=['GET'])
def obtener_cita_aleatoria():
    cita_aleatoria = random.choice(citasInspiradoras)
    return {
        'cita': cita_aleatoria
    }, 200

@app.route('/generador_citas', methods=['GET'])
def generar_cita():
    return render_template('cita.html')
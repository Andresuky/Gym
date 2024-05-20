from flask import Blueprint, render_template, redirect, url_for, request
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename

# Crear un Blueprint para manejar las rutas relacionadas con los ejercicios
ejercicios_blueprint = Blueprint('ejercicios', __name__)

# Configurar la conexión a la base de datos MongoDB para los ejercicios
client = MongoClient('localhost', 27017)
db = client['gym']
collection = db['ejercicios']

# Ruta para mostrar todos los ejercicios
@ejercicios_blueprint.route('/ejercicios')
def ejercicios():
    ejercicios_data = get_ejercicios_data()  
    return render_template('ejercicios.html', ejercicios_data=ejercicios_data)

def get_ejercicios_data():
    data = list(collection.find())
    return data

# Ruta para mostrar los detalles de un ejercicio específico
@ejercicios_blueprint.route('/ejercicio/<ejercicio_name>')
def ejercicio_detail(ejercicio_name):
    ejercicio = collection.find_one({'name': ejercicio_name})  # Obtener un ejercicio por nombre
    if ejercicio:
        return render_template('ejercicio_detail.html', ejercicio=ejercicio)  # Renderizar la plantilla con los detalles del ejercicio
    else:
        return "Ejercicio no encontrado"

# Ruta para manejar el envío de formulario para agregar un nuevo ejercicio
@ejercicios_blueprint.route('/submit_ejercicio_form', methods=['POST'])
def submit_ejercicio_form():
    if request.method == 'POST':
        # Obtener datos del formulario enviado
        nombre = request.form['name']
        descripcion = request.form['descripcion']
        repeticiones = int(request.form['repeticiones'])
        duracion = int(request.form['duracion'])
        tiempo = int(request.form['tiempo'])
        youtube_url = request.form['youtube_url']
        logo_image = request.files['logo'] if 'logo' in request.files else None

        # Procesar la URL de YouTube
        if youtube_url.startswith("https://www.youtube.com/watch?v="):
            video_id = youtube_url.split('=')[-1]
            youtube_url = f"https://www.youtube.com/embed/{video_id}"

        # Guardar la imagen del logo si se ha proporcionado
        target_directory = 'static/img/gallery/gallery-4/'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        if logo_image:
            logo_filename = secure_filename(logo_image.filename)
            logo_image.save(os.path.join(target_directory, logo_filename))
        else:
            logo_filename = None

        # Crear el documento para insertar en la base de datos MongoDB
        ejercicio_data = {
            "name": nombre,
            "descripcion": descripcion,
            "repeticiones": repeticiones,
            "duracion" : duracion,
            "tiempo" : tiempo,
            "youtube_url": youtube_url,
            "logo_filename": logo_filename
        }

        # Insertar el documento en la colección de ejercicios
        collection.insert_one(ejercicio_data)

        # Redirigir al usuario de vuelta a la página de ejercicios
        return redirect(url_for('ejercicios.ejercicios'))
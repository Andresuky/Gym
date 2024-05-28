from flask import Blueprint, render_template, redirect, url_for, request
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename


ejercicios_blueprint = Blueprint('ejercicios', __name__)


client = MongoClient('localhost', 27017)
db = client['gym']
collection = db['ejercicios']

@ejercicios_blueprint.route('/ejercicios')
def ejercicios():
    ejercicios_data = get_ejercicios_data()  
    return render_template('ejercicios.html', ejercicios_data=ejercicios_data)

def get_ejercicios_data():
    data = list(collection.find())
    return data


@ejercicios_blueprint.route('/ejercicio/<ejercicio_name>')
def ejercicio_detail(ejercicio_name):
    ejercicio = collection.find_one({'name': ejercicio_name})  
    if ejercicio:
        return render_template('EjerciciosTemplate.html', ejercicio=ejercicio)  
    else:
        return "Ejercicio no encontrado"

# Ruta para manejar el envío de formulario para agregar un nuevo ejercicio
@ejercicios_blueprint.route('/submit_ejercicio_form', methods=['POST'])
def submit_ejercicio_form():
    if request.method == 'POST':
        nombre = request.form.get('name')
        descripcion = request.form.get('descripcion')
        repeticiones = int(request.form.get('repeticiones'))
        duracion = int(request.form.get('duracion'))
        tiempo = int(request.form.get('tiempo'))
        youtube_url = request.form.get('youtube_url')
        logo_image = request.files.get('logo')

        if youtube_url.startswith("https://www.youtube.com/watch?v="):
            video_id = youtube_url.split('=')[-1]
            youtube_url = f"https://www.youtube.com/embed/{video_id}"

        target_directory = 'static/assets/img/gallery/gallery-4/'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        if logo_image:
            logo_filename = secure_filename(logo_image.filename)
            logo_image.save(os.path.join(target_directory, logo_filename))
        else:
            logo_filename = None

        ejercicio_data = {
            "name": nombre,
            "descripcion": descripcion,
            "repeticiones": repeticiones,
            "duracion": duracion,
            "tiempo": tiempo,
            "youtube_url": youtube_url,
            "logo_filename": logo_filename
        }

        # Asume que tienes una colección MongoDB definida como `collection`
        collection.insert_one(ejercicio_data)

        return redirect(url_for('ejercicios.ejercicios'))
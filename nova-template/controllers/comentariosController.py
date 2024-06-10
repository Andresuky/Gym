from flask import Blueprint, render_template, redirect, url_for, request
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename

comentarios_blueprint = Blueprint('comentarios', __name__)

# Configuración de la conexión a MongoDB
client = MongoClient('localhost', 27017)
db = client['gym']
comentarios_collection = db.comentarios

@comentarios_blueprint.route('/enviar-comentarios', methods=['POST'])
def enviar_comentarios():
    if request.method == 'POST':
        comentario_texto = request.form.get('comentarios')
        
        comentario_data = {
            "comentarios": comentario_texto
        }

        comentarios_collection.insert_one(comentario_data)  # Corrección aquí

        return redirect(url_for('comentarios.formulario_comentarios'))

@comentarios_blueprint.route('/about')
def formulario_comentarios():
    return render_template('about.html')

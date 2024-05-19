from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from pymongo import MongoClient
import os

# Crear un Blueprint para manejar las rutas relacionadas con los proveedores de soluciones de IA
estudies_blueprint = Blueprint('estudies', __name__)

# Configurar la conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['gpai']
collection = db['estudies']

# Ruta para mostrar todos los proveedores de soluciones de IA
@estudies_blueprint.route('/aiAgro')
def ai_solutions_estudies():
    estudies_data = get_estudies_data()  
    return render_template('aiAgro.html', estudies_data=estudies_data)

def get_estudies_data():
    data = list(collection.find())
    return data

@estudies_blueprint.route('/estudiesTemplate/<estudies_name>')
def get_estudies_onlyone(estudies_name):
    estudies = collection.find_one({'name': estudies_name})  # Obtener un proveedor por nombre
    if estudies:
        return render_template('estudiesTemplate.html', estudies=estudies)  
    else:
        return "Proveedor no encontrado"


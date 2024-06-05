from flask import Blueprint, render_template
from .ejerciciosController import get_ejercicios_data
from .ejerciciosController import ejercicios_blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/ejercicios') 
def ejercicios_blif():
    ejercicios_data = get_ejercicios_data()
    return render_template('ejercicios.html', ejercicios_data=ejercicios_data)

@main_blueprint.route('/addej') 
def addejejej():
    return render_template('addej.html')

@main_blueprint.route('/Gym') 
def gym():
    return render_template('Gym.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')

@main_blueprint.route('/nutricion')
def nutreshon():
    return render_template('nutricion.html')

@main_blueprint.route('/mapa')
def clases():
    return render_template('mapa.html')

@main_blueprint.route('/entrenadores')
def entrenadores():
    return render_template('entrenadores.html')

@main_blueprint.route('/clases')
def mapeishon():
    return render_template('clases.html')
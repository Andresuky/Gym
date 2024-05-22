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

@main_blueprint.route('/contact') 
def ai_data():
    return render_template('contact.html')

@main_blueprint.route('/Gym') 
def ai_gpai():
    return render_template('Gym.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')

@main_blueprint.route('/nutricion')
def nutreshon():
    return render_template('nutricion.html')






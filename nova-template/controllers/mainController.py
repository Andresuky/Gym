from flask import Blueprint, render_template
from .ejerciciosController import get_ejercicios_data
from .estudiesController import get_estudies_data

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/ejercicios') 
def ejercicios_blif():
    ejercicios = get_ejercicios_data()
    return render_template('ejercicios.html', ejercicios=ejercicios)

@main_blueprint.route('/aiAgro') 
def ai_solutions_estudies():
    estudies_data = get_estudies_data()
    return render_template('aiAgro.html', estudies_data=estudies_data)

@main_blueprint.route('/contact') 
def ai_data():
    return render_template('contact.html')

@main_blueprint.route('/Gym') 
def ai_gpai():
    return render_template('Gym.html')

@main_blueprint.route('/aiAgro') 
def ai_agro():
    return render_template('aiAgro.html')





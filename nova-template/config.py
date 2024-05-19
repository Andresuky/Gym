import os

class Config:
    # Clave secreta para proteger las sesiones y los datos en la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-segura'

    # Configuración de la base de datos MongoDB
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/gym'

from flask import Flask
from controllers.mainController import main_blueprint
from controllers.ejerciciosController import ejercicios_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Configuración de la aplicación

app.register_blueprint(main_blueprint)
app.register_blueprint(ejercicios_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

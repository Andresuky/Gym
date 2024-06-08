from flask import Blueprint, render_template, redirect, url_for, request
from pymongo import MongoClient
import os
from werkzeug.utils import secure_filename


comentarios_blueprint = Blueprint('comentarios', __name__)


client = MongoClient('localhost', 27017)
db = client['gym']
collection = db['comentarios']

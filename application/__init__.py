from flask import Flask
import os
from application.model.entity.produto import Produto


template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)


from application.controller import index_controller

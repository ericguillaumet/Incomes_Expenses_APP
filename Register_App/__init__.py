#__init__ para poder importarlo como un módulo

from flask import Flask

app = Flask(__name__) #Para "declarar" Flask

#Para inicializar el servidor de Flask:
#Mac: export FLASK_APP=main.py
#Windows: set FLASK_APP=main.py

#flask --app main --debug run

from Register_App.routes import * 
# Hago referencia a todas las rutas definidas dentor de routes.py
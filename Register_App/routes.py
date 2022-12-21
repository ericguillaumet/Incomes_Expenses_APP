from Register_App import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html") #Llamamos a la función render template para usar el HTML 
#El framework solo va a reconocoer el método render_template si index.html se encuentra dentro de la carpeta templates

@app.route("/new")
def create():
    return render_template("new.html")
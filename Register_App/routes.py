from Register_App import app
from flask import render_template

@app.route("/")
def index():
    #prueba de diccionario a vista HTML
    data = [    
        { 
            'fecha': '18/12/2022',
            'concepto': 'Regalo de Reyes',
            'cantidad': -275.50
        },
        { 
            'fecha': '19/12/2022',
            'concepto': 'Cobro de Trabajo',
            'cantidad': 1200
        },
        { 
            'fecha': '20/12/2022',
            'concepto': 'Ropa de Navidad',
            'cantidad': -50.30
        } 
    ]
    return render_template("index.html", pageTitle="Lists", list=data) #Llamamos a la función render template para usar el HTML 
#El framework solo va a reconocoer el método render_template si index.html se encuentra dentro de la carpeta templates

@app.route("/new")
def create():
    return render_template("new.html", pageTitle="Admission")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Edit")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Delete")
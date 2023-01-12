from Register_App import app
from flask import render_template, request, redirect
from datetime import date
import csv
from config import *
import os #módulo para renombrar y eliminar archivos
from models import delete_by, insert, select_all, select_by, update_by

@app.route("/")
def index():

    data = select_all()

    return render_template("index.html", pageTitle="Lists", list=data) #Llamamos a la función render template para usar el HTML 
#El framework solo va a reconocoer el método render_template si index.html se encuentra dentro de la carpeta templates

@app.route("/new", methods=["GET","POST"])
def create():

    if request.method == "GET": #Esto puede ser POST o GET
        return render_template("new.html", pageTitle="Admission", typeAction="Admission", typeButton="Save", dataForm={}, urlForm="/new") #dataForm vacío porque es un diccionario
    else: #acceder al archivo y configurarlo para cargar un nuevo registro
        myfile = open(MOVEMENTS_FILE, 'a', newline='') #La 'a' es de actualización
        #llamamos al metodo writer de escritura y cargamos el formato para csv
        read = csv.writer(myfile, delimiter=',',quotechar='"')

        #realizamos el control de fecha
        error = validateForm(request.form)
        
        if error:                                                                                               #Mensaje de error
            return render_template("new.html", pageTitle="Admission", typeAction="Admission", typeButton="Save", msgerror = error, dataForm=request.form) 
        else:
            
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']])
            
    return redirect('/') #Para que nos redirija a la pantalla principal

@app.route("/update/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "GET":

        register = select_by(id)

        return render_template("update.html", pageTitle="Edit", typeAction="Modification", typeButton="Edit", dataForm=register, urlForm="/update/" + str(id))
    
    else:

        error = validateForm(request.form)
        
        if error:                                                                                               #Mensaje de error
            return render_template("update.html", pageTitle="Modification", typeAction="Modification", typeButton="Save", msgerror = error, dataForm=request.form) 
        else:
            
            update_by(id, [request.form['date'],
                    request.form['concept'],
                    request.form['quantity']])

    return redirect('/')
    
    #return f"This is the ID ={id} of the modify register"

@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):

        #Si no encuentra registros:
    if request.method == "GET":
        
        searched_register = select_by(id)

        if len(searched_register) > 0:
            return render_template("delete.html", pageTitle="Delete", registers = searched_register)
        else:
            return redirect("/")

    else: #aquí sería POST
        delete_by(id)
        return redirect("/")
    
#Crear una función para validar formulario de registro donde controlemos lo siguiente:
#1.- que la fecha no sea mayor a la actual.
#2.- que el concepto no quede vacio.
#3.- que el campo cantidad sea distinto a cero y de vacio

def validateForm(requestForm):
    today = date.today().isoformat() #isoformat lo transforma en string
    errors =[]
    if requestForm['date'] > today:
        errors.append("Date: the introduced date is not valid")
    if requestForm['concept'] == "":
        errors.append("Empty concept: Introduce a concept for the register")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errors.append("The quantity is empty or equals zero: Introduce a positive or negative quantity")
    return errors
   # if requestForm['concept']:
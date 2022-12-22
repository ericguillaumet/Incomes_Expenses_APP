from Register_App import app
from flask import render_template, request, redirect
from datetime import date
import csv

@app.route("/")
def index():
    file = open("data/movements.csv", "r") #Llama al archivo
    csvReader = csv.reader(file, delimiter=",",quotechar='"') #Accede a cada registro del archivo y lo formatea
    data = [] #Creo una lista de datos vacía para cargar los registros del archivo

    #recorrer el objeto csvReader y cargar cada registro a la lista de datos
    for item in csvReader:
        data.append(item)

    return render_template("index.html", pageTitle="Lists", list=data) #Llamamos a la función render template para usar el HTML 
#El framework solo va a reconocoer el método render_template si index.html se encuentra dentro de la carpeta templates

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "GET": #Esto puede ser POST o GET
        return render_template("new.html", pageTitle="Admission", typeAction="admission", typeButton="Save")
    else: #acceder al archivo y configurarlo para cargar un nuevo registro
        myfile = open('data/movements.csv', 'a', newline='')
        #llamamos al metodo writer de escritura y cargamos el formato para csv
        read = csv.writer(myfile, delimiter=',',quotechar='"')

        #realizamos el control de fecha


        #registramos los datos recibidos desde el formulario con request.form y lo añadimos con el método writerrow
        read.writerow([request.form['date'], request.form['concept'],request.form['quantity']])

        myfile.close()

    return redirect('/') #Para que nos redirija a la pantalla principal

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Edit", typeAction="modification", typeButton="Edit")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Delete")
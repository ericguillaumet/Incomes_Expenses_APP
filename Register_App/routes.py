from Register_App import app
from flask import render_template
import csv

@app.route("/")
def index():
    file = open("data/movements.txt", "r") #Llama al archivo
    csvReader = csv.reader(file, delimiter=",",quotechar='"') #Accede a cada registro del archivo y lo formatea
    data = [] #Creo una lista de datos vacía para cargar los registros del archivo

    #recorrer el objeto csvReader y cargar cada registro a la lista de datos
    for item in csvReader:
        data.append(item)

    return render_template("index.html", pageTitle="Lists", list=data) #Llamamos a la función render template para usar el HTML 
#El framework solo va a reconocoer el método render_template si index.html se encuentra dentro de la carpeta templates

@app.route("/new", methods=["GET","POST"])
def create():
    return render_template("new.html", pageTitle="Admission", typeAction="admission", typeButton="Save")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle="Edit", typeAction="modification", typeButton="Edit")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle="Delete")
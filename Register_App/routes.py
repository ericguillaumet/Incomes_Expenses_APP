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
        return render_template("new.html", pageTitle="Admission", typeAction="Admission", typeButton="Save", dataForm={}) #dataForm vacío porque es un diccionario
    else: #acceder al archivo y configurarlo para cargar un nuevo registro
        myfile = open('data/movements.csv', 'a', newline='') #La 'a' es de actualización
        #llamamos al metodo writer de escritura y cargamos el formato para csv
        read = csv.writer(myfile, delimiter=',',quotechar='"')

        #realizamos el control de fecha
        error = validateForm(request.form)
        
        if error:                                                                                               #Mensaje de error
            return render_template("new.html", pageTitle="Admission", typeAction="Admission", typeButton="Save", msgerror = error, dataForm=request.form) 
        else:
            myfile = open('data/movements.csv', 'a', newline='')
            read = csv.writer(myfile, delimiter=',',quotechar='"')
            #crear ID
            myfile = open('data/last_id.csv', 'r')

            register = myfile.read()

            if register == "":
                new_id = 1
            
            else:
                new_id = int(register) + 1
            myfile.close()

            saving_file = open('data/last_id.csv', 'w', newline='')
            saving_file.write(str(new_id))

            saving_file.close()
            #registramos los datos recibidos desde el formulario con request.form y lo añadimos con el método writerrow
            read.writerow([new_id, request.form['date'], request.form['concept'],request.form['quantity']])

        myfile.close()

    return redirect('/') #Para que nos redirija a la pantalla principal

@app.route("/update/<int:id>")
def edit(id):
    #return render_template("update.html", pageTitle="Edit", typeAction="Modification", typeButton="Edit", dataForm={})
    return f"This is the ID ={id} of the modify register"
@app.route("/delete/<int:id>")
def remove(id):
    return f"This is the ID ={id} of the delete register"
    #return render_template("delete.html", pageTitle="Delete")

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
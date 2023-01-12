from config import *
import csv
import os
from flask import request

def select_all():
    """
    Devolverá una lista con todos los registros del fichero MOVEMENTS_FILE
    """
    file = open(MOVEMENTS_FILE, "r") #Llama al archivo
    csvReader = csv.reader(file, delimiter=",",quotechar='"') #Accede a cada registro del archivo y lo formatea
    data = [] #Creo una lista de datos vacía para cargar los registros del archivo

    #recorrer el objeto csvReader y cargar cada registro a la lista de datos
    for item in csvReader:
        data.append(item)
    
    file.close()

    return data

def select_by(id):
    """
    Devolverá un registro con el ID de la entrada o vacío si no encuentra MOVEMENTS_FILE
    """
    myfile = open(MOVEMENTS_FILE, 'r')
    read = csv.reader(myfile, delimiter=',',quotechar='"')
    searched_register = []
    for register in read:
        if register[0] == str(id):
            searched_register = register
    
    dictionary = dict()
    dictionary["id"] = searched_register[0] #Posición 0 es el id
    dictionary["date"] = searched_register[1]
    dictionary["concept"] = searched_register[2]
    dictionary["quantity"] = searched_register[3]

    myfile.close()

    return dictionary
    
def delete_by(id):
    """
    Borrará el registro cuyo ID coincide con el de la entrada en el fichero MOVEMENTS_FILE
    """
    old_file = open(MOVEMENTS_FILE, 'r') #acceder al csv de registros
    file = open(MOVEMENTS_NEW_FILE, 'w', newline= "") #acceder a un archivo auxiliar

    csvReader = csv.reader(old_file, delimiter=',', quotechar='"')
    csvWriter = csv.writer(file, delimiter=',', quotechar='"')

    for register in csvReader:
        if register[0] != str(id): #mientras el id sea distinto del proporcionado, para eliminar escribimos encima de "file"
            csvWriter.writerow(register)

    old_file.close()
    file.close()

    os.remove(MOVEMENTS_FILE) #función remove que recibe la ruta del archivo a eliminar
    os.rename(MOVEMENTS_NEW_FILE, MOVEMENTS_FILE) #función para renombrar que recibe los parámetros de archivo a renombrar y nombre nuevo

def insert(register_form):


    """
    Crear un nuevo registro, siempre y cuando sea comptabile con el fichero,
    aignará al registro un ID único (acumulativo)
    """
    myfile = open(MOVEMENTS_FILE, 'a', newline='')
    read = csv.writer(myfile, delimiter=',', quotechar='"')
    #crear ID
    myfile = open(LAST_ID_FILE, 'r')

    register = myfile.read()

    if register == "":
        new_id = 1
    
    else:
        new_id = int(register) + 1
    myfile.close()

    saving_file = open(LAST_ID_FILE, 'w', newline='')
    saving_file.write(str(new_id))
    saving_file.close()

    #registramos los datos recibidos desde el formulario con request.form y lo añadimos con el método writerrow
    read.writerow([str(new_id)] + register_form)

    myfile.close()

def update_by(id, modified_register):
    old_file = open(MOVEMENTS_FILE, 'r') #acceder al csv de registros
    file = open(MOVEMENTS_NEW_FILE, 'w', newline= "") #acceder a un archivo auxiliar

    csvReader = csv.reader(old_file, delimiter=',', quotechar='"')
    csvWriter = csv.writer(file, delimiter=',', quotechar='"')

    for register in csvReader:
        if register[0] != str(id): #mientras el id sea distinto del proporcionado, para eliminar escribimos encima de "file"
            csvWriter.writerow(register)
        else: #encontramos el registro con el id dado
            csvWriter.writerow([str(id)] + modified_register)

    old_file.close()
    file.close()

    os.remove(MOVEMENTS_FILE) #función remove que recibe la ruta del archivo a eliminar
    os.rename(MOVEMENTS_NEW_FILE, MOVEMENTS_FILE) #función para renombrar que recibe los parámetros de archivo a renombrar y nombre nuevo

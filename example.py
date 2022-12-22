import csv
#Lectura de archivos
"""
with open('data/movements.csv', 'r') as result:
    read = result.read()
    print(read)
"""

#Otra manera:
"""
result = open('data/movements.csv', 'r')
read = result.read() #o readlines() para leer por línea
print(read)
"""
data = []
myfile = open("data/movements.csv", "r")
myfile = csv.reader(myfile, delimiter=",",quotechar='"')

for registers in myfile:
    print(registers)
    data.append(registers)

print("This is the data: ", data)

myfile.close()
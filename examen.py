import random
import csv
larva = 0
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
with open('registros_trabajadores.csv', 'r+') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Trabajador","Sueldo"])
def ranni():
    for elemento in trabajadores:
        ede = random.randint(300000,2500000)
        escritor_csv.writerow(f"{elemento},{ede}")
def rahdan():
    with open('registros_trabajadores.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        estadistica_sueldo1 = {
            "tr":[],
            "su":[]
        }
        estadistica_sueldo2 = {
            "tr":[],
            "su":[]
        }
        estadistica_sueldo3 = {
            "tr":[],
            "su":[]
        }
        for fila in lector_csv:
            trabajador = fila['Trabajador']
            sueldo = int(fila['Sueldo'])
            if sueldo >= 800000:
                estadistica_sueldo1["su"].append(sueldo)
                estadistica_sueldo1["tr"].append(trabajador)
            if sueldo <= 800000 and sueldo >= 2000000:
                estadistica_sueldo2["su"].append(sueldo)
                estadistica_sueldo2["tr"].append(trabajador)
            else:
                estadistica_sueldo3["su"].append(sueldo)
                estadistica_sueldo3["tr"].append(trabajador)
        print ("Trabajadores con sueldo menor que 800.000")
        tilin = 0
        for elemento in estadistica_sueldo1:
            print (f"Trabajador: {estadistica_sueldo1['tr'][tilin]} ,Sueldo: {estadistica_sueldo1['su'][tilin]}")
            tilin += tilin + 1
        print ("Trabajadores con sueldo mayor que 800.000 y menor que 2.000.000")
        tilin = 0
        for elemento in estadistica_sueldo2:
            print (f"Trabajador: {estadistica_sueldo2['tr'][tilin]} ,Sueldo: {estadistica_sueldo2['su'][tilin]}")
            tilin += tilin + 1
        print ("Trabajadores con sueldo mayor que 2.000.000")
        tilin = 0
        for elemento in estadistica_sueldo3:
            print (f"Trabajador: {estadistica_sueldo3['tr'][tilin]} ,Sueldo: {estadistica_sueldo3['su'][tilin]}")
            tilin += tilin + 1
def rennala():
    with open('registros_trabajadores.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
print ("----------------------------")
print ("Menu de opciones.")
print (" .1|Asignar sueldos aleatorios|")
print (" .2|Clasificar sueldos|")
print (" .3|Ver estadísticas.|")
print (" .4|Reporte de sueldos|")
print (" .5|Salir del Programa|")
print ("----------------------------")
dedos = input("¿Que opcion desea realizar?(1,2,3,4,5): ")
if dedos == 1:
    ranni()
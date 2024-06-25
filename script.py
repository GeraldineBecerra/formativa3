import os
import csv

def inicio():
    inicio = True
    menu = ("1.Registrar trabajador","2.Listar todos los trabajadores","3.Imprimir planill de sueldos","4.Salir")
    for i in menu:
        print(i)
    opcion = int(input("Ingrese una opciòn"))

    while inicio:
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            planilla()
        elif opcion == 4:
            inicio = False

def registrar():
    columnas = ["Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Desc.AFP","Liquido a pagar"]
    with open("trabajadores.csv","w",newline='') as trabajador:
        nuevoTrabajador = csv.writer(trabajador)
        nuevoTrabajador.writerows(["Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Desc.AFP","Liquido a pagar"])

    cantTrabajadores = input("cuantos trabajadores desea agregar?")
    for i in cantTrabajadores:
        nombre = input("Nombre y apellido")
        cargo = input("Cargo")
        sueldoBruto= int(input("Sueldo bruto"))

        salud = sueldoBruto * 0.07
        afp = sueldoBruto * 0.12
        sueldoLiquido = sueldoBruto - salud - afp
        nuevoTrabajador.writerow(nombre,cargo,sueldoBruto,salud,sueldoLiquido)



        
def listar():
    with open("trabajadores.csv","r",newline='') as trabajador:
        nuevoTrabajador = trabajador
        prueba = nuevoTrabajador.read()
        for i in prueba:
            print(i)
 

def planilla():
    planilla = True
    menu = ("1.CEO","2.Desarrollador","3.Analista de datos","4.Salir")
    for i in menu:
        print(i)
    opcion = int(input("Ingrese la opcion de la planilla que desea ver"))
    
        
    
inicio()


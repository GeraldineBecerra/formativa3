import os
import csv

def inicio():
    inicio = True
    while inicio:
        menu = ("1.Registrar trabajador","2.Listar todos los trabajadores","3.Imprimir planill de sueldos","4.Salir")
        for i in menu:
            print(i)
        opcion = int(input("Ingrese una opciòn"))
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            planilla()
        elif opcion == 4:
            inicio = False

def registrar():
    archivo = "trabajadores.csv"
    archivoExiste = os.path.isfile(archivo)
    if not archivoExiste:
        with open("trabajadores.csv","w",newline='') as trabajador:
            nuevoTrabajador = csv.writer(trabajador)
            nuevoTrabajador.writerow(["Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Desc.AFP","Liquido a pagar"])

    cantTrabajadores = int(input("cuantos trabajadores desea agregar?"))
    for _ in range(cantTrabajadores):
        nombre = input("Nombre y apellido")
        cargo = input("Cargo")
        sueldoBruto= int(input("Sueldo bruto"))
        salud = sueldoBruto * 0.07
        afp = sueldoBruto * 0.12
        sueldoLiquido = sueldoBruto - salud - afp

        with open("trabajadores.csv","a",newline='') as trabajador:
            nuevoTrabajador = csv.writer(trabajador)
            nuevoTrabajador.writerow([nombre,cargo,sueldoBruto,salud,afp,sueldoLiquido])
        print("Trabajador agregado con exito")

def listar():
    with open("trabajadores.csv","r",newline='') as trabajador:
        nuevoTrabajador = csv.reader(trabajador)
        for i in nuevoTrabajador:
            print(i)
          
def planilla():
    menu = ("ceo","Desarrollador","Analista de datos")
    for i in menu:
        print(i)
    with open("trabajadores.csv","r",newline='') as trabajador:
        opcion = input("Ingrese la opcion de la planilla que desea ver")

        nuevoTrabajador = csv.reader(trabajador)
        for i in nuevoTrabajador:
            if i[1] == opcion:
                print(i)
    
    
inicio()


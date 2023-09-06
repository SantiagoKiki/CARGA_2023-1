"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

""" 
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def new_controllers(data_types):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(data_types)
    return control
    
def set_catalog_data_type(control,datatype_to_use):
    if control['model']['datos']['size'] == 0:
        return datatype_to_use

def print_menu()->None:
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10 seleccionar el tipo de representación de la lista (ARRAY_LIST o LINKED_LIST)")
    print("0- Salir")

def load_databy(control, filename:str,sort_met):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    datos = controller.load_databy(control,filename,sort_met)
    return datos

def print_load_data(load_data):
    tabla =  tabulate(controller.first_last_elements(load_data["datos"]) , headers= "keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9)
    return print(tabla)
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    data = controller.req_1(control)
    time = data[1]
    data = data[0]
    print(data)
    to_print = {}
    by_anio = data.items()
    for values in by_anio:
        for key_value in values[1].items():
            if key_value[0] not in to_print:
                to_print[key_value[0]] = []
            to_print[key_value[0]].append(key_value[1])  
    return print(tabulate(to_print,headers="keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9),"El tiempo de ejecución del requerimiento 1 es de " + str(round(time,3))+" ms")  

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    data = controller.req_3(control)
    time = data[1]
    first_table = controller.first_table_req3(data[0])
    table1 = tabulate(first_table,headers="keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9)
    second_table =controller.second_table_req3(controller.req_3(control)[0])
    table2 = tabulate(second_table,headers="keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9)
    print(table1)
    print(table2)
    print("El tiempo de ejecución del requerimiento 3 es de " + str(round(time,3))+" ms")  


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    data = controller.req_4(control)
    first_table = controller.first_table_req4(data)
    table1 = tabulate(first_table,headers="keys",tablefmt="grid",maxcolwidths= 11,maxheadercolwidths=8)
    #second_table =controller.second_table_req4(controller.req_4(control))
    #table2 = tabulate(second_table,headers="keys",tablefmt="grid",maxcolwidths= 5,maxheadercolwidths=3)
    print(table1)
    print("\n \n")
    #print(table2)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """



def print_req_6(control,anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    data = controller.req_6(control,anio)
    table1 = tabulate(data[0],headers="keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9)
    print(table1)
    tables2 = []
    tables3 = []
    tables4 = []
    for less_most in data[1]:
        table = {'Código subsector económico':[],
               "Nombre subsector económico":[],
               "Total ingresos netos del subsector económico":[],
               "Total costos y gastos del subsector económico":[],
               "Total saldo a pagar del subsector económico":[],
               "Total saldo a favor del subsector económico": []
                }
        for values in controller.calliterator(less_most):
            for key_value in values.items():
                if key_value[0] == "Actividad económica que más aporto" or key_value[0] == "Actividad económica que menos aporto":
                    for l_v in key_value[1].items():
                        if l_v[0] == "data":
                            for title_value in l_v[1].items():
                                to_add = []
                                to_add.append(title_value[0])
                                to_add.append(title_value[1])
                                if key_value[0] == "Actividad económica que más aporto":
                                    tables3.append(to_add)
                                if key_value[0] == "Actividad económica que menos aporto":
                                    tables4.append(to_add)
                if key_value[0] in table and key_value[0] != "Actividad económica que más aporto" and key_value[0] != "Actividad económica que menos aporto":
                    table[key_value[0]].append(key_value[1])
        tables2.append(table)
    print("\n \n \n \n \n")
    for tabl in tables2:
        print(tabulate(tabl,headers="keys",tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9))

    print("Actividades económicas que más aportaron en cada subsector")
    print(tabulate(tables3,tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9))
    print("\n \n \n \n \n")
    print("Actividades económicas que menos aportaron en cada subsector")
    print(tabulate(tables4,tablefmt="grid",maxcolwidths= 12,maxheadercolwidths=9))





def print_req_7(control, anio_inicial, anio_final, top_n):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    datos_finales = controller.req_7(control, anio_inicial, anio_final, top_n)
    print (datos_finales)
    #print(tabla)
    #return (tablamostrada)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

# Se crea el controlador asociado a la vista

data_type = "ARRAY_LIST"
control = new_controllers(data_type)
# main del reto

if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_databy(control,'DIAN/Salida_agregados_renta_juridicos_AG-large.csv',"Merge Sort")
                print("se cargaron " + str(controller.data_size(data[1]["datos"])) + " columnas.")
                print_load_data(data[1])
                print("\nEl tiempo que ha tardado en cargar los datos es " + str(round(data[0],3))+ " ms\n")
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                anio_esp = input("\n Ingrese el año que desea consultar: ")
                print_req_6(control,anio_esp)
            elif int(inputs) == 8:
                anios_inicial = int(input("\n Ingrese el valor de año inicial a consultar: ")) 
                anios_final = int(input("\n Ingrese el valor de año final a consultar: ")) 
                top_n = int(input("\n Ingrese el top a consultar: ")) 
                print_req_7(control, anios_inicial, anios_final, top_n)

            elif int(inputs) == 10:        
                data_type = input("ingrese el tipo de dato que quiere usar. \n Ingrese 1 para ARRAY_LIST \n Ingrese 2 para LINKED_LIST \n")
                if int(data_type) == 1:
                    data_type = "ARRAY_LIST"
                elif int(data_type) == 2:
                    data_type = "SINGLE_LINKED"
                else:
                    print("Ingrese una opción válida.")
                small_control = new_controllers(data_type)
                print("\n ha cargado la estuctura de datos de tipo " + small_control["model"]["datos"]["type"] +" correctamente. \n" )
                muestra = input("Ingrese 1 para ingresar un tamaño de muestra para el catálogo \nIngrese 2 para ingresar el sufijo del archivo que desea cargar ((ej.: -20pct.csv, -50pct.csv, -large.csv) en el catálogo \n")
                tamanio = 0
                file_size_sufijo = None
                sort_metd = None
                file_name = "DIAN/Salida_agregados_renta_juridicos_AG"
                if int(muestra) ==1:
                    tamanio = int(input("ingrese el tamaño de la meustra que desea cargar: "))
                    if tamanio < controller.data_size(data["datos"]):
                        print("\nHa cargado una muestra de "+ str(tamanio) +" datos correctamente \n")
                    else:
                        print("Ingrese una muestra válida")
                if int(muestra) == 2:
                    file_size_sufijo = input("\ningrese el sufijo del archivo que sea cargar para la muestra (ej.: -20pct.csv, -50pct.csv, -large.csv): ")
                    file_name = file_name + file_size_sufijo 
                    print("\nha cargado el archivo "+ file_name + " correctamente\n")
                    
                else:
                    print("ingrese una opción válida")

                orden = input("Seleccione el tipo de rodenamiento que quiere utilizar; \n 1 -> Selection Sort \n 2 -> Insertion sort \n 3-> Shell sort \n 4-> Quick Sort \n 5-> Merge Sort\n")
                if int(orden) == 1:
                    sort_metd = "Selection Sort"
                elif int(orden) == 2:
                    sort_metd = "Insertion sort"
                elif int(orden)==3: 
                    sort_metd = "Shell sort"
                elif int(orden)==4:
                    sort_metd = "Quick Sort"
                elif int(orden)==5:
                    sort_metd = "Merge Sort"
                else:
                    print("Ingrese una opción de Sort válida")
                data1 = load_databy(small_control, file_name,sort_metd)
                print("Tiempo de ejecución para el archivo " + file_name  + " usando " + sort_metd + " : " + str(round(data1[0],3))+ " ms")
                    
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)

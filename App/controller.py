"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(datatypes)->dict:
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs(datatypes)
    return control


# Funciones para la carga de datos

def load_databy(control,filename,sort_met):
    start_time = get_time()
    data_model = control["model"]
    datos_a_anadir = load_file_data(data_model, filename)
    model.sortby(data_model, sort_met)
    end_time = get_time()
    delta_time = deltaTime(start_time, end_time)
    return delta_time, datos_a_anadir

def load_file_data(data_structure,filename):
    data_file = cf.data_dir + filename
    input_file = csv.DictReader(open(data_file, encoding='utf-8'))
    for person in input_file:
        model.add_data(data_structure,person)
    return data_structure

def data_size(data_structure):
    """
    retorna el tamaño de la estructura de datos
    """
    size = model.data_size(data_structure)
    return size

def first_last_elements(data_structure):

    return (model.obtainsublist(model.filterbyanio(data_structure)))

# Funciones de ordenamiento

def sort(data_model):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    sorted_model = model.sort(data_model)
    return sorted_model


# Funciones de consulta sobre el catálogo

def calliterator(datastructure):
    return model.iterator(datastructure)

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
    anios = {'2012': {}, '2013': {}, '2014': {}, '2015': {}, '2016': {}, '2017': {}, '2018': {}, '2019': {}, '2020': {}, '2021': {}}
    estructura = control["model"]["datos"]
    anios =  model.req_1(estructura,anios)
    end_time = get_time()
    delta_time = deltaTime(start_time, end_time)
    return(anios,delta_time)


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    filtrados = model.filterbyanio(control["model"]["datos"])
    end_time = get_time()
    delta_time = deltaTime(start_time, end_time)
    return (model.req_3(filtrados),delta_time)

def first_table_req3(datos):
    tabla1 = {"Año":[],"Código sector económico":[],"Nombre sector económico":[],"Código subsector económico":[],"Nombre subsector económico":[],"Total de retenciones del subsector económico":[],"Total ingresos netos del subsector económico":[],"Total costos y gastos del subsector económico":[],"Total saldo a pagar del subsector económico":[],"Total saldo a favor del subsector económico":[]}
    notheaders = ["maxi","mini"]
    for anio in calliterator(datos):
        for key_value in anio.items():
            if  not key_value[0] in notheaders:
                tabla1[key_value[0]].append(key_value[1])
    return tabla1

def second_table_req3(datos):
    tabla2 = {"Código actividad económica":[],"Nombre actividad económica":[],"Total retenciones":[],"Total ingresos netos":[],"Total costos y gastos":[],"Total saldo a pagar":[],"Total saldo a favor":[],"Año":[]}
    notheaders = ["Año","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total de retenciones del subsector económico","Total ingresos netos del subsector económico","Total costos y gastos del subsector económico","Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
    for anio in calliterator(datos):
        for elemento in anio.items():
            if  not elemento[0] in notheaders:
                for key_value in elemento[1].items():
                    if key_value[0] == "elements":
                        for dicc in key_value[1]:
                            for llave_valor in dicc.items():
                                #print(llave_valor,anio["Año"])
                                tabla2[llave_valor[0]].append(llave_valor[1])
    return tabla2


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    filtrados = model.filterbyanio(control["model"]["datos"])
    return model.req_4(filtrados)
    # TODO: Modificar el requerimiento 
def first_table_req4(datos):
    tabla1 = {"Año":[],"Código sector económico":[],"Nombre sector económico":[],"Código subsector económico":[],"Nombre subsector económico":[],"Costos y gastos nómina":[],"Total ingresos netos del subsector económico":[],"Total costos y gastos del subsector económico":[],"Total saldo a pagar del subsector económico":[],"Total saldo a favor del subsector económico":[]}
    notheaders = ["maxi","mini"]
    for anio in calliterator(datos):
        for key_value in anio.items():
            if  not key_value[0] in notheaders:
                tabla1[key_value[0]].append(key_value[1])
    return tabla1

def second_table_req4(datos):
    tabla2 = {"Código actividad económica":[],"Nombre actividad económica":[],"Costos y gastos nómina":[],"Total ingresos netos":[],"Total costos y gastos":[],"Total saldo a pagar":[],"Total saldo a favor":[],"Año":[]}
    notheaders = ["Código sector económico","Nombre sector económico","Costos y gastos nómina","Total ingresos netos del subsector económico","Total costos y gastos del subsector económico","Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
    for anio in calliterator(datos):
        for elemento in anio.items():
            if  not elemento[0] in notheaders:
                for key_value in elemento[1]:
                    if key_value[0] == "elements":
                        for dicc in key_value[1]:
                            for llave_valor in dicc.items():
                                #print(llave_valor,anio["Año"])
                                tabla2[llave_valor[0]].append(llave_valor[1])
    return tabla2

def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    filtradosbyanio = model.filterbyanio(control["model"]["datos"])
    filterbyact = model.filterbysece(filtradosbyanio[anio])
    return model.req_6(filterbyact)

def req_7(control, anio_inicial, anio_final, top_n):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass
    filtrados = model.filterbyanio(control["model"]["datos"])
    return model.req_7(filtrados, anio_inicial, anio_final, top_n)

def first_table_req7(datos):
    tabla1 = {"Año":[],"Código actividad económica":[],
              "Nombre actividad económica":[],
              "Código sector económico":[],
              "Nombre sector económico":[],
              "Código subsector económico":[],
              "Nombre subsector económico":[],
              "Total ingresos netos consolidados para el periodo":[],
              "Total costos y gastos para el periodo":[],
              "Total saldo a pagar consolidados para el periodo":[],
              "Total saldo a favor consolidados para el periodo":[]
              }
    for anio in calliterator(datos):
        #print(anio)
        for key_value in anio.items():
            for value in key_value:
                if value == "elements":
                    tabla1[0].append[value[1]]
                    print(tabla1)


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

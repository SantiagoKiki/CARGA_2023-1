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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs(new_datatype)->list:
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data ={
        'datos':None
    }
    data['datos'] = lt.newList(new_datatype)
    return data


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs['datos'],data)
    return data_structs


# Funciones para creacion de datos

def filterbyanio(datastructure):
    retorno = {}
    for dicci in iterator(datastructure):
        if dicci["Año"] not in retorno:
            retorno[dicci["Año"]] = lt.newList("ARRAY_LIST")
        lt.addLast(retorno[dicci["Año"]],dicci)
    return retorno

def filterbysece(list_anio):
    retorno = {}
    for act in iterator(list_anio):
        if act["Código sector económico"] not in retorno:
            retorno[act["Código sector económico"]] = lt.newList("ARRAY_LIST")
        lt.addLast(retorno[act["Código sector económico"]],act)
    return retorno       

# Funciones de consulta

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs)

def obtainsublist(by_anios):
    retorno = []
    for anio in by_anios.values():
        inicio = lt.subList(anio,1,3)
        final = lt.subList(anio,lt.size(anio)-2,3)
        to_add = []
        to_add.append(inicio)
        to_add.append(final)
        retorno.extend(to_add)
    return filtrar_sublistas(retorno)

def filtrar_sublistas(sublistas):
    retorno = {"Año":[],"Código actividad económica":[],"Nombre actividad económica":[],"Código sector económico":[],"Nombre sector económico":[],"Código subsector económico":[],"Total ingresos netos":[],"Total costos y gastos":[],"Total saldo a pagar":[],"Total saldo a favor":[]}
    headers = retorno.keys()
    for sublista in sublistas:
        for elemento in iterator(sublista):
            for key_value in elemento.items():
                if key_value[0] in headers:
                    retorno[key_value[0]].append(key_value[1]) 
                    
    return retorno  






def req_1(data_structs,anios):
    """
    Función que soluciona el requerimiento 1
    """
    for dicci in iterator(data_structs):
        sub_dicci = {
                "Año":dicci["Año"],
                "Código actividad económica":dicci["Código actividad económica"],
                "Nombre actividad económica":dicci["Nombre actividad económica"],
                "Código sector económico":dicci["Código sector económico"],
                "Nombre sector económico":dicci["Nombre sector económico"],
                "Código subsector económico":dicci["Código subsector económico"],
                "Total ingresos netos":dicci["Total ingresos netos"],
                "Total costos y gastos":dicci["Total costos y gastos"],
                "Total saldo a pagar":dicci["Total saldo a pagar"],
                "Total saldo a favor":dicci["Total saldo a favor"]   
               }
        if anios[dicci["Año"]] == {}:
            anios[dicci["Año"]] = sub_dicci
        elif float(dicci["Total saldo a pagar"]) > float(anios[dicci["Año"]]['Total saldo a pagar']):
               anios[dicci["Año"]] = sub_dicci
    return anios

        

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_filtarados):
    """
    Función que soluciona el requerimiento 3
    """
    retorno_f = lt.newList("ARRAY_LIST")
    for anio in data_filtarados.values():
        subsectores_by_anio = {}
        for registro in iterator(anio):
            to_add = {"Año":None,
                  "Código sector económico":None,
                  "Nombre sector económico":None,
                  "Código subsector económico":None,
                  "Nombre subsector económico": None,
                  "Total de retenciones del subsector económico":0,
                  "Total ingresos netos del subsector económico":0,
                  "Total costos y gastos del subsector económico":0,
                  "Total saldo a pagar del subsector económico":0,
                  "Total saldo a favor del subsector económico":0,
                  "maxi" : lt.newList("ARRAY_LIST"),
                  "mini" : lt.newList("ARRAY_LIST")     
                     }
            
            if registro["Código subsector económico"] not in subsectores_by_anio:
                subsectores_by_anio[registro["Código subsector económico"]] = to_add
                subsectores_by_anio[registro["Código subsector económico"]]["Año"] = registro["Año"]


            subsectores_by_anio[registro["Código subsector económico"]]["Año"] = registro["Año"]
            subsectores_by_anio[registro["Código subsector económico"]]["Código sector económico"] = registro["Código sector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Nombre sector económico"] = registro["Nombre sector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Código subsector económico"] = registro["Código subsector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Nombre subsector económico"] = registro["Nombre subsector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Total de retenciones del subsector económico"] += float(registro["Total retenciones"])
            subsectores_by_anio[registro["Código subsector económico"]]["Total ingresos netos del subsector económico"] += float(registro["Total ingresos netos"])
            subsectores_by_anio[registro["Código subsector económico"]]["Total costos y gastos del subsector económico"] += float(registro["Total costos y gastos"])
            subsectores_by_anio[registro["Código subsector económico"]]["Total saldo a pagar del subsector económico"] += float(registro["Total saldo a pagar"])
            subsectores_by_anio[registro["Código subsector económico"]]["Total saldo a favor del subsector económico"] += float(registro["Total saldo a favor"])

            sub_dict = {
                        "Código actividad económica" : registro["Código actividad económica"],
                        "Nombre actividad económica":registro["Nombre actividad económica"],
                        "Total retenciones": registro["Total retenciones"],
                        "Total ingresos netos":registro["Total ingresos netos"],
                        "Total costos y gastos": registro["Total costos y gastos"],
                        "Total saldo a pagar" : registro["Total saldo a pagar"],
                        "Total saldo a favor" : registro["Total saldo a favor"],
                        "Año":registro["Año"]
                        }        
            

            if lt.size(subsectores_by_anio[registro["Código subsector económico"]]["maxi"]) < 3:
                lt.addLast(subsectores_by_anio[registro["Código subsector económico"]]["maxi"], sub_dict) 
                
            if lt.size(subsectores_by_anio[registro["Código subsector económico"]]["mini"]) < 3:
                lt.addLast(subsectores_by_anio[registro["Código subsector económico"]]["mini"], sub_dict)

            sortsublist_max(sub_dict,subsectores_by_anio[registro["Código subsector económico"]]["maxi"])
            sortsublist_mini(sub_dict,subsectores_by_anio[registro["Código subsector económico"]]["mini"])

        lt.addLast(retorno_f,subsectores_by_anio)    
    return sortsubsectors(retorno_f)
                
            


def req_4(data_filtrados):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    retorno_f = lt.newList("ARRAY_LIST")
    
    for anio in data_filtrados.values():
        subsectores_by_anio = {}
        for registro in iterator(anio):
            to_add = {"Año":None,
                  "Código sector económico":None,
                  "Nombre sector económico":None,
                  "Código subsector económico":None,
                  "Nombre subsector económico": None,
                  "Costos y gastos nómina": 0,
                  "Total ingresos netos del subsector económico": 0,
                  "Total costos y gastos del subsector económico": 0,
                  "Total saldo a pagar del subsector económico": 0,
                  "Total saldo a favor del subsector económico": 0,
                   "maxi" : lt.newList("ARRAY_LIST"),
                  "mini" : lt.newList("ARRAY_LIST")
                     }
        
            if registro["Código subsector económico"] not in subsectores_by_anio:
                subsectores_by_anio[registro["Código subsector económico"]] = to_add
                subsectores_by_anio[registro["Código subsector económico"]]["Año"] = registro["Año"]

            subsectores_by_anio[registro["Código subsector económico"]]["Año"] = registro["Año"]
            subsectores_by_anio[registro["Código subsector económico"]]["Código sector económico"] = registro["Código sector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Nombre sector económico"] = registro["Nombre sector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Código subsector económico"] =  registro["Código sector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Nombre subsector económico"] = registro["Nombre subsector económico"]
            subsectores_by_anio[registro["Código subsector económico"]]["Costos y gastos nómina"] += float(registro["Costos y gastos nómina"])
            subsectores_by_anio[registro["Código subsector económico"]]["Total ingresos netos del subsector económico"] += float(registro["Total ingresos netos"])           
            subsectores_by_anio[registro["Código subsector económico"]]["Total costos y gastos del subsector económico"] += float(registro["Total costos y gastos"])             
            subsectores_by_anio[registro["Código subsector económico"]]["Total saldo a pagar del subsector económico"] += float(registro["Total saldo a pagar"])             
            subsectores_by_anio[registro["Código subsector económico"]]["Total saldo a favor del subsector económico"] += float(registro["Total saldo a favor"])
            
            sub_dict = {"Código actividad económica": registro["Código actividad económica"],
                    "Nombre actividad económica":registro["Nombre actividad económica"],
                    "Costos y gastos nómina":registro["Costos y gastos nómina"],
                    "Total ingresos netos":registro["Total ingresos netos"],
                    "Total costos y gastos": registro["Total costos y gastos"],
                    "Total saldo a pagar" : registro["Total saldo a pagar"],
                    "Total saldo a favor" : registro["Total saldo a favor"]
                    }        
            
            if lt.size(subsectores_by_anio[registro["Código subsector económico"]]["maxi"]) < 3:
                lt.addLast(subsectores_by_anio[registro["Código subsector económico"]]["maxi"], sub_dict) 
            if lt.size(subsectores_by_anio[registro["Código subsector económico"]]["mini"]) < 3:
                 lt.addLast(subsectores_by_anio[registro["Código subsector económico"]]["mini"], sub_dict)
            
            sortsublist_max1(sub_dict,subsectores_by_anio[registro["Código subsector económico"]]["maxi"])
            sortsublist_mini1(sub_dict,subsectores_by_anio[registro["Código subsector económico"]]["mini"])

        lt.addLast(retorno_f,subsectores_by_anio)    
    return sortsubsectors1(retorno_f)

def iterator(datastructure):
    return lt.iterator(datastructure)

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(sec_list):
    """
    Función que soluciona el requerimiento 6
    """
    retorno_f = lt.newList("ARRAY_LIST")
    retorno_2 = lt.newList("ARRAY_LIST")
    for secs in sec_list.values():
        secs_byact = {}
        for sec in iterator(secs):
            to_add = {
                  "Código sector económico":None,
                  "Nombre sector económico":None,
                  "Total ingresos netos del sector económico":0,
                  "Total costos y gastos del sector económico":0,
                  "Total saldo a pagar del sector económico":0, 
                  "Total saldo a favor del sector económico":0,
                  "subsectores":{}
                     }
            if sec["Código sector económico"] not in secs_byact:
                secs_byact[sec["Código sector económico"]] = to_add
                secs_byact[sec["Código sector económico"]]["Código sector económico"] = sec["Código sector económico"]

            secs_byact[sec["Código sector económico"]]["Código sector económico"] = sec["Código sector económico"]
            secs_byact[sec["Código sector económico"]]["Nombre sector económico"] = sec["Nombre sector económico"]
            secs_byact[sec["Código sector económico"]]["Total ingresos netos del sector económico"] += float(sec["Total ingresos netos"])
            secs_byact[sec["Código sector económico"]]["Total costos y gastos del sector económico"] += float(sec["Total costos y gastos"])
            secs_byact[sec["Código sector económico"]]["Total saldo a pagar del sector económico"] += float(sec["Total saldo a pagar"])
            secs_byact[sec["Código sector económico"]]["Total saldo a favor del sector económico"] += float(sec["Total saldo a favor"])

            if sec["Código subsector económico"] not in  secs_byact[sec["Código sector económico"]]["subsectores"]:
                secs_byact[sec["Código sector económico"]]["subsectores"][sec["Código subsector económico"]] = lt.newList("ARRAY_LIST")

            lt.addLast(secs_byact[sec["Código sector económico"]]["subsectores"][sec["Código subsector económico"]],sec)
        lt.addLast(retorno_f,secs_byact)    
    for sector in iterator(retorno_f):
        for subsectores in sector.values():
            sumados = sumsubsectors_req6(subsectores["subsectores"])
            lt.addLast(retorno_2,sumados)
     
    retorno_f = filter_table1_req6(retorno_f)
    retorno_2 = filter_table2_req6(retorno_2)
    return retorno_f,retorno_2
            
            
def sumsubsectors_req6(list_subsecs):
    
    for subsector in list_subsecs.values():
        retorno = {}
        for elemento in iterator(subsector):
            suma = {
                "Código subsector económico":None,
                "Nombre subsector económico":None,
                "Total ingresos netos del subsector económico": 0,
                "Total costos y gastos del subsector económico": 0,
                "Total saldo a pagar del subsector económico": 0,
                "Total saldo a favor del subsector económico": 0,
                "Actividad económica que más aporto" : {"Total ingresos netos" : 0,"data":None},
                "Actividad económica que menos aporto" : {"Total ingresos netos" : 1000000000000000,"data":None},
                }
            if elemento["Código subsector económico"] not in retorno:
                retorno[elemento["Código subsector económico"]] = suma
            retorno[elemento["Código subsector económico"]]["Código subsector económico"] = elemento["Código subsector económico"]

            retorno[elemento["Código subsector económico"]]["Nombre subsector económico"] = elemento["Nombre subsector económico"]
        
            retorno[elemento["Código subsector económico"]]["Total ingresos netos del subsector económico"] += float(elemento["Total ingresos netos"])

            retorno[elemento["Código subsector económico"]]["Total costos y gastos del subsector económico"] += float(elemento["Total costos y gastos"])

            retorno[elemento["Código subsector económico"]]["Total saldo a pagar del subsector económico"] += float(elemento["Total saldo a pagar"])

            retorno[elemento["Código subsector económico"]]["Total saldo a favor del subsector económico"] += float(elemento["Total saldo a favor"])

            sub_dict = {
                "Código actividad económica" : elemento["Código actividad económica"],
                "Nombre actividad económica" : elemento["Nombre actividad económica"],
                "Total ingresos netos": elemento["Total ingresos netos"],
                "Total costos y gastos":elemento["Total costos y gastos"],
                "Total saldo a pagar":elemento["Total saldo a pagar"],
                "Total saldo a favor":elemento["Total saldo a favor"]
            }
   
            if float(elemento["Total ingresos netos"]) > float(retorno[elemento["Código subsector económico"]]["Actividad económica que más aporto"]["Total ingresos netos"]):
                retorno[elemento["Código subsector económico"]]["Actividad económica que más aporto"]["Total ingresos netos"] = elemento["Total ingresos netos"]
                retorno[elemento["Código subsector económico"]]["Actividad económica que más aporto"]["data"] = sub_dict

            if float(elemento["Total ingresos netos"]) < float(retorno[elemento["Código subsector económico"]]["Actividad económica que menos aporto"]["Total ingresos netos"]):
                retorno[elemento["Código subsector económico"]]["Actividad económica que menos aporto"]["Total ingresos netos"] = elemento["Total ingresos netos"]
                retorno[elemento["Código subsector económico"]]["Actividad económica que menos aporto"]["data"] = sub_dict
    return retorno
        
def filter_table1_req6(data_table1):
    retorno = {"Código sector económico":[],
               "Nombre sector económico":[],
               "Total costos y gastos del sector económico":[],
               "Total saldo a favor del sector económico":[],
               "Total saldo a favor del sector económico":[]}
    for dicc in iterator(data_table1):
        for key_dict in dicc.items():
                for key_value in key_dict[1].items():
                    if key_value[0] in retorno.keys():
                        retorno[key_value[0]].append(key_value[1])

    return retorno
 
def filter_table2_req6(data_table2):

    to_sort = lt.newList("ARRAY_LIST")
    for subsectors in iterator(data_table2):
        for subsec_dic in subsectors.values():
            lt.addLast(to_sort,subsec_dic)
    retorno = to_sort_req6(to_sort)
    obtain_less = lt.subList(retorno,1,3)
    obtain_most = lt.subList(retorno,lt.size(retorno)-2,3)
    return [obtain_less,obtain_most]

def to_sort_req6(list):
    list = merg.sort(list,cmpmaxreq6)
    return list

def cmpmaxreq6(dicc1, dicc2):
    if float(dicc1["Total ingresos netos del subsector económico"]) < float(dicc2["Total ingresos netos del subsector económico"]):
        return True
    else:
        return False


def req_7(data_structs, anio_inicial , anio_final, top_n):
    """
    Función que soluciona el requerimiento 7
    """
    anio_inicial = int(anio_inicial)
    años = lt.newList("ARRAY_LIST")
    data_filter = lt.newList("ARRAY_LIST")
    while anio_inicial <= int(anio_final):
        lt.addLast(años, str(anio_inicial))
        anio_inicial += 1
    for año_list in data_structs.items():
        if año_list[0] in años["elements"]:
            lt.addLast(data_filter, año_list[1])
    data_filter = obtain_list(data_filter)
    data_filter = sort_req7(data_filter)
    data_filter = (lt.subList(data_filter, 0, top_n))
    return(data_filter)

def cmpreq7(dicc1,dicc2):
    if float(dicc1["Total costos y gastos"]) < float(dicc2["Total costos y gastos"]):
        return True
    else: 
        return False
    

def sort_req7(filter_data):
    filter_data = merg.sort(filter_data,cmpreq7)
    return filter_data
        
def obtain_list(list_of_list):
    retorno = lt.newList("ARRAY_LIST")
    for list_anio in iterator(list_of_list):
        for registro in iterator(list_anio):
            lt.addLast(retorno,registro)
    return retorno

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def comparemin(data1,data2):
    if float(data1["Total retenciones"]) < float(data2["Total retenciones"]):
        return True
    else:
        return False
    
def comparemax(data1,data2):
    if float(data1["Total retenciones"]) > float(data2["Total retenciones"]):
        return True
    else:
        return False

def comparemin1(data1,data2):
    if float(data1["Costos y gastos nómina"]) > float(data2["Costos y gastos nómina"]):
        return True
    elif float(data1["Costos y gastos nómina"]) < float(data2["Costos y gastos nómina"]):
        return False
    
def comparemax1(data1,data2):
    if float(data1["Costos y gastos nómina"]) < float(data2["Costos y gastos nómina"]):
        return True
    elif float(data1["Costos y gastos nómina"]) > float(data2["Costos y gastos nómina"]):
        return False
    
def sortsublist_max1(registr,maxi_mini):
    if lt.size(maxi_mini) > 3:
        lt.addLast(maxi_mini,registr)
    merg.sort(maxi_mini,comparemax1)
    if lt.size(maxi_mini) > 3:
        lt.removeFirst(maxi_mini)

def sortsublist_mini1(registr,maxi_mini):
    if lt.size(maxi_mini) > 3:
        lt.addLast(maxi_mini,registr)
    merg.sort(maxi_mini,comparemin1)
    if lt.size(maxi_mini) > 3:
        lt.removeFirst(maxi_mini)


def sortsubsectors1(dicci_anios):
    sorted_anios  = lt.newList("ARRAY_LIST")
    for anio in iterator(dicci_anios):
        min = {"Costos y gastos nómina":0}
        for subsec in anio.values():
            if float(subsec["Costos y gastos nómina"]) > min["Costos y gastos nómina"]:
                  min = subsec
        lt.addLast(sorted_anios,min)
    return sorted_anios


def cmp_impuestos_by_anio_CAE(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not data_1["Código actividad económica"].isnumeric() or not data_2["Código actividad económica"].isnumeric():
        data_1["Código actividad económica"] = data_1["Código actividad económica"].replace("/","")
        data_2["Código actividad económica"]= data_2["Código actividad económica"].replace("/","")
        if len(data_1["Código actividad económica"]) > 4 or len(data_2["Código actividad económica"]) > 4:
            data_1["Código actividad económica"] = data_1["Código actividad económica"][0:4]
            data_2["Código actividad económica"] = data_2["Código actividad económica"][0:4]
    if (float(data_1['Año']) < float(data_2['Año'])):
        return True 
    elif (float(data_1['Año']) > float(data_2['Año'])):
        return False
    else:
        if float(data_1["Código actividad económica"]) < float(data_2["Código actividad económica"]):
            return True
        else:
            return False


# Funciones de ordenamiento

def sortsublist_max(registr,maxi_mini):
    if lt.size(maxi_mini) > 3:
        lt.addLast(maxi_mini,registr)
    merg.sort(maxi_mini,comparemax)
    if lt.size(maxi_mini) > 3:
        lt.removeFirst(maxi_mini)

def sortsublist_mini(registr,maxi_mini):
    if lt.size(maxi_mini) > 3:
        lt.addLast(maxi_mini,registr)
    merg.sort(maxi_mini,comparemin)
    if lt.size(maxi_mini) > 3:
        lt.removeFirst(maxi_mini)


def sortsubsectors(dicci_anios):
    sorted_anios  = lt.newList("ARRAY_LIST")
    for anio in iterator(dicci_anios):
        min = {"Total de retenciones del subsector económico":100000000000000}
        for subsec in anio.values():
            if float(subsec["Total de retenciones del subsector económico"]) < min["Total de retenciones del subsector económico"]:
                  min = subsec
        lt.addLast(sorted_anios,min)
    return sorted_anios

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs['datos'],cmp_impuestos_by_anio_CAE)

def sortby(control_model, sort_met):
    if sort_met == "Selection Sort":
        se.sort(control_model["datos"], cmp_impuestos_by_anio_CAE)
    elif sort_met == "Insertion Sort":
        ins.sort(control_model["datos"], cmp_impuestos_by_anio_CAE)
    elif sort_met == "Shell Sort":
        sa.sort(control_model["datos"], cmp_impuestos_by_anio_CAE)
    elif sort_met == "Quick Sort":
        quk.sort(control_model["datos"], cmp_impuestos_by_anio_CAE)
    elif sort_met == "Merge Sort":
        merg.sort(control_model["datos"], cmp_impuestos_by_anio_CAE)


def iterator(datastructure):
    return lt.iterator(datastructure)

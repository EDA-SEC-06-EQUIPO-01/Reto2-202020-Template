"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
from time import process_time
import csv
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def timer(func):
    def inner(*args, **kwargs):
        t1 = process_time()
        ret = func(*args, **kwargs)
        t2 = process_time()
        print(
            f"El tiempo que tardó la funcion {func.__name__} fue de {t2 - t1} segundos."
        )
        return ret

    return inner


@timer
def load_csv(filepath: str, sep=";", impl="SINGLE_LINKED", cmpfunction=None):
    lst = lt.newList(impl, cmpfunction)
    print(f"Cargando archivo {filepath} {'.'*5}")
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(config.data_dir + filepath, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for el in row:
                lt.addLast(lst, el)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def cmpkey(element, node):
    return 0 if element == node["key"] else 1


@timer
def load_csv_map_byAttribute(filepath: str, attribute, impl="CHAINING"):
    sep = ";"
    map = mp.newMap(1000, comparefunction=cmpkey)
    print(f"Cargando archivo {filepath} {'.'*5}")
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(config.data_dir + filepath, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for el in row:
                att = el[attribute]
                if mp.contains(map, att):
                    tmp = mp.get(map, att)["value"]
                    lt.addLast(tmp, el)
                    mp.put(map, att, tmp)
                else:
                    tmp_lst = lt.newList()
                    lt.addLast(tmp_lst, el)
                    mp.put(map, att, tmp_lst)

    except:
        print("Hubo un error con la carga del archivo")
    return map


# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================

def req1_conocer_un_director():
    1

# ==============================
# Funciones de Comparacion
# ==============================

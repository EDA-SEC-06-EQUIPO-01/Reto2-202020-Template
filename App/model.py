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
from DISClib.DataStructures import listiterator as it
import helper as h

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
            f"El tiempo que tardó la funcion {func.__name__} fue de {t2 - t1} segundos.\n"
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
def load_csv_map_byAttribute(filepath: str, attribute, impl="CHAINING", loadfactor=1.0):
    sep = ";"
    map = mp.newMap(1000, comparefunction=cmpkey,
                    maptype=impl, loadfactor=loadfactor)
    print(f"Cargando archivo {filepath} {'.'*5}")
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(config.data_dir + filepath, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for el in row:
                att = el[attribute]
                atts = att.split("|")
                for e in atts:
                    if mp.contains(map, e):
                        tmp = mp.get(map, e)["value"]
                        lt.addLast(tmp, el)
                        mp.put(map, e, tmp)
                    else:
                        tmp_lst = lt.newList()
                        lt.addLast(tmp_lst, el)
                        mp.put(map, e, tmp_lst)

    except:
        print("Hubo un error con la carga del archivo")
    return map


@timer
def load_csv_map_byAtts(filepath: str, atts, impl="CHAINING", loadfactor=1.0):
    sep = ";"
    map = mp.newMap(1000, comparefunction=cmpkey,
                    maptype=impl, loadfactor=loadfactor)
    print(f"Cargando archivo {filepath} {'.'*5}")
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(config.data_dir + filepath, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for el in row:
                for at in atts:
                    att = el[at]
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

@timer
def req3_conocer_un_actor(filepath_casting: str, nombre: str, mp_details, mp_casting):
    mp_actores = load_csv_map_byAtts(
        filepath_casting, ("actor1_name", "actor2_name", "actor3_name", "actor4_name", "actor5_name"))
    try:
        actor = mp.get(mp_actores, nombre)['value']
        actor_it = it.newIterator(actor)

        movies = lt.newList()
        votes = []
        while it.hasNext(actor_it):
            movie = dict(it.next(actor_it))
            det_movie = dict(lt.firstElement(
                dict((mp.get(mp_details, movie['id'])))['value']))
            lt.addLast(movies, det_movie['title'])
            votes.append(
                float(det_movie['vote_average']))
        media = sum(votes)/len(votes)
        return movies, mp.size(actor), round(media, 2)

    except:
        print(
            f"El actor {nombre} no existe en el archivo csv.")
        return None


def descubrir_productoras(map_productoras, prod):
    lst = mp.get(map_productoras, prod)["value"]
    length = lt.size(lst)
    avg_vote_lst = [int(i["vote_count"]) for i in h.travel(lst)]
    avg_vote = sum(avg_vote_lst) / len(avg_vote_lst)

    return lst, length, avg_vote


def entender_genero(map_genero, genero):
    lst = mp.get(map_genero, genero)["value"]
    length = lt.size(lst)
    avg_vote_lst = [int(i["vote_count"]) for i in h.travel(lst)]
    avg_vote = sum(avg_vote_lst) / len(avg_vote_lst)

    return lst, length, avg_vote


def pel_countrie(m_pais, m_id_cast, pais):
    lst = mp.get(m_pais, pais)["value"]

    dir = [
        mp.get(m_id_cast, i)["value"]["first"]["info"]["director_name"]
        for i in h.travel(lst, "id")
    ]

    return lst, dir


# ==============================
# Funciones de Comparacion
# ==============================

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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Requerimiento 1 - Descubrir productoras de cine")
    print("3- Requerimiento 2 - Conocer a un director")
    print("4- Requerimiento 3 - Conocer a un actor")
    print("5- Requerimiento 4 - Entender un género cinematográfico")
    print("6- Requerimiento 5 - Encontrar películas por país")
    print("0- Salir")


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def timer(func):
    return model.timer(func)


def load_csv_map_byAttribute(filepath: str, attribute, impl="CHAINING"):
    return model.load_csv_map_byAttribute(filepath, attribute, impl)


def load_csv_map_byAtts(filepath: str, *atts, impl="CHAINING", loadfactor=1.0):
    return model.load_csv_map_byAtts(filepath, atts, impl, loadfactor)


def load_csv(name: str, sep=";", impl="SINGLE_LINKED", cmpfunction=None):
    return model.load_csv(name, sep, impl, cmpfunction)


def req3(filepath_casting: str, nombre: str, mp_details, mp_casting):
    return model.req3_conocer_un_actor(filepath_casting, nombre, mp_details, mp_casting)


def descubrir_productoras(map_productoras, prod):
    return model.descubrir_productoras(map_productoras, prod)


def entender_genero(map_genero, genero):
    return model.entender_genero(map_genero, genero)

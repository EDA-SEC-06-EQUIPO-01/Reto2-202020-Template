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
import sys




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
    print("0- Salir")







# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def main():
    movies_dir = "themoviesdb/"
    details = movies_dir + "SmallMoviesDetailsCleaned.csv"
    casting = movies_dir + "MoviesCastingRaw-small.csv"
    while True:
            printMenu()  # imprimir el menu de opciones en consola
            # leer opción ingresada
            inputs = input("Seleccione una opción para continuar\n")
            if len(inputs) > 0:

                if int(inputs[0]) == 1:  # opcion 1
                    lista_details = model.load_CSV(
                        details, impl="ARRAY_LIST", cmpfunction=None
                    )
                    lista_casting = model.load_CSV(
                        casting, impl="ARRAY_LIST", cmpfunction=None
                    )
                elif int(inputs[0]) == 0:  # opcion 0, salir
                    sys.exit(0)
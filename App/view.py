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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller

assert config

movies_dir = "themoviesdb/"
details = movies_dir + "SmallMoviesDetailsCleaned.csv"
casting = movies_dir + "MoviesCastingRaw-small.csv"

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def main():

    while True:
        controller.printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input("Seleccione una opción para continuar\n")
        if len(inputs) > 0:

            if int(inputs[0]) == 1:  # opcion 1
                # lista_details = controller.load_csv(
                #     details, impl="ARRAY_LIST", cmpfunction=None
                # )
                # lista_casting = controller.load_csv(
                #     casting, impl="ARRAY_LIST", cmpfunction=None
                # )

                # IMPORTANT
                # interface to charge data into a map
                # add load factor
                mp = controller.load_csv_map(casting, "director_name")

                # replace all of below

                print("En la lista details.")
                print(f"Se han cargado {lt.size(lista_details)}")

                # Impresión primer elemento details
                print("\tDel primer elemento:")
                fe = lt.firstElement(lista_details)
                print(f"\t\tTítulo: {fe['title']}")
                print(f"\t\tFecha: {fe['release_date']}")
                print(f"\t\tPromedio votos: {fe['vote_average']}")
                print(f"\t\tNúmero votos: {fe['vote_count']}")
                print(f"\t\tLenguaje original: {fe['original_language']}")

                # Impresión último elemento details
                print("\tDel último elemento:")
                le = lt.lastElement(lista_details)
                print(f"\t\tTítulo: {fe['title']}")
                print(f"\t\tFecha: {fe['release_date']}")
                print(f"\t\tPromedio votos: {fe['vote_average']}")
                print(f"\t\tNúmero votos: {fe['vote_count']}")
                print(f"\t\tLenguaje original: {fe['original_language']}")

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


main()

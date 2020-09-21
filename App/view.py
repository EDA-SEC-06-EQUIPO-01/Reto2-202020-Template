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
from DISClib.ADT import map as mp
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

                casting_key = "director_name"
                details_key = "genres"

                mp_casting = controller.load_csv_map(casting, casting_key)
                mp_details = controller.load_csv_map(details, details_key)

                # Prueba en consola de que carga los datos correctamente

                print("Se han cargado los mapas details y casting.")
                print(
                    f"Del mapa casting, se han cargado {mp.size(mp_casting)} elementos")
                print(
                    f"Del mapa details, se han cargado {mp.size(mp_details)} elementos")

                iteration = it.newIterator(mp.keySet(mp_casting))
                print(
                    f"\nLas llaves del mapa casting, respecto a la llave {casting_key} son:")
                while it.hasNext(iteration):
                    key = it.next(iteration)
                    print(f'\t{key}')

                iteration = it.newIterator(mp.keySet(mp_details))
                print(
                    f"\nLas llaves del mapa details, respecto a la llave {details_key} son:")
                while it.hasNext(iteration):
                    key = it.next(iteration)
                    print(f'\t{key}')

                print(
                    f"Como prueba final, se mostrará el valor asociado a la llave '{key}' en el map_details:\n")
                print(mp.get(mp_details, key))

                print()

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


main()

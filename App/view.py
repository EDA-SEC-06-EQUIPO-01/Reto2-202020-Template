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
import helper as h

assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

movies_dir = "themoviesdb/"
details = movies_dir + "SmallMoviesDetailsCleaned.csv"
casting = movies_dir + "MoviesCastingRaw-small.csv"

# ___________________________________________________
#  Funciones para imprimir la información de
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
                casting_key = "id"
                details_key = "id"

                mp_casting = controller.load_csv_map_byAtts(casting, casting_key)
                mp_details = controller.load_csv_map_byAtts(details, details_key)

                print(
                    f"Se crearon los maps:\n\tcasting, con {mp.size(mp_casting)} elementos, ordenado por la llave {casting_key}\n\tdetails, con {mp.size(mp_details)} elementos, ordenado por la llave {details_key}"
                )
            elif int(inputs[0]) == 2:
                pass
            elif int(inputs[0]) == 3:
                pass
            elif int(inputs[0]) == 4:
                genero = input("Digite el género sobre el cuál desea trabajar:\n")
                g = controller.load_csv_map_byAttribute(details, "genres")

                lista, longitud, promedio = controller.entender_genero(g, genero)

                cont = 0
                print("Las películas que tienen dicho género son\n")
                for i in h.travel(lista, parameter="title"):
                    cont += 1
                    print(f"{cont}. {i}")
                print(f"En total son {longitud} películas.")
                print(
                    f"El voto promedio para las películas de género {genero} es {promedio}"
                )
                print()
            elif int(inputs[0]) == 5:
                pass
            elif int(inputs[0]) == 6:
                pass
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


main()

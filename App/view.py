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
import prettytable as pt 
import datetime as dt
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("0- Salir")
    #No olvidar el pdf de analisis

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def lastArtist(catalog):
    """
    Muestra los ultimos 3 artistas
    """
    return controller.lastArtist(catalog)

def lastArtwork(catalog):
    """
    Muestra las ultimas 3 obras
    """
    return controller.lastArtwork(catalog)


# def printAuthorData(author):
#     if author:
#         print('Autor encontrado: ' + author['name'])
#         print('Promedio: ' + str(author['average_rating']))
#         print('Total de libros: ' + str(lt.size(author['books'])))
#         for book in lt.iterator(author['books']):
#             print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
#     else:
#         print('No se encontro el autor')


# def printBestBooks(books):
#     size = lt.size(books)
#     if size:
#         print(' Estos son los mejores libros: ')
#         for book in lt.iterator(books):
#             print('Titulo: ' + book['title'] + '  ISBN: ' +
#                   book['isbn'] + ' Rating: ' + book['average_rating'])
#     else:
#         print('No se encontraron libros')

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Numero de artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Numero de obras cargadas: ' + str(lt.size(catalog['artworks']))+"\n")

        print('Ultimos 3 artistas:\n' + str((catalog)))
        print('Ultimas 3 obras:\n' + str(lastArtwork(catalog)))

    elif int(inputs[0])==2:
        first=int(input("Año inicial: "))
        last=int(input("Año final: "))
        
        print("="*15+ "Req No. 1 Inputs"+ "="*15)
        print("Artist born between "+ str(first)+" and " +str(last))
        print("="*15, "Req No. 1 Answers", "="*15)
        cronologicalArtists=controller.cronologicalArtists(catalog,first,last)
        print("Total de artistas: ", cronologicalArtists[1])
        print(cronologicalArtists[0])
        pass
#
    elif int(inputs[0])==3:
        firstY=int(input("Año incial: "))
        firstM=int(input("Mes incial: "))
        firstD=int(input("Dia inicial: "))
        first=dt.date(firstY,firstM,firstD)

        lastY=int(input("Año final: "))
        lastM=int(input("Mes final: "))
        lastD=int(input("Dia final: "))
        last=dt.date(lastY,lastM,lastD)

        print("="*15+ "Req No. 2 Inputs"+ "="*15)
        print("Artwork aquired between "+ str(first)+" and " +str(last))
        print("="*15, "Req No. 2 Answers", "="*15)
        
        cronologicalArtwork=controller.cronologicalArtwork(catalog, first, last)
        print("Total of unique pieces aquired: ", cronologicalArtwork[1])
        print("Total of artwork purchased: ", cronologicalArtwork[2])
        
        table= pt.PrettyTable()
        table.field_names=["ObjectID","Title","ArtistsNames","Medium","Dimensions","Date","DateAquired","URL"]
        # table.max_width=40
        # for n in range(1,4):
        # line=lt.getElement(cronologicalArtwork[0],2)
        # table.add_row([line["id"],line["title"],"None",line["medium"],line["dimensions"],line["date"],line["date_aquired"],line["url"]])
        # print(table)
        print(lt.size(cronologicalArtwork[0]))
        pass

    # elif int(inputs[0]) == 2:
    #     number = input("Buscando los TOP ?: ")
    #     books = controller.getBestBooks(catalog, int(number))
    #     printBestBooks(books)

    # elif int(inputs[0]) == 3:
    #     authorname = input("Nombre del autor a buscar: ")
    #     author = controller.getBooksByAuthor(catalog, authorname)
    #     printAuthorData(author)

    # elif int(inputs[0]) == 4:
    #     label = input("Etiqueta a buscar: ")
    #     book_count = controller.countBooksByTag(catalog, label)
    #     print('Se encontraron: ', book_count, ' Libros')

    else:
        sys.exit(0)
sys.exit(0)


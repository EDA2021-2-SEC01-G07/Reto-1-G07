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
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

catalog = None

def printMenu():
    print("Welcome")
    print("1- Load information in the Catalog")
    print("2- List cronologically the artists")
    print("3- List cronologically the adquisitions")
    print("4- Classify the artworks of an artist by technique/medium")
    print("5- Classify the artworks by the nationality of their creators")
    print("0- Exit")

def printLoadCatalog():
    global catalog
    print("Cargando información de los archivos ....")
    catalog = initCatalog()
    loadData(catalog)
    print('Numero de artistas cargados: ' + str(lt.size(catalog['artists'])))
    print('Numero de obras cargadas: ' + str(lt.size(catalog['artworks']))+"\n")

    print('Ultimos 3 artistas:\n' + str(lastArtist(catalog)))
    print('Ultimas 3 obras:\n' + str(lastArtwork(catalog)))

def printCronologicallyArtists():
    global catalog
    first=int(input("Año inicial: "))
    last=int(input("Año final: "))
    
    print("="*15+ "Req No. 1 Inputs"+ "="*15)
    print("Artist born between "+ str(first)+" and " +str(last))
    print("="*15, "Req No. 1 Answers", "="*15)
    cronologicalArtists=controller.cronologicalArtists(catalog,first,last)
    print("Total de artistas: ", cronologicalArtists[1])
    table= pt.PrettyTable()
    table.field_names=["ConstituentID","DisplayName","BeginDate","Nationality","Gender","ArtistBio","Wiki QID","ULAN"]
    table.max_width=30
    for n in range(1,7):
        line=lt.getElement(cronologicalArtists[0],n)
        table.add_row([line["id"],line["name"],line["begin_date"],line["nationality"],line["gender"],line["biography"],line["wiki_id"],line["ulan"]])
    print(table)

def printCronologicallyArtworks():
    global catalog
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

def printArtistMediums():
    global catalog
    print("="*15 + " Req No. 3 Inputs " + "="*15)
    artist_name = input("Examine the work of the artist named: ")
    artist = controller.getArtist(catalog, artist_name)
    top_artworks, medium_ranking = controller.techniquesFromArtist(catalog, artist)
    artist_id = artist['id']

    total_artworks = 0
    for ranking in lt.iterator(medium_ranking):
        total_artworks += ranking['len']

    print(f'''\n{"="*15} Req No. 3 Answer {"="*15}n
{artist_name} with MoMA ID {artist_id} has {total_artworks} in his/her name at the museum\n
There are {lt.size(medium_ranking)} different mediums/techniques in his/her work.\n
Her/His top 5 Medium/Technique are:''')
    tb = pt.PrettyTable()
    tb.field_names = ['MediumName', 'Count']
    tb.hrules = pt.ALL

    done = 1
    while done < 6:
        element = lt.getElement(medium_ranking, done)
        tb.add_row([element['medium'], element['len']])
        done += 1
    
    tb.align['MediumName'] = 'l'
    tb.align['Count'] = 'r'
    print(tb)

    top_element = lt.getElement(medium_ranking, 1)
    top_medium = top_element['medium']
    top_length = top_element['len']
    print(f'\nHis/Her most used Medium/Technique is: {top_medium} with {top_length}.')
    print(f'A sample of {top_length} {top_medium} from the collection are:')

    tb = pt.PrettyTable()
    tb.field_names = ['ObjectID', 'Title', 'Medium', 'Date', 'Dimensions',
     'DateAcquired', 'Department', 'Classification', 'URL']
    tb._max_width = {'Title': 20, 'Dimensions': 20, 'URL': 20}
    tb.hrules = pt.ALL

    for row in lt.iterator(top_artworks):
        tb.add_row([row['id'], row['title'], row['medium'], row['date'], row['dimensions'],
         row['date_aquired'], row['department'], row['classification'], row['url']])
    print(tb)

def printArtworkNationality():
    global catalog
    nationalities=controller.sortByNationality(catalog)
    print("="*15+ "Req No. 4 Inputs"+ "="*15)
    print("Ranking countries by their number of artworks in the MoMA...\n")
    print("="*15, "Req No. 4 Answers", "="*15)
    print("The TOP 10 Countries in the MoMA are:")
    
    table= pt.PrettyTable()
    table.field_names=["Nationality","Artworks"]
    table.hrules = pt.ALL
    table.max_width=30
    for n in range(1,11):
        line=lt.getElement(nationalities[0],n)
        table.add_row([line["nationality"],line["Artworks"]])
    print(table)     
    print("\nThe TOP nacionality in the museum is",nationalities[2],"with", nationalities[3],"unique pieces.")
    print("The first and last 3 objects in the",nationalities[2],"artwork list are:")  
    table2=pt.PrettyTable()
    table2.field_names=["ObjectID","Title","ArtistsNames","Medium","Date","Dimensions","Department","Classification","URL"]
    
    for n in lt.iterator(nationalities[1]):
        nombres=str(n["Names"])
        nombres=nombres[1:len(nombres)-1].replace("'","")
        table2.add_row([n["id"],n["title"],nombres,n["medium"],n["date"],n["dimensions"],n["department"],n["classification"],n["url"]])
    table2.align="l"
    table2._max_width={"ObjectID":17,"Title":17,"ArtistsNames":18,"Medium":18,"Date":17,"Dimensions":18,"Department":15,"Classification":17,"URL":22}
    table2.hrules = pt.ALL
    print(table2)

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

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printLoadCatalog()
    elif int(inputs[0])==2:
        printCronologicallyArtists()
    elif int(inputs[0])==3:
        printCronologicallyArtworks()
    elif int(inputs[0])==4:
        printArtistMediums()
    elif int(inputs[0])==5:
        printArtworkNationality()
    else:
        sys.exit(0)


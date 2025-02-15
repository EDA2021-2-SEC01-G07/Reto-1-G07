﻿"""
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
import time
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
    print("6- Transport artworks by deparment")
    print("0- Exit")

def printLoadCatalog():#Input 1
    global catalog
    print("Cargando información de los archivos ....")
    start_time = time.process_time()
    catalog = initCatalog()
    loadData(catalog)
    end_time=(time.process_time() - start_time)*1000
    print('Numero de artistas cargados: ' + str(lt.size(catalog['artists'])))
    print('Numero de obras cargadas: ' + str(lt.size(catalog['artworks']))+"\n")

    print('Ultimos 3 artistas:\n' + str(lastArtist(catalog)))
    print('Ultimas 3 obras:\n' + str(lastArtwork(catalog)))
    print("The processing time is: ",end_time, " ms.")
def printCronologicallyArtists():#Input 2
    global catalog
    first=int(input("Año inicial: "))
    last=int(input("Año final: "))
    start_time = time.process_time()
    print("="*15+ "Req No. 1 Inputs"+ "="*15)
    print("Artist born between "+ str(first)+" and " +str(last))
    print("="*15, "Req No. 1 Answers", "="*15)
    cronologicalArtists=controller.cronologicalArtists(catalog,first,last)
    end_time=(time.process_time() - start_time)*1000
    print("Total de artistas: ", cronologicalArtists[1])
    table= pt.PrettyTable()
    table.field_names=["ConstituentID","DisplayName","BeginDate","Nationality","Gender","ArtistBio","Wiki QID","ULAN"]
    table.max_width=30
    for n in range(1,7):
        line=lt.getElement(cronologicalArtists[0],n)
        table.add_row([line["id"],line["name"],line["begin_date"],line["nationality"],line["gender"],line["biography"],line["wiki_id"],line["ulan"]])
    print(table)
    print("The processing time is: ",end_time, " ms.")

def printCronologicallyArtworks():#Input 3
    global catalog
    firstY=int(input("Año incial: "))
    firstM=int(input("Mes incial: "))
    firstD=int(input("Dia inicial: "))
    first=dt.date(firstY,firstM,firstD)

    lastY=int(input("Año final: "))
    lastM=int(input("Mes final: "))
    lastD=int(input("Dia final: "))
    last=dt.date(lastY,lastM,lastD)
    start_time = time.process_time()
    print("="*15+ "Req No. 2 Inputs"+ "="*15)
    print("Artwork aquired between "+ str(first)+" and " +str(last))
    print("="*15, "Req No. 2 Answers", "="*15)
    
    foundArtwork, totalArtwork, purchased = controller.cronologicalArtwork(catalog, first, last)
    print(f'The MoMA acquired {totalArtwork} unique pieces between {firstY}-{firstM}-{firstD} and {lastY}-{lastM}-{lastD}')
    print(f'With {lt.size(foundArtwork)} different artists and purchased {purchased} of them')
    print("The first and last 3 artists in the range are...")
    artist_dict=controller.getArtistDict(catalog["artists"])
    controller.addArtworkArtists(foundArtwork,artist_dict)
    end_time=(time.process_time() - start_time)*1000
    table= pt.PrettyTable()
    table.field_names=["ObjectID","Title","ArtistsNames","Medium","Dimensions","Date","DateAquired","URL"]
    table.max_width=40
    for n in range(1,7):
        line=lt.getElement(foundArtwork, n)
        names=str(line["Names"])
        names=names[1:len(names)-1].replace("'","")
        table.add_row([line["id"],line["title"],names,line["medium"],line["dimensions"],line["date"],line["date_aquired"],line["url"]])
    table._max_width={"ObjectID":17,"Title":17,"ArtistsNames":17,"Medium":21,"Dimensions":21,"Date":17,"DateAquired":17,"URL":21}
    print(table)
    print("The processing time is: ",end_time, " ms.")

def printArtistMediums():#Input 4
    global catalog
    print("="*15 + " Req No. 3 Inputs " + "="*15)
    artist_name = input("Examine the work of the artist named: ")
    start_time = time.process_time()
    artist = controller.getArtist(catalog, artist_name)
    top_artworks, medium_ranking = controller.techniquesFromArtist(catalog, artist)
    artist_id = artist['id']

    total_artworks = 0
    for ranking in lt.iterator(medium_ranking):
        total_artworks += ranking['len']
    end_time=(time.process_time() - start_time)*1000
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
    print("The processing time is: ",end_time, " ms.")

def printArtworkNationality():#Input 5
    global catalog
    start_time = time.process_time()
    nationalities=controller.sortByNationality(catalog)
    print("="*15+ "Req No. 4 Inputs"+ "="*15)
    print("Ranking countries by their number of artworks in the MoMA...\n")
    print("="*15, "Req No. 4 Answers", "="*15)
    print("The TOP 10 Countries in the MoMA are:")
    end_time=(time.process_time() - start_time)*1000
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
        names=str(n["Names"])
        names=names[1:len(names)-1].replace("'","")
        table2.add_row([n["id"],n["title"],names,n["medium"],n["date"],n["dimensions"],n["department"],n["classification"],n["url"]])
    table2.align="l"
    table2._max_width={"ObjectID":17,"Title":17,"ArtistsNames":18,"Medium":18,"Date":17,"Dimensions":18,"Department":15,"Classification":17,"URL":22}
    table2.hrules = pt.ALL
    print(table2)
    print("The processing time is: ",end_time, " ms.")

def printcostFromDepartment():#Input 6
    global catalog
    department= input("Search for department named: ")
    start_time = time.process_time()
    transportation=controller.costFromDepartment(catalog,department)
    artwork_dict=controller.getArtworkDict(catalog["artworks"])
    artist_dict=controller.getArtistDict(catalog["artists"])
    total_cost=0
    for key in transportation[3]:
        total_cost+=transportation[3][key]
    weight=0
    for artwork in lt.iterator(transportation[1]):
        if artwork["weight"]!="Unknown":
            weight+=float(artwork["weight"])
    print("="*15 + " Req No. 5 Inputs " + "="*15)
    print("Estimate the cost to transport all artifacts in ",department," MoMA's Department")
    print("="*15 + " Req No. 5 Answers " + "="*15)
    print("The MoMA is going to transport ",lt.size(transportation[0])," artifacts from the ",department)
    print("REMEMBER!, NOT all MoMA's data is complete!!!...These are ESTIMATES!!!!")
    print("Estimated cargo weight (kg): " ,round(weight,3))
    print("Estimated cargo cost (USD): ", round(total_cost,3))
    print("The TOP 5 most expensive items to transport are:")
    tb = pt.PrettyTable()
    tb.field_names = ['ObjectID', 'Title',"ArtistsNames", 'Medium', 'Date', 'Dimensions',
     'Classifications', 'TransCost (USD)', 'URL']
    contador=0
    controller.addArtworkArtists(transportation[1],artist_dict)
    end_time=(time.process_time() - start_time)*1000
    for i in lt.iterator(transportation[0]):
        if contador >4:
            break
        code=i["artwork"]
        artwork=artwork_dict[code]
        
        names=[]
        for artist in transportation[2][code]:
            names.append(artist["name"])
        names=str(names)
        tb.add_row([code,artwork["title"],names[1:len(names)-1].replace("'",""),artwork["medium"],artwork["date"],artwork["dimensions"],
        artwork["classification"],round(i["cost"],4),artwork["url"]])
        contador+=1
    tb._max_width ={'ObjectID':17, 'Title':17,"ArtistsNames":17, 'Medium':17, 'Date':17, 'Dimensions':17,
     'Classifications':17, 'TransCost (USD)':17, 'URL':17}
    print(tb)

    print("The TOP 5 oldest items to transport are: ")
    tb2 = pt.PrettyTable()
    tb2.field_names = ['ObjectID', 'Title',"ArtistsNames", 'Medium', 'Date', 'Dimensions',
     'Classifications', 'TransCost (USD)', 'URL']
    contador=0
    for i in lt.iterator(transportation[1]):
        if contador >4:
            break
        id=i["id"]
        cost=transportation[3][id]
        names=str(i["Names"])
        names=names[1:len(names)-1].replace("'","")
        tb2.add_row([id,i["title"],names,i["medium"],i["date"],i["dimensions"],
        i["classification"],round(cost,4),i["url"]])
        contador+=1
    tb2._max_width ={'ObjectID':17, 'Title':17,"ArtistsNames":17, 'Medium':17, 'Date':17, 'Dimensions':17,
     'Classifications':17, 'TransCost (USD)':17, 'URL':17}
    print(tb2)
    print("The processing time is: ",end_time, " ms.")
    
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
    elif int(inputs[0])==6:
        printcostFromDepartment()
    else:
        sys.exit(0)


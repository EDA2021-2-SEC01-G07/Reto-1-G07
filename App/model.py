﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.DataStructures.arraylist import newList
import config as cf
from DISClib.ADT import list as lt
import datetime as dt
from DISClib.Algorithms.Sorting import mergesort
from typing import Tuple, Dict, Callable
from math import pi

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

ADTList = Dict[str, any]

def newCatalog():
    catalog = {
        'artists': None,
        'artworks': None
        
    }
    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')
    
    return catalog
    
def newArtist(id, name, biography, nationality, gender, begin_date, end_date, wiki_id, ulan):
    artist = {'id': id,
    'name': name,
    'biography': biography,
    'nationality': nationality,
    'gender': gender,
    'begin_date': int(begin_date),
    'end_date': int(end_date),
    'wiki_id': wiki_id,
    'ulan': ulan
    }
    for key in artist:
        if artist[key] == "":
            artist[key] = "Unknown"
    return artist

def newArtwork(id, title, constituent_id, date, medium, dimensions, credit_line,
accession_number, classification, department, date_aquired, cataloged, url, circumference,
depth, diameter, height, lenght, weight, width, seat_height, duration):
    artwork = {"id": id,
    "title": title,
    "constituent_id": constituent_id,
    "date": date,
    "medium": medium,
    "dimensions": dimensions,
    "credit_line": credit_line,
    "accession_number": accession_number,
    "classification": classification,
    "department": department,
    "date_aquired": date_aquired,
    "cataloged": cataloged,
    "url": url,
    "circumference": circumference,
    "depth": depth,
    "diameter": diameter,
    "height": height,
    "lenght": lenght,
    "weight": weight,
    "width": width,
    "seat_height": seat_height,
    "duration": duration
    }

    for key in artwork:
        if artwork[key] == '':
            artwork[key] = "Unknown"
    return artwork

def addArtwork(catalog, artwork):
    a = newArtwork(id=artwork["ObjectID"],
    title=artwork["Title"],
    constituent_id=artwork["ConstituentID"],
    date=artwork["Date"],
    medium=artwork["Medium"],
    dimensions=artwork["Dimensions"],
    credit_line=artwork["CreditLine"],
    accession_number=artwork["AccessionNumber"],
    classification=artwork["Classification"],
    department=artwork["Department"],
    date_aquired=artwork["DateAcquired"],
    cataloged=artwork["Cataloged"],
    url=artwork["URL"],
    circumference=artwork["Circumference (cm)"],
    depth=artwork["Depth (cm)"],
    diameter=artwork["Diameter (cm)"],
    height=artwork["Height (cm)"],
    lenght=artwork["Length (cm)"],
    weight=artwork["Weight (kg)"],
    width=artwork["Width (cm)"],
    seat_height=artwork["Seat Height (cm)"],
    duration=artwork["Duration (sec.)"])
    lt.addLast(catalog['artworks'], a)

def addArtist(catalog, artist):
    a = newArtist(id=artist["ConstituentID"],
    name=artist["DisplayName"], 
    biography=artist["ArtistBio"],
    nationality=artist["Nationality"],
    gender=artist["Gender"],
    begin_date=artist["BeginDate"],
    end_date=artist["EndDate"],
    wiki_id=artist["Wiki QID"],
    ulan=artist["ULAN"])

    lt.addLast(catalog['artists'], a)

def cronologicalArtists(catalog, beginDate, endDate):
    catalogArtists= dict(catalog["artists"])
    mergesort.sort(catalogArtists, cmpArtistByDate)
    foundArtists=lt.newList(datastructure='ARRAY_LIST')
    firstAndLast=lt.newList(datastructure='ARRAY_LIST')
  
    for artist in lt.iterator(catalogArtists):
        if artist["begin_date"]>=beginDate and artist["begin_date"]<=endDate:
            if lt.size(firstAndLast)<3:
                lt.addLast(firstAndLast,artist)
            lt.addLast(foundArtists,artist)     
    for n in range(2,-1,-1):
        posicion=lt.size(foundArtists)-n
        elemento=lt.getElement(foundArtists,posicion)
        lt.addLast(firstAndLast,elemento)
    
    return firstAndLast, lt.size(foundArtists)


def cronologicalArtwork(catalog, beginDate, endDate):
    catalogArtwork=dict(catalog["artworks"])
    mergesort.sort(catalogArtwork, cmpArtworkByDateAcquired)
    totalArtwork=0
    foundArtwork=lt.newList('ARRAY_LIST')
    purchased=0

    for artwork in lt.iterator(catalogArtwork):
        if artwork["date_aquired"]=="Unknown":
            continue
        date=textToDate(artwork["date_aquired"])
        if date>=beginDate and date<=endDate:
            lt.addLast(foundArtwork, artwork)
            if "purchase" in artwork["credit_line"].lower():
                purchased+=1
            totalArtwork+=1
    index=lt.size(catalogArtwork)
    while index!=0 and lt.size(foundArtwork)<6:
        date=textToDate(artwork["date_aquired"])
        artwork=lt.getElement(catalogArtwork, index)
        if date>=beginDate and date<=endDate:
            lt.addLast(foundArtwork,artwork)
        index-=1   
    return foundArtwork, totalArtwork, purchased

def textToDate(text):
    if text!="Unknown":
        date=text.split("-")
        date=dt.date(int(date[0]),int(date[1]),int(date[2]))
        return date
    else:
        return dt.date(1,1,1)

def lastArtist(catalog):
    authors = []
    size = lt.size(catalog['artists'])
    for n in range(0, 3):
        authors.append(lt.getElement(catalog['artists'], size - n))
    return authors

def lastArtwork(catalog):
    artworks = []
    size = lt.size(catalog['artworks'])
    for n in range(0, 3):
        artworks.append(lt.getElement(catalog['artworks'], size - n))
    return artworks

def getArtist(catalog, artist_name):
    """
    Retorna la informacion de un artista a partir de
    su nombre, buscandolo linealmente en el catalogo.
    Args:
        catalog: Catalogo para buscar
        artist_name: Nombre del artista
    """
    for artist in lt.iterator(catalog['artists']):
        if artist['name'] == artist_name:
            return artist
    return None

def getMediumsByArtist(catalog:dict, artist:dict)->Tuple[ADTList, ADTList]:
    """
    Retorna un ARRAY_LIST con valores teniendo dos llaves:
    'medium' siendo el nombre de el medio
    'len' siendo la cantidad de obras que pertenecen a este medio

    La lista esta ordenada de mayor a menor basado en la cantidad de obras.

    Tambien retorna otra lista que contiene todas las obras de el medio
    mas popular de el autor.
    Args:
        catalog: Catalogo para buscar
        artist: Informacion del artista
    """
    artist_id = artist['id']
    medium_to_artworks = {}

    for artwork in lt.iterator(catalog['artworks']): 
        ids = artwork['constituent_id'][1:-1].replace(' ', '').split(',')
        if artist_id in ids:
            medium = artwork['medium']
            if medium in medium_to_artworks:
                lt.addLast(medium_to_artworks[medium], artwork)
            else:
                new_list = lt.newList('ARRAY_LIST')
                lt.addLast(new_list, artwork)
                medium_to_artworks[medium] = new_list

    medium_ranking = dictToList(medium_to_artworks, 'medium', 'len', lt.size)

    mergesort.sort(medium_ranking, cmpMediumByLength)

    top_artworks = medium_to_artworks[lt.getElement(medium_ranking, 1)['medium']]

    return top_artworks, medium_ranking

def dictToList(dictionary: dict, key_name: str, value_name: str, mod_func: Callable)->ADTList:
    """
    Devuelve una lista con valores igual a llaves de el diccionario de forma
    key_name: llave, value_name: value
    Esto permite que se organize el diccionario segun llave o segun valor
    Args:
        dictionary: diccionario a convertir
        key_name: llave que se va a usar para acceder a el valor de la llave en los diccionarios.
        value_name: llave que se va a usar para acceder al valo en los diccionarios.
        mod_func: funcion para aplicar a el valor antes de guardarse.
    """
    l = lt.newList(datastructure='ARRAY_LIST')
    for key in dictionary:
        lt.addLast(l, {key_name: key, value_name: mod_func(dictionary[key])})
    return l

def cmpMediumByLength(medium1, medium2)->bool:
    """
    Devuelve verdadero (True) si el valor de la llave 'len' de medium1 es mayor que el de
    medium2
    Args:
        medium1: informacion de el primer medio, siendo nombre y cantidad de obras
        medium2: informacion de el segundo medio, siendo nombre y cantidad de obras
    """
    return medium1['len'] > medium2['len']

def cmpArtworkByDateAcquired(artwork1, artwork2)->bool: 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de 
    artwork2 
    Args: 
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    return textToDate(artwork1["date_aquired"]) < textToDate(artwork2["date_aquired"])

def cmpArtworkByDateAcquiredReversed(artwork1, artwork2)->bool: 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de 
    artwork2 
    Args: 
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    if artwork1["date"]=="Unknown":
        return artwork2["date"]
    if artwork2["date"]=="Unknown":
        return artwork1["date"]
    return int(artwork1["date"]) < int(artwork2["date"])

def cmpArtistByDate(artist1, artist2)->bool: 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de 
    artwork2 
    Args: 
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    return artist1["begin_date"] < artist2["begin_date"]

def cmpArtworkByNationality(artist1, artist2): 
    return artist1["nationality"] < artist2["nationality"] #Menor a mayor

def cmpNationality(natio1,natio2):
    return natio1 < natio2 #Menor a Mayor 

def cmpTotalNationalities(natio1,natio2):
    return natio1["Artworks"]>natio2["Artworks"]  #Mayor a menor 

def sortByNationality(catalog):
    artists=catalog["artists"]
    artworks=catalog["artworks"]
    nationalities_dict={}
    list_of_nationalities=lt.newList(datastructure="ARRAY_LIST")
    artists_dict=createArtistDict(artists)

    for artwork in lt.iterator(artworks):
        code=artwork["constituent_id"] 
        code=code[1:-1].replace(" ","").split(",")
        for artist_id in code:
            nationality=artists_dict[artist_id]["nationality"]
            if nationality=="" or nationality =="Nationality unknown":
                nationality="Unknown"
            if nationality in nationalities_dict:
                nationalities_dict[nationality].append(artwork)
            else:
                nationalities_dict[nationality]=[artwork]
    
    for nationality in nationalities_dict:
        lt.addLast(list_of_nationalities,{"nationality":nationality,"Artworks":len(nationalities_dict[nationality])})
    
    sorted_nationalities=mergesort.sort(list_of_nationalities,cmpTotalNationalities)
    top=lt.getElement(sorted_nationalities,1)["nationality"]
    
    matching_artworks=lt.newList(datastructure="ARRAY_LIST")
    nationality_artwork=nationalities_dict[top]
    artwork_id=None
    for i in nationality_artwork:
        if i["id"]!=artwork_id:
            lt.addLast(matching_artworks,i)
            artwork_id=i["id"]
    
    artwork_count=lt.size(matching_artworks)
    
    joined=lt.newList(datastructure="ARRAY_LIST")
    first=lt.subList(matching_artworks,1,3)
    last=lt.subList(matching_artworks,lt.size(matching_artworks)-3,3)
    for i in lt.iterator(first):
        lt.addLast(joined,i)
    for n in lt.iterator(last):
        lt.addLast(joined,n)

    addArtworkArtists(joined,artists_dict)

    return sorted_nationalities, joined, top, artwork_count

def createArtistDict(artists):
    """
    Crea un diccionario donde la llave es el ID del artista y el valor es otro diccionario con toda la informacion del artista.
    """
    artists_dict={}
    for artist in lt.iterator(artists):
        artist_id=artist["id"]
        artists_dict[artist_id]=artist
    return artists_dict

def addArtworkArtists(artworks,artists_dict):
    """
    Añade al array artworks los nombres de los artistas para cada obra
    """
    for artwork in lt.iterator(artworks):
        names=[]
        if artwork["url"]=="":
            artwork["url"]="Unknown"
        code=artwork["constituent_id"]
        code=code[1:-1].replace(" ","").split(",")
        for artist_id in code:
            names.append(artists_dict[artist_id]["name"])
        artwork["Names"]=names
    
def createArtworkDict(artworks):
    """
    Crea un diccionario donde la llave es el ID de la obra y el valor es otro diccionario con toda la informacion de la obra.
    """
    artwork_dict={}
    for artwork in lt.iterator(artworks):
        artwork_id=artwork["id"]
        artwork_dict[artwork_id]=artwork
    return artwork_dict

def costFromDepartment(catalog, department):

    artwork_id_to_cost = {}
    artwork_id_to_authors = {}
    id_to_artist = createArtistDict(catalog['artists'])
    
    artworks_department = lt.newList('ARRAY_LIST')

    for artwork in lt.iterator(catalog['artworks']):
        if department == artwork['department']:
            lt.addLast(artworks_department, artwork)

    for artwork in lt.iterator(artworks_department):
        authors = []
        author_ids = stringArrayToArray(artwork['constituent_id'])
        for id in author_ids:
            authors.append(id_to_artist[id])
        artwork_id_to_authors[artwork["id"]] = authors
        artwork_id_to_cost[artwork["id"]] = getTransportationCost(artwork)
    
    organized_cost_list = dictToList(artwork_id_to_cost, 'artwork', 'cost', lambda x: x)

    mergesort.sort(organized_cost_list, cmpCost)
    mergesort.sort(artworks_department, cmpArtworkByDateAcquiredReversed)

    return organized_cost_list, artworks_department, artwork_id_to_authors, artwork_id_to_cost

def cmpCost(value1, value2):
    return value1['cost'] > value2['cost']

def stringArrayToArray(string):
    return string[1:-1].replace(' ', '').split(',')

def getTransportationCost(artwork):
    cost = 42
    artworks = ['width', 'height', 'lenght', 'depth']
    weight = artwork['weight']
    width = 0
    height = 0
    lenght = 0
    radius = 0
    dimensions = 0
    total = 0
    unit1 = ""
    unit2 = ""

    for unit in artworks:
        value = artwork[unit]
        if value != "0" and value !="Unknown":
            unit1 = unit
            width = float(value)
    if width != 0:
        dimensions += 1
    for unit in artworks:
        value = artwork[unit]
        if value != "0" and value !="Unknown" and unit != unit1:
            unit2 = unit
            height = float(value)
    if height != 0:
        dimensions += 1
    for unit in artworks:
        value = artwork[unit]
        if value != "0" and value !="Unknown" and unit not in (unit1, unit2):
            lenght = float(value)
            break
    if lenght != 0:
        dimensions += 1
    
    if artwork['circumference'] != "0" and artwork['circumference']!="Unknown":
        radius = float(artwork['circumference'])/2*pi
    elif artwork['diameter'] != "0" and artwork['diameter']!="Unknown":
        radius = float(artwork['diameter'])/2
    
    if radius != 0:
        dimensions += 2
    
    if dimensions == 2 or dimensions ==3:
        if bool(radius):
            total = pi * radius**2
            total/=10000
            if width != 0:
                total *= width
                total/=100
        else:
            total = width * height
            total/=10000
            if lenght != 0:
                total *= lenght
                total/=100
    
    if weight != "0" and weight!="Unknown":
        if total!=0 and total > float(weight):
            cost = total * 72
        else:
            cost = float(weight) *72
    elif total!=0:
        cost = total * 72
    

    return cost
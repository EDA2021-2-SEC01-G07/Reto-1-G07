"""
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


from DISClib.DataStructures.arraylist import iterator
import config as cf
from DISClib.ADT import list as lt
import datetime as dt
import time
from DISClib.Algorithms.Sorting import insertionsort, shellsort, mergesort, quicksort

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

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

def sortArtworks(catalog):
    return mergesort.sort(catalog,cmpArtworkByDateAcquired)

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de 
    artwork2 
    Args: 
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    return textToDate(artwork1["date_aquired"]) < textToDate(artwork2["date_aquired"])

def sortArtist(catalog):
    return mergesort.sort(catalog,cmpArtistByDate)

def cmpArtistByDate(artist1, artist2): 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de 
    artwork2 
    Args: 
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    return artist1["begin_date"] < artist2["begin_date"]


def textToDate(text):
    if text!="":
        date=text.split("-")
        date=dt.date(int(date[0]),int(date[1]),int(date[2]))
        return date
    else:
        return dt.date(1,1,1)

def cmpArtworkByNationality(artist1, artist2): 
    return artist1["nationality"] < artist2["nationality"] #Menor a mayor

def cmpNationality(natio1,natio2):
    return natio1 < natio2 #Menor a Mayor 

def cmpTotalNationalities(natio1,natio2):
    return natio1["Artworks"]>natio2["Artworks"]  #Mayor a menor 

def sortByNationality(catalog):
    artists=catalog["artists"]
    artworks=catalog["artworks"]
    nationality_list=lt.newList(datastructure="ARRAY_LIST")

    artits_dict={}#La llave es el ID del artista, el valor es otro diccionario con toda la informacion del artista.
    nationalities_dict={}
    list_of_nationalities=lt.newList(datastructure="ARRAY_LIST")
    for artist in lt.iterator(artists):
        artist_id=artist["id"]
        nationality=artist["nationality"]
        artits_dict[artist_id]=artist
    
    for artwork in lt.iterator(artworks):
        code=artwork["constituent_id"] 
        code=code[1:len(code)-1].replace(" ","").split(",")
        for artist_id in code:
            nationality=artits_dict[artist_id]["nationality"]
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
    
    for artwork in lt.iterator(joined):
        names=[]
        if artwork["url"]=="":
            artwork["url"]="Unknown"
        code=artwork["constituent_id"]
        code=code[1:len(code)-1].replace(" ","").split(",")
        for artist_id in code:
            names.append(artits_dict[artist_id]["name"])
        artwork["Names"]=names
    
    return sorted_nationalities, joined, top, artwork_count
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

    for ids in lt.iterator(artworks):
        code=ids["constituent_id"]
        mod=code.replace("[","").replace("]","").replace(" ","").split(",")
        getNationalities(artists,mod,nationality_list)
    
    countedNationalities=countNationalities(nationality_list) #Array con todas las nacionalidades y cuantas obras de arte expusieron
    # print(countedNationalities)   
    top=lt.getElement(countedNationalities,1)["Nationality"]
    codes=searchCodes(artists, artworks, top) #Array en donde cada elemento contiene codigo de la obra y sus artistas Si hay almenos uno que sea de la nacionalidad mas repetida.    
    # print(codes)
    
    
    
    # artwork_info=lt.newList(datastructure="ARRAY_LIST")
    first=lt.subList(codes,1,3)
    last=lt.subList(codes,lt.size(codes)-3,3)
    # searchInfo(first,last,artists, artworks)

    # print(first)
    # print(last)
    # top_pais=lt.newList(datastructure="ARRAY_LIST")
    # for artwork in lt.iterator(artwork):
    #     if artwork["nationality"]==top:
    #         lt.addLast(top_pais, artwork)
    # first=lt.subList(top_pais,1,3)
    # last=lt.subList(top_pais,lt.size-3,3)
    # print(top)
    return countedNationalities

def getNationalities(artists, code, nationality_list):
    """
        Recibe el catalago de artistas, la lista con los codigos de los artistas para una obra
        Añade al array nationality_list la nacionalidad de los artistas que crearon la obra.
    """
    for artist_id in code:
        for n in lt.iterator(artists):
            nationality=n["nationality"]
            current_id=n["id"]
            if nationality=="" or nationality =="Nationality unknown":
                nationality="Unknown"
            if artist_id==current_id:                
                lt.addLast(nationality_list,nationality)
    pass

def countNationalities(nationality_list):
    """
    Cuenta cuantas veces aparece cada nacionalidad en el array nationality_list
    Retorna un array con cada nacionalidad y cuantas obras de arte tiene. 
    """
    countedNationalities=lt.newList(datastructure="ARRAY_LIST")
    sortedNationalities=mergesort.sort(nationality_list,cmpNationality)
    anterior=lt.getElement(sortedNationalities,1)
    contador=0
    for nationality in lt.iterator(sortedNationalities):
        if nationality==anterior:
            contador+=1
        elif nationality!=anterior:
            nationalities={"Nationality":None,"Artworks":None}
            nationalities["Nationality"]=anterior
            nationalities["Artworks"]=contador
            lt.addLast(countedNationalities,nationalities)
            contador=1
            anterior=nationality
        
    countedNationalities=mergesort.sort(countedNationalities,cmpTotalNationalities)
    return countedNationalities

def searchCodes(artists, artworks, top):
    """
    Busca cada codigo, si encuentra que un artista es de la nacionalidad con mas obras de arte.
    Añade al array artWorkCodes el codigo de la obra junto con los codigos de todos los artistas que participaron.
    """
    artWorkCodes=lt.newList(datastructure="ARRAY_LIST")
    for ids in lt.iterator(artworks):
        # pos=lt.isPresent(artworks,ids)
        print(ids)
        code=ids["constituent_id"]
        artwork_id=ids["id"]
        code=code.replace("[","").replace("]","").replace(" ","").split(",")
        for artist_id in code: 
            for n in lt.iterator(artists):
                nationality=n["nationality"]
                current_id=n["id"] 
                if artist_id == current_id and top==nationality:
                    artwork={"ID":artwork_id,"Artists":code}
                    lt.addLast(artWorkCodes,artwork)
    return artWorkCodes

def searchInfo(first,last,artists,artworks):
    info=lt.newList(datastructure="ARRAY_LIST")
    
    for codes in lt.iterator(first):
        element={
            "ObjectID":None,
            "Title": None,
            "ArtistsNames":None,
            "Medium":None,
            "Date":None,
            "Dimensions":None,
            "Department":None,
            "Classification":None,
            "URL":None
            }
        work_id=codes["ID"]
        artists=codes["Artists"]
        # pos=lt.isPresent(artworks,work_id)
        # print(pos)
        
    pass


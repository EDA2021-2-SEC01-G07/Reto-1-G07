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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
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
    artwork = {id: id,
    title: title,
    constituent_id: constituent_id,
    date: date,
    medium: medium,
    dimensions: dimensions,
    credit_line: credit_line,
    accession_number: accession_number,
    classification: classification,
    department: department,
    date_aquired: date_aquired,
    cataloged: cataloged,
    url: url,
    circumference: circumference,
    depth: depth,
    diameter: diameter,
    height: height,
    lenght: lenght,
    weight: weight,
    width: width,
    seat_height: seat_height,
    duration: duration
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
    for n in range(1, 4):
        authors.append(lt.getElement(catalog['artists'], size - n))
    return authors
    
def lastArtwork(catalog):
    artworks = []
    size = lt.size(catalog['artworks'])
    for n in range(1, 4):
        artworks.append(lt.getElement(catalog['artworks'], size - n))
    return artworks
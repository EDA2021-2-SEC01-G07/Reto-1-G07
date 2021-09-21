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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadArtWork(catalog)
    
def loadArtist(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    artistfiles = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistfiles, encoding='utf-8'))
    for authors in input_file:
        model.addArtist(catalog, authors)


def loadArtWork(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    artfiles = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artfiles, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def lastArtist(catalog):
    """
    Muestra los ultimos 3 artistas
    """
    lista=model.lastArtist(catalog)
    ultimos=""
    for i in lista:
        ultimos += str(i["name"]) + "\n"
    return ultimos

def lastArtwork(catalog):
    """
    Muestra las ultimas 3 obras
    """
    lista= model.lastArtwork(catalog)
    ultimos=""
    for i in lista:
        ultimos += str(i["title"]) + "\n"
    return ultimos

def getArtist(catalog, artist_name):
    return model.getArtist(catalog, artist_name)
        
def cronologicalArtists(catalog, beginDate, endDate):
    catalogArtists= catalog["artists"]
    sortedArtists=model.sortArtist(catalogArtists)
    foundArtists=lt.newList(datastructure='ARRAY_LIST')
    firstAndLast=lt.newList(datastructure='ARRAY_LIST')
  
    for artist in lt.iterator(sortedArtists):
        if artist["begin_date"]>=beginDate and artist["begin_date"]<=endDate:
            if lt.size(firstAndLast)<3:
                lt.addLast(firstAndLast,artist)
            lt.addLast(foundArtists,artist)     
    for n in range(2,-1,-1):
        posicion=lt.size(foundArtists)-n
        elemento=lt.getElement(foundArtists,posicion)
        lt.addLast(firstAndLast,elemento)
    
    return firstAndLast,lt.size(foundArtists)


def cronologicalArtwork(catalog, beginDate, endDate):
    catalogArtwork=catalog["artworks"]
    sortedArtworks=model.sortArtworks(catalogArtwork)
    totalArtwork=0
    foundArtwork=lt.newList()
    purchased=0


    for position in range(1, lt.size(sortedArtworks)):
        artwork=lt.getElement(sortedArtworks, position)
        if artwork["date_aquired"]=="":
            continue
        date=model.textToDate(artwork["date_aquired"])
        if date>=beginDate and date<=endDate:
            lt.addLast(foundArtwork, artwork)
            if artwork["credit_line"].lower().startswith("purchase"):
                purchased+=1
            totalArtwork+=1    
    index=lt.size(sortedArtworks)
    while index!=0 and lt.size(foundArtwork)<6:
        date=model.textToDate(artwork["date_aquired"])
        artwork=lt.getElement(sortedArtworks, index)
        if date>=beginDate and date<=endDate:
            lt.addLast(foundArtwork,artwork)
        
        index-=1   
    return (foundArtwork, totalArtwork, purchased)

def sortByNationality(catalog):
    return model.sortByNationality(catalog)
    
def techniquesFromArtist(catalog, artist):
    return model.getMediumsByArtist(catalog, artist)

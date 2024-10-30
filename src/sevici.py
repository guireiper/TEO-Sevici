import csv
from math import sqrt
import os
import webbrowser
import folium
from collections import namedtuple

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')

def lee_estaciones(fichero):
    res=[]

    with open(fichero, encoding='UTF-8') as f:
        lista = csv.reader(f)
        next(lista)

        for nombre, bornetas, bornetas_vacias, bicis_disponibles, latitud, longitud in lista:

            bornetas = int(bornetas)
            bornetas_vacias = int(bornetas_vacias)
            bicis_disponibles = int(bicis_disponibles)
            coordenadas = Coordenadas(float(latitud), float(longitud))
            tupla = Estacion(nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas)
            res.append(tupla)
    
        return res


def estaciones_bicis_libres(estaciones, k=5):
    res = []

    for linea in estaciones:
        if  linea.bicis_disponibles >= k:
            tupla = (linea.bicis_disponibles, linea.nombre)
            res.append(tupla)
    
    return res

def calcula_distancia(coordenadas1, coordenadas2):
    
    x1 = coordenadas1.latitud
    y1 = coordenadas1.longitud

    x2 = coordenadas2.latitud
    y2 = coordenadas2.longitud

    distancia = sqrt((x2-x1)**2 + (y2-y1)**2)

    return distancia


def estaciones_cercanas(estaciones, coordenadas, k=5):
    res = []
    listadist = []

    for linea in estaciones:

        distancia= calcula_distancia(coordenadas, linea.coordenadas)
        tupla = (distancia, linea.nombre,linea.bicis_disponibles)
        listadist.append(tupla)
    
    listadist = sorted(listadist)

    for linea in listadist[:5]:
        res.append(linea)

    return res

def crea_mapa(latitud, longitud, zoom=9):

    mapa = folium.Map(location=[latitud, longitud], zoom_start=zoom)

    return mapa

def crea_marcador (latitud, longitud, etiqueta, color):

    marcador = folium.Marker([latitud,longitud], popup=etiqueta, icon=folium.Icon(color=color, icon='info-sign')) 
    
    return marcador



def media_coordenadas (estaciones):
    latitudes = 0
    logitudes = 0

    for linea in estaciones:


        latitudes = latitudes + linea.coordenadas.latitud
        logitudes = logitudes + linea.coordenadas.longitud

    latitud = latitudes/len(estaciones)
    longitud = logitudes/len(estaciones)

    tupla = Coordenadas(latitud,longitud)

    return tupla


def crea_mapa_estaciones(estaciones,funcion_color):
    #Calculamos la media de las coordenadas de las estaciones, para poder centrar el 
    #mapa
    centro_mapa = media_coordenadas(estaciones)
    # creamos el mapa con folium
    mapa = crea_mapa(centro_mapa.latitud, centro_mapa.longitud, 13)

    for estacion in estaciones:
        etiqueta = estacion.nombre
        color = funcion_color(estacion)
        marcador = crea_marcador(estacion.coordenadas.latitud, estacion.coordenadas.longitud, etiqueta, color)
        marcador.add_to(mapa)
    
    return mapa

def guarda_mapa(mapa, ruta_fichero):
    
    mapa.save(ruta_fichero)
    # Abre el fichero creado en un navegador web
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))

def color_azul(estacion):


    return "blue"

def obten_color_bicis_disponibles(estacion):
    '''Función que devuelve "red" si la estación no tiene bicis disponibles, y verde en caso contrario 
    ENTRADA
      :param estacion: Estacion para la que quiero averiguar el color
      :type estacion: Estacion(str, int, int, int, Coordenadas(float, float))
    SALIDA
      :return: "red" o "green" dependiendo de si la estación tiene bicis disponibles o no
      :rtype: str
    '''
    res="red"
    if estacion.bicis_disponibles>0:
        res="green"
    return res
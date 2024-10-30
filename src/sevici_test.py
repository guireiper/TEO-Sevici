from sevici import *
from coordenadas import *

def test_lee_estaciones(fichero):

    lista = lee_estaciones(fichero)

    print('Las tres primeras son :')
    for linea in lista[:3]:
        print(linea)
    
    print('Las tres últimas son :')
    for linea in lista[-3:]:
        print(linea)


def test_estaciones_bicis_libres(fichero):

    estaciones = lee_estaciones(fichero)
    k= 5
    lista_final = estaciones_bicis_libres(estaciones,k)
    print(f'Hay {len(lista_final)} con {k} o más bicis libres y las 5 primeras son:')
    for linea in lista_final[:5]:
        print(linea)

    k= 10
    lista_final = estaciones_bicis_libres(estaciones,k)
    print(f'Hay {len(lista_final)} con {k} o más bicis libres y las 5 primeras son:')
    for linea in lista_final[:5]:
        print(linea)
    
    k= 1
    lista_final = estaciones_bicis_libres(estaciones,k)
    print(f'Hay {len(lista_final)} con {k} o más bicis libres y las 5 primeras son:')
    for linea in lista_final[:5]:
        print(linea)

def test_estaciones_cercanas(fichero):
    estaciones = lee_estaciones(fichero)

    k = 5
    coordenadas = Coordenadas(37.357659, -5.9863)
    lista_final = estaciones_cercanas(estaciones,coordenadas, k)

    print(f'Las {k} estaciones más cercanas al punto {Coordenadas[0]}, {Coordenadas[1]} son:')
    for linea in lista_final:
        print(linea)

def test_crear_mapa_azul(fichero):
    estaciones = lee_estaciones(fichero)

    mapa = crea_mapa_estaciones(estaciones,color_azul)

    guarda_mapa(mapa,"./out/azul.html")

def test_crear_mapa(fichero):
    estaciones = lee_estaciones(fichero)

    mapa = crea_mapa_estaciones(estaciones,obten_color_bicis_disponibles)

    guarda_mapa(mapa, "./out/estaciones_bicis_disponibles.html")

    



if __name__ == "__main__":
    #test_lee_estaciones('data\estaciones.csv')

    #test_estaciones_bicis_libres('data\estaciones.csv')

    #test_estaciones_cercanas('data\estaciones.csv')

    #test_crear_mapa_azul('data\estaciones.csv')

    test_crear_mapa('data\estaciones.csv')



    
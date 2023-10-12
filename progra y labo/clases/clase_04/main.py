from data import lista_bzrp
'''
[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Mostrar lista
8 - Salir
'''

def calcular_tema_mas_visto():
    for indice in range(len(lista_bzrp)):
        if indice == 0 or maximo_views < lista_bzrp[indice]["views"]:
            maximo_views = lista_bzrp[indice]["views"]
            maximo_indice = indice

    print(f"\nTema mas visto: \nTitulo: {lista_bzrp[maximo_indice]['title']} - Views: {lista_bzrp[maximo_indice]['views']} - Length: {lista_bzrp[maximo_indice]['length']}")

def calcular_tema_menos_visto():

    for indice in range(len(lista_bzrp)):
        if indice == 0 or minimo_views > lista_bzrp[indice]["views"]:
            minimo_views = lista_bzrp[indice]["views"]
            minimo_indice = indice

    print(f"\nTema menos visto: \nTitulo: {lista_bzrp[minimo_indice]['title']} - Views: {lista_bzrp[minimo_indice]['views']} - Length: {lista_bzrp[minimo_indice]['length']}")

def calcular_tema_mas_largo():
    for indice in range(len(lista_bzrp)):
        if indice == 0 or maximo_length < lista_bzrp[indice]["length"]:
            maximo_length = lista_bzrp[indice]["length"]
            maximo_indice = indice

    print(f"\nTema mas largo: \nTitulo: {lista_bzrp[maximo_indice]['title']} - Views: {lista_bzrp[maximo_indice]['views']} - Length: {lista_bzrp[maximo_indice]['length']}")

def calcular_tema_mas_corto():
    for indice in range(len(lista_bzrp)):
        if indice == 0 or minimo_length > lista_bzrp[indice]["length"]:
            minimo_length = lista_bzrp[indice]["length"]
            minimo_indice = indice

    print(f"\nTema mas corto: \nTitulo: {lista_bzrp[minimo_indice]['title']} - Views: {lista_bzrp[minimo_indice]['views']} - Length: {lista_bzrp[minimo_indice]['length']}")

def calcular_promedio_duracion():
    acumulador_duracion = 0
    for video in lista_bzrp:
        acumulador_duracion += video['length']
    duracion_promedio = acumulador_duracion/len(lista_bzrp)
    print(f"\nLa duracion promedio es de {duracion_promedio:.2f} segundos")

def calcular_promedio_vistas():
    acumulador_vistas = 0
    for video in lista_bzrp:
        acumulador_vistas += video['views']
    vistas_promedio = acumulador_vistas/len(lista_bzrp)
    print(f"\nLa vistas promedio son de {vistas_promedio:.2f} millones")

def mostrar_lista_videos():
    
    for video in lista_bzrp:
        print(f"\nTitulo: {video['title']} - Views: {video['views']} - Length: {video['length']}")

while True:
    print("\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas\n7 - Mostrar lista\n8 - Salir")
    respuesta_str = input("\nSeleccione una opcion: ")
    respuesta_int = int(respuesta_str)

    match respuesta_int:
        case 1:
            calcular_tema_mas_visto()
        case 2:
            calcular_tema_menos_visto()
            pass
        case 3:
            calcular_tema_mas_largo()
            pass
        case 4:
            calcular_tema_mas_corto()
            pass
        case 5:
            calcular_promedio_duracion()
            pass
        case 6:
            calcular_promedio_vistas()
            pass
        case 7:
            mostrar_lista_videos()
        case 8:
            print("\nCerrando programa.")
            break
        case _:
            print("\nLa opcion no es valida")

    input("\nPulse enter para continuar")
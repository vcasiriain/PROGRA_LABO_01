from data_stark import lista_personajes

"""A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M"""
"""B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"""
"""C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"""
"""D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"""
"""E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M"""
"""F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F"""
"""G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M"""
"""H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F"""
"""I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)"""
"""J. Determinar cuántos superhéroes tienen cada tipo de color de ojos."""
"""K. Determinar cuántos superhéroes tienen cada tipo de color de pelo."""
"""L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)."""
"""M. Listar todos los superhéroes agrupados por color de ojos."""
"""N. Listar todos los superhéroes agrupados por color de pelo."""
"""O. Listar todos los superhéroes agrupados por tipo de inteligencia"""

def mostrar_lista_heroes(lista_heroes):
    """
    Recibe e imprime una lista de heroes
    """
    for heroe in lista_heroes:
        print(heroe)

def mostrar_heroes_por_genero(lista_heroes,genero):
    """
    Recibe una lista de heroe y su genero
    Imprime nombre de heroe por genero
    """
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            print(heroe["nombre"])

def encontrar_heroe_mas_alto(lista_heroes,genero):
    """
    Recibe una lista de heroes y su genero
    Encuentra al heroe mas alto
    Devuelve el nombre del heroe mas alto
    """
    altura_maxima = 0
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            altura = float(heroe["altura"])
            if altura > altura_maxima:
                altura_maxima = altura
                nombre_heroe = heroe["nombre"]       
    return nombre_heroe

def encontrar_heroe_mas_bajo(lista_heroes,genero):
    """
    Recibe una lista de heroes y su genero
    Encuentra al heroe mas bajo
    Devuelve el nombre del heroe mas bajo
    """
    altura_minima = None
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            altura = float(heroe["altura"])
            if altura_minima == None or altura < altura_minima:
                altura_minima = altura
                nombre_heroe = heroe["nombre"]
    return nombre_heroe

def promedio_altura_heroe(lista_heroes,genero):
    """
    Recibe una lista de heroes y su genero
    Calcula el promedio de altura por genero
    Retorna valor del promedio de altura por genero
    """
    suma_altura = 0
    contador_heroes_por_genero = 0
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            suma_altura += float(heroe["altura"])
            contador_heroes_por_genero += 1
            
    promedio = suma_altura/contador_heroes_por_genero

    return promedio

def mostrar_cantidad_de_heroes_por_clave(lista_heroes,clave):
    """
    Recibe una lista de heroes y una clave
    Agrupa en un diccionario los valores de las claves y calcula la cantidad por clave
    Imprime la clave y la cantidad del diccionario
    """
    dict_claves = {}
    for heroe in lista_heroes:
        valor_clave = heroe.get(clave)
        if valor_clave == "" or valor_clave == "No Hair":
            valor_clave = "No tiene"
        if valor_clave in dict_claves:
            dict_claves[valor_clave] += 1
        else:
            dict_claves[valor_clave] = 1
    for clave,cantidad in dict_claves.items():
        print(f"{clave}: {cantidad}")

def mostrar_nombre_de_heroes_por_clave(lista_heroes,clave):
    """
    Recibe una lista de heroes y una clave
    Agrupa en un diccionario los valores de las claves junto al nombre del heroe
    Imprime los nombres de los heroes agrupados por clave
    """
    dict_claves = {}
    for heroe in lista_heroes:
        valor_clave = heroe.get(clave)
        if valor_clave == "" or valor_clave == "No Hair":
            valor_clave = "No tiene"
        if valor_clave in dict_claves:
            dict_claves[valor_clave].append(heroe["nombre"])
        else:
            dict_claves[valor_clave] = [heroe["nombre"]]
    for clave,cantidad in dict_claves.items():
        print(f"{clave}: {cantidad}")

def mostrar_menu(lista_heroes: list[dict]):

    while True:
        print("\nMenú:")
        print("1. Mostrar los nombres de cada superheroe de genero M")
        print("2. Mostrar los nombres de cada superheroe de genero F")
        print("3. Mostrar al superheroe mas alto de genero M")
        print("4. Mostrar al superheroe mas alto de genero F")        
        print("5. Mostrar al superheroe mas bajo de genero M")
        print("6. Mostrar al superheroe mas bajo de genero F")
        print("7. Mostrar la altura promedio de los superheroes de genero M")        
        print("8. Mostrar la altura promedio de los superheroes de genero F")
        print("9. Mostrar cantidad de superheroes por color de ojos")        
        print("10. Mostrar cantidad de superheroes por color de pelo")
        print("11. Mostrar cantidad de superheroes por inteligencia")
        print("12. Mostrar superheroes por color de ojos")
        print("13. Mostrar superheroes por color de pelo")
        print("14. Mostrar superheroes por inteligencia")        
        print("15. Mostrar lista de heroes")

        opcion = input("\nIngrese el número de la opción que desea ejecutar: ")

        match opcion:
            case "1":
                print("\nLos nombres de los heroes son: ")
                mostrar_heroes_por_genero(lista_personajes,genero='M')
            case "2":
                print("\nLos nombre de las heroinas son: ")
                mostrar_heroes_por_genero(lista_personajes,genero='F')
            case "3":
                nombre_heroe = encontrar_heroe_mas_alto(lista_personajes,genero='M')
                print(f"\nEl heroe mas alto es: {nombre_heroe}")
            case "4":
                nombre_heroe = encontrar_heroe_mas_alto(lista_personajes,genero='F')
                print(f"\nLa heroina mas alta es: {nombre_heroe}")
            case "5":
                nombre_heroe = encontrar_heroe_mas_bajo(lista_personajes,genero='M')
                print(f"\nEl heroe mas bajo es: {nombre_heroe}")
            case "6":
                nombre_heroe = encontrar_heroe_mas_bajo(lista_personajes,genero='F')
                print(f"\nLa heroina mas baja es: {nombre_heroe}")
            case "7":
                promedio = promedio_altura_heroe(lista_personajes,genero='M')
                print(f"\nLa altura promedio de los heroes es: {promedio}")
            case "8":
                promedio = promedio_altura_heroe(lista_personajes,genero='F')
                print(f"\nLa altura promedio de las heroinas es: {promedio}")
            case "9":
                print("\nLa cantidad de heroes por color de ojos es: ")
                mostrar_cantidad_de_heroes_por_clave(lista_personajes,clave="color_ojos")
            case "10":
                print("\nLa cantidad de heroes por color de pelo es: ")
                mostrar_cantidad_de_heroes_por_clave(lista_personajes,clave="color_pelo")
            case "11":
                print("\nLa cantidad de heroes por inteligencia es: ")
                mostrar_cantidad_de_heroes_por_clave(lista_personajes,clave="inteligencia")
            case "12":
                print("\nNombres de heroes por color de ojos: ")
                mostrar_nombre_de_heroes_por_clave(lista_personajes,clave="color_ojos")
            case "13":
                print("\nNombres de heroes por color de pelo: ")
                mostrar_nombre_de_heroes_por_clave(lista_personajes,clave="color_pelo")
            case "14":
                print("\nNombres de heroes por inteligencia: ")
                mostrar_nombre_de_heroes_por_clave(lista_personajes,clave="inteligencia")
            case "15":
                mostrar_lista_heroes(lista_personajes)
            case "0":
                print("\nCerrando el programa")
                break
            case _:
                print("\nError. Ingrese el número de la opción que desea ejecutar: ")

        input("\nPulse enter para continuar")
    

mostrar_menu(lista_personajes)
from data_stark import lista_personajes

def obtener_nombre(heroe: dict) -> str:
	"""
    Obtiene el valor de la clave "nombre" del heroe
    Recibe un diccionario que representa a un heroe
    Retorna el nombre del heroe
    """
	nombre = heroe.get("nombre")
	return nombre

def obtener_identidad(heroe: dict) -> str:
	"""
    Obtiene el valor de la clave "identidad" del heroe
    Recibe un diccionario que representa a un heroe
    Retorna la identidad del heroe
    """
	identidad = heroe.get("identidad")
	return identidad

def obtener_altura(heroe: dict) -> float:
    """
    Obtiene el valor de la clave "altura" del heroe
    Recibe un diccionario que representa a un heroe
    Retorna la altura del heroe
    """
    altura = heroe.get("altura")
    return altura

def obtener_peso(heroe: dict) -> float:
    """
    Obtiene el valor de la clave "peso" del heroe
    Recibe un diccionario que representa a un heroe
    Retorna el peso del heroe
    """
    peso = heroe.get("peso")
    return peso

"""
B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
"""

def imprimir_nombres_de_heroes(lista_heroes: list[dict]):
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        print(nombre)
"""
C- Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
"""
def imprimir_nombre_altura_de_heroes(lista_heroes: list[dict]):
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        altura = obtener_altura(heroe)
        print(f"Nombre: {nombre} | Altura: {altura}")
"""
D- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
"""
def determina_heroe_mas_alto(lista_heroes: list[dict]):
    heroe_mas_alto = None
    
    for heroe in lista_heroes:
        if heroe_mas_alto == None or float(heroe_mas_alto["altura"]) < float(obtener_altura(heroe)):
            heroe_mas_alto = heroe
    print("El heroe mas alto es {0}".format(obtener_nombre(heroe_mas_alto)))
    return heroe_mas_alto
"""
E- Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
"""
def determina_heroe_mas_bajo(lista_heroes: list[dict]):
    heroe_mas_bajo = None
    
    for heroe in lista_heroes:
        if heroe_mas_bajo == None or float(heroe_mas_bajo["altura"]) > float(obtener_altura(heroe)):
            heroe_mas_bajo = heroe
    print("El heroe mas bajo es {0}".format(obtener_nombre(heroe_mas_bajo)))
    return heroe_mas_bajo
"""
F- Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
"""
def calcular_altura_promedio(lista_heroes: list[dict]):
    suma_alturas = 0

    for heroe in lista_heroes:
        altura = obtener_altura(heroe)
        suma_alturas += altura

    altura_promedio = suma_alturas/len(lista_heroes)

    print(f"La altura promedio de los heroes es: {altura_promedio}")
    return altura_promedio
"""
G- Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
"""
def determina_identidad_mas_alto(lista_heroes: list[dict]):
    heroe_mas_alto = None
    
    for heroe in lista_heroes:
        if heroe_mas_alto == None or float(heroe_mas_alto["altura"]) < float(obtener_altura(heroe)):
            heroe_mas_alto = heroe
    print(f"La identidad del heroe mas alto es {obtener_identidad(heroe_mas_alto)}")

def determina_identidad_mas_bajo(lista_heroes: list[dict]):
    heroe_mas_bajo = None
    
    for heroe in lista_heroes:
        if heroe_mas_bajo == None or float(heroe_mas_bajo["altura"]) > float(obtener_altura(heroe)):
            heroe_mas_bajo = heroe
    print(f"La identidad del heroe mas bajo es {obtener_identidad(heroe_mas_bajo)}")

"""
H- Calcular e informar cual es el superhéroe más y menos pesado.
"""
def determina_heroe_mas_pesado(lista_heroes: list[dict]):
    heroe_mas_pesado = None
    
    for heroe in lista_heroes:
        if heroe_mas_pesado == None or float(heroe_mas_pesado["peso"]) > float(obtener_peso(heroe)):
            heroe_mas_pesado = heroe
    mensaje = "El heroe mas pesado es {0}".format(obtener_nombre(heroe_mas_pesado))
    print(mensaje)
    return heroe_mas_pesado

def determina_heroe_menos_pesado(lista_heroes: list[dict]):
    heroe_menos_pesado = None
    
    for heroe in lista_heroes:
        if heroe_menos_pesado == None or float(heroe_menos_pesado["peso"]) < float(obtener_altura(heroe)):
            heroe_menos_pesado = heroe
    mensaje = "El heroe menos pesado es {0}".format(obtener_nombre(heroe_menos_pesado))
    print(mensaje)
    return heroe_menos_pesado
"""
I- Ordenar el código implementando una función para cada uno de los valores informados.
"""
"""
J- Construir un menú que permita elegir qué dato obtener
"""
def mostrar_menu(lista_heroes: list[dict]):

    while True:
        print("\nMenú:")
        print("1. Mostrar los nombres de cada superheroe")
        print("2. Mostrar los nombres de cada superheroe junto a su altura")
        print("3. Mostrar al superheroe mas alto")
        print("4. Mostrar al superheroe mas bajo")
        print("5. Mostrar la identidad del superheroe mas alto y mas bajo")
        print("6. Mostrar el superheroe mas pesado y el menos pesado")
        print("0. Salir")

        opcion = input("\nIngrese el número de la opción que desea ejecutar: ")

        match opcion:
            case "1":
                imprimir_nombres_de_heroes(lista_heroes)
            case "2":
                imprimir_nombre_altura_de_heroes(lista_heroes)
            case "3":
                determina_heroe_mas_alto(lista_heroes)           
            case "4":
                determina_heroe_mas_bajo(lista_heroes)    
            case "5":
                determina_identidad_mas_alto(lista_heroes)
                determina_identidad_mas_bajo(lista_heroes)
            case "6":
                determina_heroe_mas_pesado(lista_heroes)
                determina_heroe_menos_pesado(lista_heroes)
            case "0":
                print("\nCerrando el programa")
                break
            case _:
                print("\nLa opcion no es valida")

        input("\nPulse enter para continuar")
    

mostrar_menu(lista_personajes)
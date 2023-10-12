from biblioteca_02_stark import (
    imprimir_nombres_de_heroes, imprimir_nombre_altura_de_heroes, determina_heroe_mas_alto, determina_heroe_mas_bajo, determina_identidad_mas_alto, determina_identidad_mas_bajo, determina_heroe_mas_pesado, determina_heroe_menos_pesado, mostrar_menu
)

"""
J- Construir un menú que permita elegir qué dato obtener
"""
def main_app(lista_heroes):
    """
    Ejecuta todo nuestro programa
    Recibe la lista de heroes
    """
    while True:
        opcion = mostrar_menu()
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

        input("\nPulse enter para continuar ")
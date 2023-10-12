"""
1- Crear una función que convierta grados Celsius a grados Fahrenheit. 
Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
"""
        
# def convierte_celsius_a_fahrenheit(grados_celsius):
#     """
#     Recibe: valor de grados en celsius\n
#     Realiza calculo de conversion\n
#     Retorna: valor de grado ingresado en fahrenheit
#     """
#     grados_fahrenheit = (grados_celsius * 9 / 5) + 32
#     return grados_fahrenheit

# grados_celsius = int(input("Ingrese un valor de grados celsius: "))

# grados_fahrenheit = convierte_celsius_a_fahrenheit(grados_celsius)

# print(f"{grados_celsius} grados Celsius equivale a {grados_fahrenheit} grados Fahrenheit.")

"""
2- Crear una función que calcule el área de un círculo. 
Recibe un parámetro (radio) y devuelve el área del círculo.
"""
# import math

# def calcular_area_circulo(radio):
#     """
#     Recibe: valor de radio de un circulo\n
#     Reliza calculo del area\n
#     Retorna: valor del area del circulo
#     """
#     area = math.pi * radio**2
#     return area

# radio = int(input("Ingrese el radio de un circulo: "))

# area_del_circulo = calcular_area_circulo(radio)

# print(f"El area de un circulo de {radio}cm de radio es: {area_del_circulo:.2f} centimetros cuadrados")

"""
3- Crear una función que calcule el descuento aplicado a un producto. 
Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.
"""

# def calcular_porcentaje_descuento(precio_original, precio_con_descuento):
#     """
#     Recibe: precio original y precio con descuento
#     Calcula el porcentaje del descuento sobre el original
#     Retorna: porcentaje de descuento
#     """
#     descuento = precio_original - precio_con_descuento
#     porcentaje_descuento = (descuento / precio_original) * 100
#     return porcentaje_descuento


# precio_original = int(input("Ingrese el precio original de su compra: "))
# precio_con_descuento = int(input("Ingrese el precio con el descuento aplicado: "))
# porcentaje_descuento = calcular_porcentaje_descuento(precio_original, precio_con_descuento)

# print(f"El porcentaje de descuento aplicado es del {porcentaje_descuento}%")

"""
4- Crear una función que calcule el promedio de edad de un grupo de personas. 
Recibe una lista de edades y devuelve el promedio.
"""

# lista_de_edades = [22, 24, 26, 21, 28]

# def calcular_promedio_edad(lista_de_edades):
#     """
#     Recibe: lista de edades
#     Valida que la lista no se encuentre vacia
#     Devuelve: resultado del promedio
#     """
#     if len(lista_de_edades) == 0:
#         return 0
#     suma_edades = sum(lista_de_edades)
#     promedio = int(suma_edades/len(lista_de_edades))
#     return promedio

# promedio_edad = calcular_promedio_edad(lista_de_edades)

# print(f"El promedio de edad es de {promedio_edad} años")

"""
5- Crear una función que determine si un número es primo o no. 
Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.
"""

# def determina_si_numero_es_primo(numero):
#     """
#     Recibe: un numero entero
#     Verifica si el mismo es primo
#     Devuelve True si es primo o False si no lo es
#     """
#     if numero <= 1:
#         return False

#     for divisor in range(2, int(numero**0.5) + 1):
#         if numero % divisor == 0:
#             return False

#     return True

# numero = int(input("Ingrese un numero: "))

# resultado = determina_si_numero_es_primo(numero)

# if resultado:
#     mensaje = f"{numero} es un número primo"
# else:
#     mensaje = f"{numero} no es un número primo"

# print(mensaje)

"""
6- Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
"""

# def calcular_area_triangulo(base, altura):
#     """
#     Recibe: valor de base y altura
#     calcula area del triangulo
#     Devuelve: valor del area del triangulo
#     """
#     area = (base * altura) / 2
#     return area


# base = int(input("Ingrese la base de su triangulo: "))
# altura = int(input("Ingrese la altura de su triangulo: "))

# area_del_triangulo = calcular_area_triangulo(base, altura)

# print(f"El area su triángulo con base {base} y altura {altura} es de {area_del_triangulo:.2f} centimetros cuadrados")

"""
7- Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
"""

# def calcula_maximo_comun_divisor(numero_a,numero_b):
#     """
#     Recibe dos números enteros.
#     Calcula el máximo común divisor
#     Retorna el valor del maximo comun divisor
#     """
#     numero_menor = 0
#     numero_mayor = 0

#     if numero_a >= numero_b:
#         numero_menor = numero_b
#         numero_mayor = numero_a
#     else:
#         numero_menor = numero_a
#         numero_mayor = numero_b

#     while numero_mayor != 0:
#         numero_temporal = numero_mayor
#         numero_mayor = numero_menor % numero_mayor
#         maximo_comun_divisor = numero_temporal

#     return maximo_comun_divisor

# numero_a = int(input("Ingrese el primer número: "))
# numero_b = int(input("Ingrese el segundo número: "))

# maximo_comun_divisor = calcula_maximo_comun_divisor(numero_a, numero_b)
# print(f"El máximo común divisor de {numero_a} y {numero_b} es {maximo_comun_divisor}.")

"""
8- Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.
"""

# def informa_si_es_par_o_impar(numero:int):
#     """
#     Recibe un número entero.
#     Calcula si el número es par o impar 
#     Retorna True si es par o False si es impar
#     """
#     resto = numero % 2
#     if resto == 0:
#         return True
#     else:
#         return False

# numero = int(input("Ingrese un numero: "))
# if informa_si_es_par_o_impar(numero):
#     print(f"{numero} es un número par.")
# else:
#     print(f"{numero} es un número impar.")

"""
9- Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
"""

# def contar_elemento_en_lista(lista, elemento):
#     """
#     Recibe una lista y un elemento
#     Cuenta y retorna la cantidad de veces que aparece el elemento en la lista
#     """
#     contador = 0
#     for item in lista:
#         if item == elemento:
#             contador += 1
#     return contador

# lista_de_elementos = ["perro", "perro","alfombra", "alfombra", "alfombra", "sombrero"]
# print(lista_de_elementos)

# elemento_a_contar = input("Seleccione un elemento en la lista para saber su cantidad: ")
# while not elemento_a_contar in lista_de_elementos:
#     elemento_a_contar = input("Error. Seleccione un elemento en la lista: ")

# cantidad = contar_elemento_en_lista(lista_de_elementos, elemento_a_contar)
# print(f"{elemento_a_contar} aparece {cantidad} veces en la lista")

"""
10- Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
"""

# lista_de_palabras = [
#     "murcielago", "otorrinolaringologo", "auto", "pepsi"
# ]

# def encuentra_palabra_mas_larga_de_la_lista(lista):
#     """
#     Recibe una lista de palabras
#     Encuentra y devuelve la palabra mas larga
#     """
#     palabra_mas_larga = None

#     if lista:
#         for palabra in lista:
#             if palabra_mas_larga == None or len(palabra_mas_larga) <= len(palabra):
#                 palabra_mas_larga = palabra
#         return palabra_mas_larga

# palabra_encontrada = encuentra_palabra_mas_larga_de_la_lista(lista_de_palabras)
# print(f"La palabra con mas cantida de letras es: {palabra_encontrada}")

"""
11- Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
"""

# def contar_vocales(cadena):
#     """
#     Recibe una cadena de texto
#     Encuentra y devuelve la cantidad de vocales que tiene
#     """
#     cadena = cadena.lower()

#     vocales = ["a","e","i","o","u"]

#     contador = 0

#     for caracter in cadena:
#         if caracter in vocales:
#             contador += 1

#     return contador


# cadena = input("Ingrese una cadena de texto: ")
# cantidad_de_vocales = contar_vocales(cadena)
# print(f"La cantidad de vocales en la cadena es: {cantidad_de_vocales}")

"""
12 -Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
"""

# def nombres_en_comun(lista_1, lista_2):
#     """
#     """
#     set_lista_1 = set(lista_1)
#     set_lista_2 = set(lista_2)

#     nombres_comunes = set_lista_1.intersection(set_lista_2)

#     lista_nombres_comunes = list(nombres_comunes)

#     return lista_nombres_comunes

# nombres1 = ["Juan", "Nacho", "Fran", "Moli", "Flor"]
# nombres2 = ["Flor", "Luis", "Elena", "Carlos"]

# nombres_comunes = nombres_en_comun(nombres1, nombres2)
# print(f"Nombres en común: {nombres_comunes}")

"""
13- Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.
"""

# lista_de_palabras_1 = ["pepe", "moni", "dardo", "paola", "mariaelena", "fatiga"]

# def retorna_diccionario_palabras_y_cantidad_letras(lista_palabras: list) -> dict:

#     diccionario_palabras = {}
#     for palabra in lista_palabras:
#         diccionario_palabras[palabra] = len(palabra)

#     return diccionario_palabras

# diccionario_final = retorna_diccionario_palabras_y_cantidad_letras(lista_de_palabras_1)

# for clave, valor in diccionario_final.items():
#     mensaje = f"La palabra: {clave} tiene {valor} letras. "
#     print(mensaje)

"""
14- Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.
"""

# def valores_lista_numeros(lista_numeros):

#     valor_minimo = lista_numeros[0]
#     valor_maximo = lista_numeros[0]
#     suma = 0

#     for numero in lista_numeros:
#         if numero < valor_minimo:
#             valor_minimo = numero
#         if numero > valor_maximo:
#             valor_maximo = numero
#         suma += numero

#     promedio = suma / len(lista_numeros)

#     valores = {
#         "minimo": valor_minimo,
#         "maximo": valor_maximo,
#         "promedio": promedio
#     }

#     return valores

# numeros = [22, 24, 26, 21, 28]
# resultado = valores_lista_numeros(numeros)
# print(resultado)

"""
15- Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.
"""

# lista_de_peliculas = [
#     {
#         "titulo": "Transformers 1",
#         "genero": "Accion",
#         "director": "Michael Bay"
#     },
#     {
#         "titulo": "Transformers 2",
#         "genero": "Accion",
#         "director": "Michael Bay"
#     },
#     {
#         "titulo": "Transformers 3",
#         "genero": "Accion",
#         "director": "Michael Bay"
#     },
#     {
#         "titulo": "EL juego del miedo",
#         "genero": "Terror",
#         "director": "David Hackl"
#     },
#     {
#         "titulo": "EL juego del miedo 2",
#         "genero": "Terror",
#         "director": "David Hackl"
#     },
#     {
#         "titulo": "Black Clover",
#         "genero": "Animacion",
#         "director": "Yuki Tabata"
#     },
# ]

# def devuelve_cantidad_peliculas_por_genero(lista_peliculas: list[dict]) -> dict:

#     informe_cantidades = {}

#     for pelicula in lista_peliculas:
#         genero = pelicula.get("genero","Sin genero")
#         if not genero in informe_cantidades.keys():
#             informe_cantidades[genero] = 1
#         else:
#             informe_cantidades[genero] += 1
#     return informe_cantidades

# def devuelve_cantidad_peliculas_por_genero(lista_peliculas: list[dict]) -> dict:

#     informe_cantidades = {}

#     for pelicula in lista_peliculas:
#         genero = pelicula.get("genero","Sin genero")
#         informe_cantidades[genero] = informe_cantidades.get(genero, 0) + 1

#     return informe_cantidades

# informe = devuelve_cantidad_peliculas_por_genero(lista_de_peliculas)
# print(informe)
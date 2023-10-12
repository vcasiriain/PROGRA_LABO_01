"""
1. Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
"""
def devuelve_mayusculas(cadena):
    return cadena.upper()

cadena = devuelve_mayusculas("Hola Mundo")
print(cadena)
"""
2. Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
"""
def devuelve_minusculas(cadena):
    return cadena.lower()

cadena = devuelve_minusculas("Hola Mundo")
print(cadena)
"""
3. Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
"""
def concatenar_cadenas(cadena_1, cadena_2):
    return cadena_1 + " " + cadena_2

def concatenar_cadenas(cadena_1, cadena_2):
    mensaje = "{0} {1}".format(cadena_1,cadena_2)
    return mensaje

def concatenar_cadenas(cadena_1, cadena_2):
    mensaje = f"{cadena_1} {cadena_2}"
    return mensaje

def concatenar_cadenas(cadena_1, cadena_2):
    lista_de_cadenas = [cadena_1,cadena_2]
    cadena_final = " ".join(lista_de_cadenas)
    return cadena_final

cadena = concatenar_cadenas("Hola Mundo", "Chau Mundo")
print(cadena)
"""
4. Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
"""
def contar_caracteres(cadena):
    return len(cadena)

cantidad_caracteres = contar_caracteres("Hola Mundo")
print(cantidad_caracteres)
"""
5. Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
"""
def contar_aparicion_de_caracteres(cadena, caracter):
    return cadena.count(caracter)

aparicion_caracter = contar_aparicion_de_caracteres("Hola Mundo", "o")
print(aparicion_caracter)
"""
6. Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
"""
def muestra_palabras_con_caracter(cadena, caracter):
    palabras_con_caracter = []
    palabras = cadena.split()
    
    for palabra in palabras:
        if caracter in palabra:
            palabras_con_caracter.append(palabra)
    
    return palabras_con_caracter

lista_palabras = muestra_palabras_con_caracter("Hola mundo, como andan el dia de hoy?", "o")
print(lista_palabras)
"""
7. Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
"""
def eliminar_todos_los_espacios(cadena): #elimina todos los espacios que existan en la cadena
    return cadena.replace(" ", "")

def eliminar_espacios_delante_detras(cadena): #elimina solo los espacios delante y detras
    return cadena.strip()

cadena_con_espacios = eliminar_espacios_delante_detras("       Hola mundo, como andan el dia de hoy?     ")
print(cadena_con_espacios)
"""
8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
"""
def corregir_nombre_apellido(nombre, apellido):

    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    return{"nombre": nombre, "apellido": apellido}

nombre_apellido = corregir_nombre_apellido("  valentin ","   casiriain ")
print(nombre_apellido)  
"""
9. Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
"""
def unir_nombre_con_salto_de_linea(nombres):
    return "\n".join(nombres)

nombres = unir_nombre_con_salto_de_linea(["Valen", "Flor", "Nacho", "Juan", "Fran"])
print(nombres)
"""
10. Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
Por ejemplo Facundo Falcone: f.falcone@utn-fra.com.ar
"""
def crear_email(nombre, apellido):
    inicial_nombre = nombre[0].lower()
    email = f"{inicial_nombre}.{apellido.lower()}@utn-fra.com.ar"
    return email

"""
11. Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
"""
def concatenar_palabras(palabras):
    cadena = palabras[0]
    for palabra in palabras[1:-1]:
        cadena += ", " + palabra
    cadena += " y " + palabras[-1]
    return cadena
    
palabras = ["manzanas", "naranjas", "bananas"]
palabras = concatenar_palabras(palabras)
print(palabras)
"""
12. Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
"""
def ocultar_numero_tarjeta(numero_tarjeta):
    longitud = len(numero_tarjeta)
    asteriscos = "*" * (longitud - 4)
    ultimos_cuatro = numero_tarjeta[-4:]
    numero_oculto = asteriscos + " " + ultimos_cuatro
    return numero_oculto
"""
13. Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
"""

"""
14. Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
"""

"""
15. Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
"""

"""
16. Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
"""

"""
17. Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
"""

"""
18. Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
"""

"""
19. Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
"""

"""
20. Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
"""

"""
21. Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
"""

"""
7. USAR REPLACE
"""
"""
8. USAR STRIP Y CAPITALIZE
"""
"""
9. USAR JOIN
"""
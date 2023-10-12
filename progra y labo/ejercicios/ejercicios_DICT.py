"""
1- Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".
"""

# dias_de_la_semana = {
#     "lunes": 1,
#     "martes": 2,
#     "miercoles": 3,
#     "jueves": 4,
#     "viernes": 5,
#     "sabado": 6,
#     "domingo": 7
# }

# print(dias_de_la_semana.get("miercoles", "la clave no existe"))

"""
2- Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".
"""

# meses_del_anio = {
#     "enero": 1,
#     "febrero": 2,
#     "marzo": 3,
#     "abril": 4,
#     "mayo": 5,
#     "junio": 6,
#     "julio": 7,
#     "agosto": 8,
#     "septiembre": 9,
#     "octubre": 10,
#     "noviembre": 11,
#     "diciembre": 12
# }

# print(meses_del_anio.get("junio", "la clave no existe"))

"""
3- Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
"""

# info_pelicula = {
#     "titulo": "Shrek",
#     "director": "Mike Mitchell",
#     "año": "2001"
# }

# print(info_pelicula.get("titulo", "la clave no existe"))

"""
4- Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
"""

# direccion = {
#     "nombre de la calle": "Salom",
#     "altura": "551",
#     "localidad": "Barracas",
#     "codigo postal": "1277",
#     "partido": "Capital Federal",
#     "provincia": "Buenos Aires"
# }

# nombre_de_la_calle = direccion.get("nombre de la calle", "el nombre de la calle no fue definido")
# altura = direccion.get("altura", "la altura de la calle no fue definida")

# print(f"la calle es {nombre_de_la_calle} y la altura es {altura}")

"""
5- Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".
"""

# continentes = {
#     "America": 1,
#     "Europa": 2,
#     "Asia": 3,
#     "Antartida": 4,
#     "Oceania": 5,
#     "Africa": 6
#     }

# print(continentes.get("Africa", "la clave no existe"))

"""
6- Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".
"""

# estaciones = {
#     "Otoño": 1,
#     "Invierno": 2,
#     "Primavera": 3,
#     "Verano": 4,
#     }

# print(estaciones.get("Invierno", "la clave no existe"))


"""
7- Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.
"""

# datos_cancion = {
#     "titulo": "La Fama",
#     "artista": "Rosalia feat The Weeknd",
#     "duracion": "03:08"
# }

# print(datos_cancion.get("duracion", "la clave no existe"))

"""
8- Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.
"""

# edad_personas = {
#     "Flor": 22,
#     "Valen": 24,
#     "Bianca": 2
# }

# print(edad_personas.get("Bianca", "la clave no existe"))

"""
9- Crea un diccionario que contenga las capitales de los países de América del Sur. 
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
"""

# capitales_sudamerica = {
#     "Argentina": "Buenos Aires",
#     "Brasil": "Brasilia",
#     "Uruguay": "Montevideo",
#     "Paraguay": "Asuncion",
#     "Bolivia": "La Paz"
# }

# nombre_de_pais = input("Ingrese el nombre de un pais de SudAmerica: ").capitalize()

# while not nombre_de_pais in capitales_sudamerica.keys():
#     mensaje = f"El nombre del pais {nombre_de_pais} no esta presente, ingrese otro: "
#     nombre_de_pais = input(mensaje).capitalize()
# else:
#     capital_seleccionada = capitales_sudamerica.get(nombre_de_pais)

# print(f"La capital de {nombre_de_pais} es {capital_seleccionada}!")

"""
10- Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.
"""

# notas_alumnos = {
#     "Juan": 6,
#     "Nacho": 7,
#     "Fran": 9,
#     "Valen": 6
# }

# suma = 0
# for nota in notas_alumnos.keys():
#     nota = notas_alumnos[nota]
#     suma += nota

# promedio = suma/(len(notas_alumnos))

# print(f"El promedio de las notas es {promedio}")

"""
11- Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
"""

# tareas_por_hacer = {
#     "tarea_1": "completada",
#     "tarea_2": "pendiente",
#     "tarea_3": "en proceso"
# }

# for clave, valor in tareas_por_hacer.items():
#     print(clave,valor)

"""
12- Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
"""
# lista_de_compras = {
#     "Cereal": "2",
#     "Fideos": "4",
#     "Papel": "6",
#     "Carne": "3"
# }

# nombre_de_producto = input("Ingrese un producto: ").capitalize()

# while not nombre_de_producto in lista_de_compras.keys():
#     mensaje = f"El nombre del producto {nombre_de_producto} no esta presente, ingrese otro: "
#     nombre_de_producto = input(mensaje).capitalize()
# else:
#     producto_seleccionado = lista_de_compras.get(nombre_de_producto)

# print(f"La cantidad de {nombre_de_producto} es {producto_seleccionado}")

"""
13- Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
"""

# info_juegos_de_mesa = {
#     "Monopoly": "Intermedio",
#     "Truco": "Facil",
#     "Canasta": "Facil",
#     "Poker": "Dificil"
# }

# nivel_de_dificultad = input("Ingrese el nivel de dificultad: ").capitalize()
# while not nivel_de_dificultad in info_juegos_de_mesa.values():
#     nivel_de_dificultad = input(f"El nivel de dificultad {nivel_de_dificultad} no esta presente, ingrese otro: ").capitalize()

# for clave, valor in info_juegos_de_mesa.items():
#     if valor == nivel_de_dificultad:
#         print(clave)

"""
14- Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
"""

# juego_de_puntajes = {
#     "Poroto": "25",
#     "Juji": "50",
#     "Salvatore": "100"
# }

# for clave, valor in juego_de_puntajes.items():
#     print (clave,valor)

# jugador_elegido = input("Ingrese el nombre de un jugador 'Poroto', 'Juji' o 'Salvatore' : ").capitalize()

# while not jugador_elegido in juego_de_puntajes.keys():
#     mensaje = f"El nombre del jugador {jugador_elegido} no esta presente, ingrese otro: "
#     jugador_elegido = input(mensaje).capitalize()

# puntaje_nuevo = input("Ingrese un puntaje para su jugador: ")
# juego_de_puntajes[jugador_elegido] = puntaje_nuevo

# for clave, valor in juego_de_puntajes.items():
#     print (clave,valor)

"""
15- Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.
"""

# lista_de_empleados = {
#     "Julian": 70000,
#     "Rodrigo": 50000,
#     "Lionel": 200000
# }

# for clave, valor in lista_de_empleados.items():
#     print (f"El empleado: {clave} cobra: ${valor}")

# empleado_elegido = input("Ingrese el nombre de un empleado 'Julian', 'Rodrigo' o 'Lionel' : ").capitalize()

# while not empleado_elegido in lista_de_empleados.keys():
#     empleado_elegido = input(f"El nombre del empleado {empleado_elegido} no esta presente, ingrese otro: ").capitalize()

# aumento_sueldo = input("Ingrese un monto de dinero a aumentar: $")
# sueldo_int = int(lista_de_empleados[empleado_elegido])
# aumento_sueldo_int = int(aumento_sueldo)

# lista_de_empleados[empleado_elegido] = aumento_sueldo_int + sueldo_int

# for clave, valor in lista_de_empleados.items():
#     print (f"El empleado: {clave} cobra: ${valor}")

"""
16- Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes
"""

# tareas_pendientes = {
#     "Limpiar": False,
#     "Estudiar": False,
#     "Comprar": False 
# }

# estado_de_tarea = "Incompleta"

# print(tareas_pendientes)

# for clave in tareas_pendientes:
#     print(clave,estado_de_tarea)

# tarea_elegida = input("Selecciona una tarea para completarla 'Limpiar', 'Estudiar' o 'Comprar': ").capitalize()

# while not tarea_elegida in tareas_pendientes.keys():
#     tarea_elegida = input(f"La tarea {tarea_elegida} no es correcta, ingrese otra: "). capitalize()
# else:
#     print(f"Usted marco la tarea {tarea_elegida} como completa")
#     del(tareas_pendientes[tarea_elegida])

# print(tareas_pendientes)

# for clave in tareas_pendientes:
#     print(clave,estado_de_tarea)

"""
17- Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
"""

# peliculas_en_cartelera = {
#     "Endgame": "15:50",
#     "Avatar": "17:30",
#     "Mario": "20:30"
# }

# print(peliculas_en_cartelera)

# peliculas_en_cartelera["Endgame"] = "19:30"

# print(peliculas_en_cartelera)

"""
18- Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación 
"""

# juegos_puntuados = {
#     "Zomboid": 0,
#     "Terraria": 0,
#     "Survivors": 0,
#     "Astroneer": 0
# }

# print(juegos_puntuados)
# puntaje = range(11)

# while True:
#     nombre_del_juego = input("Seleccione el nombre de un juego: ").capitalize()
#     if not nombre_del_juego in juegos_puntuados.keys():
#         print(f"El juego {nombre_del_juego} se agrego a la lista")

#     puntaje_elegido = input("Ingrese un puntaje del 1 al 10: ")
#     puntaje_elegido_int = int(puntaje_elegido)
#     while not puntaje_elegido_int in puntaje:
#         puntaje_elegido = input("Error. Ingrese un puntaje del 1 al 10: ")
#         puntaje_elegido_int = int(puntaje_elegido)

#     juegos_puntuados.update({nombre_del_juego: puntaje_elegido})
    
#     continuar = input("Desea continuar? s/n ")
#     if continuar == "n":
#         break

# print(juegos_puntuados)

"""
19- Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.
"""

# dias_de_la_semana = {
#    "lunes": 22,
#    "martes": 17,
#    "miercoles": 21,
#    "jueves": 18,
#    "viernes": 23,
#    "sabado": 24,
#    "domingo": 16
# }

# cantidad_de_dias = len(dias_de_la_semana)
# suma_temperatura = 0

# for valor in dias_de_la_semana.value():
#     temperatura = int(valor)
#     suma_temperatura += temperatura

# promedio_temperatura = suma_temperatura/cantidad_de_dias

# print(f"El promedio de temperatura de la semana es de es de {promedio_temperatura:.2f}")

"""
20- Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres
"""

# asientos_de_avion = {
#     "V25": False,
#     "P26": False,
#     "V27": False,
#     "P28": False,
#     "V29": False,
#     "P30": False
# }

# estado_de_asiento = "Vacio"

# print(asientos_de_avion)

# for clave in asientos_de_avion:
#     print(clave,estado_de_asiento)

# asiento_elegido = input("Elija un asiento para su vuelo: ").capitalize()

# while not asiento_elegido in asientos_de_avion.keys():
#     asiento_elegido = input(f"La asiento {asiento_elegido} no existe o ya fue ocupado, elija otro: ").capitalize()
# else:
#     print(f"Usted eligio correctamente el asiento {asiento_elegido}")
#     del(asientos_de_avion[asiento_elegido])

# print(asientos_de_avion)

# for clave in asientos_de_avion:
#     print(clave,estado_de_asiento)

"""
21- Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
"""

# lista_de_gastos = {
#    "Juegos": 2000,
#    "Comida": 3000,
#    "Libros": 3000,
#    "Higiene": 8000,
# }

# print(lista_de_gastos)

# suma_gastos = 0

# for gastos in lista_de_gastos.keys():
#     gastos = lista_de_gastos[gastos]
#     suma_gastos += gastos

# print(f"El total de sus gastos es de ${suma_gastos}")

"""
22- Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona en el mes.
"""

# lista_de_gastos = {
#    "Juegos": 2000,
#    "Comida": 3000,
#    "Libros": 3000,
#    "Higiene": 8000,
# }

# print(lista_de_gastos)

# suma_gastos = 0
# dias_del_mes = 30

# for clave, valor in lista_de_gastos.items():
#     gastos = int(valor)
#     suma_gastos += gastos
#     gasto_por_mes = suma_gastos * dias_del_mes

# print(f"El total de sus gastos por mes es de ${gasto_por_mes}")

"""
23- Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.
"""

# contactos_de_telefono = {
#    "Flor": 1520304050,
#    "Juan": 1580706050,
#    "Nacho": 1540504040,
#    "Moli": 1530303030,
# }

# print(contactos_de_telefono)

# continuar_cargando_telefonos = True
# telefono = range(1499999999,1600000000)

# while continuar_cargando_telefonos != False:
#     contacto_elegido = input("Ingrese el nombre de un contacto: ").capitalize()
#     if not contacto_elegido in contactos_de_telefono.keys():
#         print(f"El contacto {contacto_elegido} se agrego a la lista")

#     numero_de_telefono_agregado = int(input("Ingrese el telefono para su contacto: "))
    
#     while not numero_de_telefono_agregado in telefono:
#         numero_de_telefono_agregado = int(input(f"Error. Elija un telefono correcto: "))
#     else:
#         print(f"Usted modifico correctamente el telefono a {numero_de_telefono_agregado}")

#     contactos_de_telefono.update({contacto_elegido: numero_de_telefono_agregado})

#     continuar_cargando_telefonos = input("Desea continuar? s/n: ").capitalize()

#     while continuar_cargando_telefonos != "N":
#         continuar_cargando_telefonos = input(f"Ingrese una opcion valida. Desea continuar? s/n: ").capitalize()
#     else:
#         continuar_cargando_telefonos = False

# print(contactos_de_telefono)
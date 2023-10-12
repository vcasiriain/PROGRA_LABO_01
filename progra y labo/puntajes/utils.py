def formatear_puntaje(puntaje: str) -> str:
    return str(puntaje.zfill(5))

def formatear_nombre_jugador(nombre: str) -> str:
    return nombre.strip().split(" ")[0].upper()

def ordenar_puntajes(lista_puntajes:list[dict]):
    lista_puntajes_ordenada = sorted(lista_puntajes, key=lambda puntaje:puntaje["puntaje"],reverse=True)

# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
# por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el 
# nombre del mes.

# Funcion que formetea el string a formato fecha
def formatear_fecha(fecha:str) -> str:
    """
    Formatea una fecha en el formato dd/mm/aaaa a dd de <nombre del mes> de aaaa.

    Parameters
    ----------
    fecha : str 
        Es el tipo de fecha en formato dd/mm/aaaa.

    Returns
    -------
    str: 
        La fecha formateada o None si el formato o mes son inválidos.
    """
    meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
        7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 
        12: "diciembre"
    }

    partes_fecha = fecha.split('/')
    if len(partes_fecha) == 3 and partes_fecha[0].isdigit() and partes_fecha[1].isdigit() and partes_fecha[2].isdigit():
        dia = int(partes_fecha[0])
        mes = int(partes_fecha[1])
        anio = int(partes_fecha[2])

        if mes in meses:
            nombre_mes = meses[mes]
            fecha_formateada = f"{dia} de {nombre_mes} de {anio}"
            return fecha_formateada
        else:
            return None  # Mes inválido
    else:
        return None  # Formato de fecha incorrecto

if __name__ == "__main__":
    # Entrada
    fecha_valida = False
    while not fecha_valida:
        fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
        # Proceso
        fecha_formateada = formatear_fecha(fecha)
        if fecha_formateada is not None:
            fecha_valida = True
            # Salida
            print(fecha_formateada)
        else:
            print("Fecha inválida. Por favor, ingrese una fecha válida en formato dd/mm/aaaa.")

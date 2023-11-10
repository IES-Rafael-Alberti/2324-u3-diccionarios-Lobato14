# Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos 
# puntos, y cada par <palabra>:<traducción> separados por comas. El programa 
# debe crear un diccionario con las palabras y sus traducciones. Después 
# pedirá una frase en español y utilizará el diccionario para traducirla 
# palabra a palabra. Si una palabra no está en el diccionario debe dejarla 
# sin traducir.

def son_todas_letras(palabras:str) -> bool:
    """
    Verifica si todas las palabras de una cadena están compuestas únicamente por letras.

    Parameters
    ----------
    - palabras : str 
        Cadena de palabras en formato 'palabra:traduccion' separadas por espacios.

    Returns
    -------
    - bool: 
        True si todas las palabras son válidas (compuestas solo por letras), False en caso contrario.
    """
    for par in palabras:
        palabra, traduccion = par.strip().split(':')
        if not palabra.isalpha() or not traduccion.isalpha():
            return False
    return True


def traducir_frase(diccionario:dict, frase:str) -> str:
    """
    Traduce una frase palabra por palabra utilizando un diccionario.

    Parameters
    ----------
    - diccionario : dict
        Diccionario que contiene las traducciones de las palabras.
    - frase : str
        La frase que se desea traducir.

    Returns
    -------
    - str:
        La frase traducida, donde las palabras no encontradas en el diccionario se 
        mantienen iguales.
    """
    palabras = frase.split()
    frase_traducida = []
    for palabra in palabras:
        traduccion = diccionario.get(palabra, palabra)
        frase_traducida.append(traduccion)
    return ' '.join(frase_traducida)


def crear_diccionario(entrada_usuario:str) -> dict:
    """
    Crea un diccionario a partir de la entrada del usuario que contiene pares de palabras y 
    sus traducciones.

    Parameters
    ----------
    - entrada_usuario : str 
        Cadena que contiene pares de palabras y traducciones separadas por comas 
        introducidas por el usuario


    Returns
    --------
    - dict: 
        Diccionario creado a partir de las palabras y traducciones proporcionadas por 
        el usuario.
    """
    diccionario = {}
    pares_palabras = entrada_usuario.split(',')
    for par in pares_palabras:
        palabra, traduccion = par.strip().split(':')
        diccionario[palabra] = traduccion
    return diccionario

def verificar_frase(frase_espanol:str) -> bool:
    """
    Verifica si una cadena contiene solo letras, lo que sugiere que es una frase en 
    español.

    Parameters
    ----------
    - frase_espanol : str
        Cadena que se desea verificar.

    Returns
    -------
    - bool:
        True si la cadena contiene solo letras, False en caso contrario.
    """
    return frase_espanol.replace(" ", "").isalpha()


if __name__ == "__main__":
    # Entrada
    diccionario = {}
    formato_correcto = False
    # Proceso
    while not formato_correcto:
        entrada_usuario = input("Introduce las palabras en español e inglés separadas por dos puntos y comas: ")
        formato_correcto = son_todas_letras(entrada_usuario.split(','))
        if formato_correcto:
            diccionario = crear_diccionario(entrada_usuario)
        else:
            print("Error: Las palabras deben contener solo letras.")

    frase_valida = False
    while not frase_valida:
        frase_espanol = input("Introduce una frase en español: ")
        frase_valida = verificar_frase(frase_espanol)
        if not frase_valida:
            print("Error: La frase debe contener solo letras y espacios.")
    
    frase_traducida = traducir_frase(diccionario, frase_espanol)
    print("Frase traducida: ", frase_traducida)
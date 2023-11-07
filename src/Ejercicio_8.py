# Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos 
# puntos, y cada par <palabra>:<traducción> separados por comas. El programa 
# debe crear un diccionario con las palabras y sus traducciones. Después 
# pedirá una frase en español y utilizará el diccionario para traducirla 
# palabra a palabra. Si una palabra no está en el diccionario debe dejarla 
# sin traducir.

# Funcion que comprueba si todas las palabras de una cadena son palabras
def son_todas_letras(palabras):
    for par in palabras:
        palabra, traduccion = par.strip().split(':')
        if not palabra.isalpha() or not traduccion.isalpha():
            return False
    return True

# Funcion que traduce la palabra desde el dicionario a la frase
def traducir_frase(diccionario, frase):
    palabras = frase.split()
    frase_traducida = []
    for palabra in palabras:
        traduccion = diccionario.get(palabra, palabra)
        frase_traducida.append(traduccion)
    return ' '.join(frase_traducida)

# Función en donde secrea el diccionario de las palabras a traducir
def crear_diccionario(entrada_usuario):
    diccionario = {}
    pares_palabras = entrada_usuario.split(',')
    for par in pares_palabras:
        palabra, traduccion = par.strip().split(':')
        diccionario[palabra] = traduccion
    return diccionario

# Función que verifica la frase traducida
def verificar_frase(frase_espanol):
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
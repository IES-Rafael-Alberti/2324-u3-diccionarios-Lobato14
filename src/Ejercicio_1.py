# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':
# '$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
# de aviso si la divisa no está en el diccionario.

# Funcion que busca si dicha divisa está o no en el diccionario.
def buscarDiccionarioMonetario(diccionarioMonetario:dict, divisa:str) -> bool:
    """ Busca la divisa introducida en el diccionario.

    Parameters
    ----------
    diccionarioMonetario : dict
        Diccionario en donde se guardan las divisas
    
    divisa: str
        Divisa introducida por teclado

    Returns
    -------
    bool
        Devuelve False si la divisa no está en el diccionario y True si la divisa está
        en el diccionario 
    
    """
    if divisa not in diccionarioMonetario:
        return False
    else:
        return True

if __name__ == "__main__":
    # Entrada
    diccionarioMonetario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    divisa = input("Escribe una divisa: ")
    # Procesamiento
    resultadoDivisa = buscarDiccionarioMonetario(diccionarioMonetario, divisa)
    # Salida
    print(resultadoDivisa)
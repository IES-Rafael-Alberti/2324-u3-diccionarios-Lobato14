from src.Ejercicio_1 import buscarDiccionarioMonetario

def test_buscarDiccionarioMonetario():
    """
        Función que busca comprueba el valor monetario que existe en el diccionario
    """
    diccionarioMonetario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    assert buscarDiccionarioMonetario(diccionarioMonetario, "Euro") == "El símbolo de la divisa Euro es €"
    assert buscarDiccionarioMonetario(diccionarioMonetario, "Libra") == "La divisa no se encuentra en el diccionario"
    assert buscarDiccionarioMonetario(diccionarioMonetario, "") == "La divisa no se encuentra en el diccionario"
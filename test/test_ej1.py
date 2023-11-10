from src.Ejercicio_1 import buscarDiccionarioMonetario

def test_buscarDiccionarioMonetario():
    diccionarioMonetario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    assert buscarDiccionarioMonetario(diccionarioMonetario, "Euro") == True
    assert buscarDiccionarioMonetario(diccionarioMonetario, "Libra") == False
    assert buscarDiccionarioMonetario(diccionarioMonetario, "") == False
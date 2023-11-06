from src.Ejercicio_8 import son_todas_letras, verificar_frase, crear_diccionario, traducir_frase

def test_son_todas_letras():
    assert son_todas_letras(["perro:dog", "gato:cat"])
    assert not son_todas_letras(["perro:dog", "gato:123"])

def test_verificar_frase():
    assert verificar_frase("Hola mundo")
    assert not verificar_frase("Hola123")

def test_crear_diccionario():
    entrada_usuario = "perro:dog, gato:cat, casa:house"
    assert crear_diccionario(entrada_usuario) == {"perro": "dog", "gato": "cat", "casa": "house"}

def test_traducir_frase():
    diccionario = {"perro": "dog", "gato": "cat"}
    frase_espanol = "perro gato"
    assert traducir_frase(diccionario, frase_espanol) == "dog cat"
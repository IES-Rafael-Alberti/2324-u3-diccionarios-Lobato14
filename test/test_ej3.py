from src.Ejercicio_3 import calcular_precio

def test_calcular_precio_fruta_valida():
    """
    Test para verificar el cálculo del precio final en el caso de que el precio sea válido.
    Se espera que el precio calculado sea igual a 1.60 para 2 kilos de manzanas.
    """
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Manzana"
    kilos = 2
    assert calcular_precio(fruta, kilos, diccionario_frutas) == 1.60

def test_calcular_precio_fruta_invalida():
    """
    Test para verificar que el cálculo del precio devuelve None cuando la fruta no está en el diccionario.
    Se espera que el resultado sea None para una fruta no válida como "Fresa".
    """
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Fresa"
    kilos = 2
    assert calcular_precio(fruta, kilos, diccionario_frutas) == None

def test_calcular_precio_kilos_negativos():
    """
    Test para verificar que el cálculo del precio devuelve None cuando se ingresan kilos negativos.
    Se espera que el resultado sea None para kilos negativos, por ejemplo, -1 kilo de plátanos.
    """
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Platano"
    kilos = -1
    assert calcular_precio(fruta, kilos, diccionario_frutas) == None
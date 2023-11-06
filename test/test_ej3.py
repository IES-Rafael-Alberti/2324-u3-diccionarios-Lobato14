from src.Ejercicio_3 import calcular_precio

def test_calcular_precio_fruta_valida():
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Manzana"
    kilos = 2
    assert calcular_precio(fruta, kilos, diccionario_frutas) == 1.60

def test_calcular_precio_fruta_invalida():
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Fresa"
    kilos = 2
    assert calcular_precio(fruta, kilos, diccionario_frutas) == None

def test_calcular_precio_kilos_negativos():
    diccionario_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = "Platano"
    kilos = -1
    assert calcular_precio(fruta, kilos, diccionario_frutas) == None
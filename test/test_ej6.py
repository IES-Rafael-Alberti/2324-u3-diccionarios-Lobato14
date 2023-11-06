from src.Ejercicio_6 import validar_edad, validar_telefono

def test_validar_edad():
    assert validar_edad("25") == True
    assert validar_edad("-5") == False
    assert validar_edad("abc") == False

def test_validar_telefono():
    assert validar_telefono("123456789") == True
    assert validar_telefono("abc") == False
    assert validar_telefono("123-456-789") == False
from src.Ejercicio_2 import validar_edad, validar_telefono

def test_validar_edad_valida():
    """Función que comprueba cuando se introduce una edad valida"""
    assert validar_edad("25") == True

def test_validar_edad_invalida():
    """Función que comprueba cuando se introduce una edad invalida"""
    assert validar_edad("-5") == False

def test_validar_telefono_valido():
    """Función que comprueba cuando se introduce un numero de telefono valido"""
    assert validar_telefono("123456789") == True

def test_validar_telefono_invalido():
    """Función que comprueba cuando se introduce un numero de telefono invalido"""
    assert validar_telefono("1234") == False
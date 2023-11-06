from src.Ejercicio_2 import validar_edad, validar_telefono

def test_validar_edad_valida():
    assert validar_edad("25") == True

def test_validar_edad_invalida():
    assert validar_edad("-5") == False

def test_validar_telefono_valido():
    assert validar_telefono("1234567890") == True

def test_validar_telefono_invalido():
    assert validar_telefono("1234") == False

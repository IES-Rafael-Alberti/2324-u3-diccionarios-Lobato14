from src.Ejercicio_4 import formatear_fecha

def test_fecha_valida():
    assert formatear_fecha("25/12/2023") == "25 de diciembre de 2023"

def test_mes_invalido():
    assert formatear_fecha("30/13/2023") == "Mes inválido. Por favor, ingrese una fecha válida."

def test_formato_incorrecto():
    assert formatear_fecha("30-12-2023") == "Formato de fecha incorrecto. Por favor, ingrese la fecha en formato dd/mm/aaaa."
from src.Ejercicio_4 import formatear_fecha

def test_fecha_valida():
    """
    Test para verificar que la función formatee correctamente una fecha válida.
    """
    assert formatear_fecha("25/12/2023") == "25 de diciembre de 2023"

def test_mes_invalido():
    """
    Test para verificar que la función devuelva el mensaje de mes inválido para un mes incorrecto.
    """
    assert formatear_fecha("30/13/2023") == "Mes inválido. Por favor, ingrese una fecha válida."

def test_formato_incorrecto():
    """
    Test para verificar que la función devuelva el mensaje de formato incorrecto para un formato de fecha incorrecto.
    """
    assert formatear_fecha("30-12-2023") == "Formato de fecha incorrecto. Por favor, ingrese la fecha en formato dd/mm/aaaa."
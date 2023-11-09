from src.Ejercicio_5 import mostrar_creditos, calcular_total_creditos

def test_mostrar_creditos():
    """
    Prueba la función mostrar_creditos para asegurar que formatea correctamente el mensaje
    con el nombre de las asignaturas y la cantidad de créditos correspondientes.
    """
    creditos_asig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    mensaje_esperado = "Matemáticas tiene 6 créditos.\nFísica tiene 4 créditos.\nQuímica tiene 5 créditos.\n"
    assert mostrar_creditos(creditos_asig) == mensaje_esperado

def test_calcular_total_creditos():
    """
    Prueba la función calcular_total_creditos para asegurar que suma correctamente los créditos
    de todas las asignaturas.
    """
    creditos_asig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    total_esperado = 15
    assert calcular_total_creditos(creditos_asig) == total_esperado
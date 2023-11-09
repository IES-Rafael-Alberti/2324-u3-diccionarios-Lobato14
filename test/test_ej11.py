from src.Ejercicio_11 import analizar_directorio

def test_analizar_directorio():
    """
        Función que analiza el directorio mediante resultados de prueba
    """
    directorio = {}
    directorio_texto = "nif;nombre;email;teléfono;descuento\n" + "01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n" + "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n" + "63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n" + "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    resultado = analizar_directorio(directorio_texto, directorio)
    assert resultado == {
        '01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5},
        '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0},
        '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2},
        '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}
    }
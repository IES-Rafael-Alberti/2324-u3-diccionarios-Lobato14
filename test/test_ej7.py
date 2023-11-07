from src.Ejercicio_7 import anadir_prod, mostrar_lista_compra

# Test para la función anadir_prod
def test_anadir_prod():
    listaCompra = {}
    anadir_prod(listaCompra, "Manzana", "1.5")
    assert len(listaCompra) == 1
    assert listaCompra["Manzana"] == 1.5

# Test para la función mostrar_lista_compra
def test_mostrar_lista_compra(capsys):
    listaCompra = {"Manzana": 1.5, "Naranja": 2.0}
    resultado_esperado = "\nLista de la compra\n\nManzana \t Precio: 1.5\nNaranja \t Precio: 2.0\n\nTotal \t\t Coste: 3.5"
    mostrar_lista_compra(listaCompra)
    captured = capsys.readouterr()
    assert captured.out.strip() == resultado_esperado

# Test para verificar la entrada y salida del programa principal
def test_programa_principal(monkeypatch, capsys):
    inputs = ["Manzana", "1.5", "si", "Naranja", "2.0", "no"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    import src.Ejercicio_7  # Importa el código principal para ejecutar el programa
    captured = capsys.readouterr()
    assert captured.out.strip() == "\nLista de la compra\n\nManzana \t Precio: 1.5\nNaranja \t Precio: 2.0\n\nTotal \t\t Coste: 3.5"
from src.Ejercicio_7 import anadir_prod, mostrar_lista_compra

# Test para la función anadir_prod
def test_anadir_prod():
    listaCompra = {}
    anadir_prod(listaCompra, "Manzana", "1.5")
    assert len(listaCompra) == 1
    assert listaCompra["Manzana"] == 1.5

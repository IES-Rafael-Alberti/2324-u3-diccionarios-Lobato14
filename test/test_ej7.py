import textwrap
from src.Ejercicio_7 import agregar_producto, mostrar_lista_compra

# Prueba para la función agregar_producto
def test_agregar_producto():
    listaCompra = {}
    agregar_producto(listaCompra, 1)
    assert len(listaCompra) == 1
    assert "Platano" in listaCompra
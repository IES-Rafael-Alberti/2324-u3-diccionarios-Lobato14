import textwrap
from src.Ejercicio_7 import agregar_producto, mostrar_lista_compra

# Prueba para la función agregar_producto
def test_agregar_producto():
    listaCompra = {}
    agregar_producto(listaCompra, 1)
    assert len(listaCompra) == 1
    assert "Platano" in listaCompra  # Utiliza la clave real ingresada por el usuario

# Prueba para la función mostrar_lista_compra

# Prueba para la función mostrar_lista_compra
def test_mostrar_lista_compra():
    listaCompra = {"Platano": 2.5, "Manzana": 1.0}
    resultado = mostrar_lista_compra(listaCompra)
    resultado_formateado = "\n".join(resultado)  # Convierte la lista en una sola cadena separada por saltos de línea
    resultado_esperado = textwrap.dedent("""
        Lista de la compra
        Platano   \t Precio: 2.5
        Manzana   \t Precio: 1.0
        Total     \t\t Coste: 3.5
    """).strip()
    assert resultado_formateado.strip() == resultado_esperado.strip()
from src.Ejercicio_9 import factura_a_pagar, estado_final, anadir_factura

# Test para la función pagar_factura
def test_factura_a_pagar():
    facturas = {"1": 100, "2": 200, "3": 0}
    assert factura_a_pagar(facturas, "1") == "Factura pagada correctamente."
    assert factura_a_pagar(facturas, "2") == "Factura pagada correctamente."
    assert factura_a_pagar(facturas, "3") == "Factura no encontrada o ya pagada."

# Test para la función estado_final
def test_estado_final():
    facturas = {"1": 100, "2": 200, "3": 0}
    assert estado_final(facturas) == (300, 300)

# Test para la función anadir_factura
def test_anadir_factura():
    facturas = {}
    anadir_factura(facturas, "1", 100)
    assert facturas == {"1": 100}
    anadir_factura(facturas, "2", 200)
    assert facturas == {"1": 100, "2": 200}
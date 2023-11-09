from src.Ejercicio_9 import pagar_factura, anadir_factura, estado_final_cobrado, estado_final_pendiente

def test_factura_a_pagar():
    """
        Test para comprobar la función pagar_factura
    """
    facturas = {"1": 100, "2": 200, "3": 0}
    assert pagar_factura(facturas, "1") == True
    assert pagar_factura(facturas, "2") == True
    assert pagar_factura(facturas, "3") == False

def test_estado_final_cobrado():
    """
        Test para comprobar la función estado_final_cobrado
    """
    facturas = {"1": 100, "2": 200, "3": 0}
    assert estado_final_cobrado(facturas) == 300

def test_estado_final_pendiente():
    """
        Test para comprobar la función estado_final_pendiente
    """
    facturas = {"1": 100, "2": 200, "3": 0}
    assert estado_final_pendiente(facturas) == 300

def test_anadir_factura():
    """
        Test para comprobar la función anadir_factura
    """
    facturas = {}
    anadir_factura(facturas, "1", 100)
    assert facturas == {"1": 100}
    anadir_factura(facturas, "2", 200)
    assert facturas == {"1": 100, "2": 200}
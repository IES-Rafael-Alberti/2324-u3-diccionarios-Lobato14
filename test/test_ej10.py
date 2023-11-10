# Archivo de prueba test_cliente.py
from src.Ejercicio_10 import anadir_cliente_base_datos, eliminar_cliente, anadir_datos

def test_anadir_cliente_base_datos():
    clientes = {}
    datos_cliente = {"nombre": "John", "apellidos": "Doe", "preferente": True}
    anadir_cliente_base_datos(clientes, "12345678A", datos_cliente)
    assert "12345678A" in clientes
    assert clientes["12345678A"] == datos_cliente

def test_eliminar_cliente():
    clientes = {"12345678A": {"nombre": "John", "apellidos": "Doe", "preferente": True}}
    eliminar_cliente(clientes, "12345678A")
    assert "12345678A" not in clientes

def test_anadir_datos():
    datos_cliente = {}
    anadir_datos(datos_cliente, "John", "Doe", "Dirección", "123456789", "john.doe@example.com", True, "12345678A")
    assert datos_cliente == {
        "nombre": "John",
        "apellidos": "Doe",
        "direccion": "Dirección",
        "telefono": "123456789",
        "correo": "john.doe@example.com",
        "preferente": True,
        "nif": "12345678A"
    }
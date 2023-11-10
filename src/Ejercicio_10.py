# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su 
# NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, 
# teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un 
# cliente preferente. El programa debe preguntar al usuario por una opción del siguiente 
# menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos 
# los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción 
# elegida el programa tendrá que hacer lo siguiente:

# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la 
# base de datos.

# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.

# 3. Preguntar por el NIF del cliente y mostrar sus datos.

# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.

# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.

# 6. Terminar el programa.

def menu() -> str :
    """
    Muestra el menú del programa y solicita al usuario que seleccione una opción.

    Returns
    -------
    - str:
        Opción seleccionada por el usuario.
    """
    print("\n¿Qué quieres hacer?")
    print("-----------------")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    print("-----------------")
    return input("Selecciona una opción: ")

def anadir_datos(datos_cliente: dict, nombre: str, apellidos: str, direccion: str, telefono: str, correo: str, preferente: bool, nif: str) -> None:
    """
    Añade los datos del cliente al diccionario proporcionado.

    Parameters
    ----------
    - datos_cliente : dict
        Diccionario que almacena los datos del cliente.
    - nombre : str
        Nombre del cliente.
    - apellidos : str
        Apellidos del cliente.
    - direccion : str
        Dirección del cliente.
    - telefono : str
        Número de teléfono del cliente.
    - correo : str
        Correo electrónico del cliente.
    - preferente : bool
        Indica si el cliente es preferente o no.
    - nif : str
        Número de identificación fiscal del cliente.
    """
    datos_cliente["nombre"] = nombre
    datos_cliente["apellidos"] = apellidos
    datos_cliente["direccion"] = direccion
    datos_cliente["telefono"] = telefono
    datos_cliente["correo"] = correo
    datos_cliente["preferente"] = preferente
    datos_cliente["nif"] = nif

def anadir_cliente_base_datos(clientes: dict, nif: str, datos_cliente: dict) -> None:
    """
    Añade al cliente en la base de datos utilizando su NIF como clave.

    Parameters
    ----------
    - clientes : dict
        Base de datos que almacena a los clientes.
    - nif : str
        Número de identificación fiscal del cliente (clave en la base de datos).
    - datos_cliente : dict
        Datos del cliente a ser almacenados en la base de datos.
    """
    clientes[nif] = datos_cliente


def eliminar_cliente(clientes: dict, nif: str) -> None:
    """
    Elimina al cliente de la base de datos utilizando su NIF como clave.

    Parameters:
    - clientes : dict
        Base de datos que almacena a los clientes.
    - nif : str
        Número de identificación fiscal del cliente a ser eliminado.
    """
    del clientes[nif]

if __name__ == "__main__":
    clientes = {}
    opcion = menu
    while opcion != "6":

        if opcion == "1":
            # Entrada
            nombre = input("Escriba su nombre: ")
            apellidos = input("Escriba sus apellidos: ")
            direccion = input("Escriba su direccion: ")
            telefono = input("Escriba su numero de telefono: ")
            correo = input("Escribe su correo electrónico: ")
            preferente = input("¿Es cliente preferente? (True/False): ").lower() == "true"
            nif = input("Escriba su NIF: ")
        
            datos_cliente = {}
            # Procesamiento y salida  
            anadir_datos(datos_cliente, nombre, apellidos, direccion, telefono, correo, preferente, nif)
            anadir_cliente_base_datos(clientes, nif, datos_cliente)
        
        elif opcion == "2":
            # Entrada
            nif = input("Escriba el NIF del cliente que desea eliminar: ")
            # Proceso
            if nif in clientes:
                eliminar_cliente(clientes, nif)
                # Salida 1
                print(f"Cliente con NIF {nif} eliminado.")
            else:
                # Salida 2
                print(f"No se encontró ningún cliente con NIF {nif}.")
        
        elif opcion == "3":
            # Entrada
            nif = input("Escriba el NIF del cliente que desea mostrar: ")
            # Procesamiento
            if nif in clientes:
                # Salida 1
                print(f"Datos del cliente con NIF {nif}:")
                for clave, valor in clientes[nif].items():
                    print(f"{clave}: {valor}")
            else:
                # Salida 2
                print(f"No se encontró ningún cliente con NIF {nif}.")

        elif opcion == "4":
            # Entrada
            print("Lista de todos los clientes:")
            # Proceso
            for nif, datos in clientes.items():
                # Salida 1
                print(f"NIF: {nif}")
                for clave, valor in datos.items():
                    # Salida 1.1
                    print(f"{clave}: {valor}")

        elif opcion == "5":
            # Entrada
            print("Clientes preferentes:")
            # Proceso
            for nif, datos in clientes.items():
                if datos["preferente"]:
                    # Salida 1
                    print(f"NIF: {nif}")
                    for clave, valor in datos.items():
                        # Salida 1.1
                        print(f"{clave}: {valor}")
        
        opcion = menu()
    
    print("Programa terminado. Gracias.")
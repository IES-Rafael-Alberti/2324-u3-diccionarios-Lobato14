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

# Imprime el menu del programa
def menu() -> str :
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

# Funcion que añade los datos del cliente al diccionario
def anadir_datos(datos_cliente, nombre, apellidos, direccion, telefono, correo, preferente, nif):
    datos_cliente["nombre"] = nombre
    datos_cliente["apellidos"] = apellidos
    datos_cliente["direccion"] = direccion
    datos_cliente["telefono"] = telefono
    datos_cliente["correo"] = correo
    datos_cliente["preferente"] = preferente
    datos_cliente["nif"] = nif

# Funcion que añade al cliente en la base datos por su nif
def anadir_cliente_base_datos(clientes, nif, datos_cliente):
    clientes[nif] = datos_cliente

# Funcion que elimina al cliente por su nif
def eliminar_cliente(clientes, nif):
    del clientes[nif]

if __name__ == "__main__":
    clientes = {}
    opcion = menu
    while opcion != "6":

        if opcion == "1":
            
            nombre = input("Escriba su nombre: ")
            apellidos = input("Escriba sus apellidos: ")
            direccion = input("Escriba su direccion: ")
            telefono = input("Escriba su numero de telefono: ")
            correo = input("Escribe su correo electrónico: ")
            preferente = input("¿Es cliente preferente? (True/False): ").lower() == "true"
            nif = input("Escriba su NIF: ")
        
            datos_cliente = {}
            # Añade los datos del cliente  
            anadir_datos(datos_cliente, nombre, apellidos, direccion, telefono, correo, preferente, nif)
            # Añadir el cliente a la base de datos
            anadir_cliente_base_datos(clientes, nif, datos_cliente)
        
        elif opcion == "2":
            nif = input("Escriba el NIF del cliente que desea eliminar: ")
            if nif in clientes:
                eliminar_cliente(clientes, nif)
                print(f"Cliente con NIF {nif} eliminado.")
            else:
                print(f"No se encontró ningún cliente con NIF {nif}.")
        
        elif opcion == "3":
            nif = input("Escriba el NIF del cliente que desea mostrar: ")
            if nif in clientes:
                print(f"Datos del cliente con NIF {nif}:")
                for clave, valor in clientes[nif].items():
                    print(f"{clave}: {valor}")
            else:
                print(f"No se encontró ningún cliente con NIF {nif}.")

        elif opcion == "4":
            print("Lista de todos los clientes:")
            for nif, datos in clientes.items():
                print(f"NIF: {nif}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")

        elif opcion == "5":
            print("Clientes preferentes:")
            for nif, datos in clientes.items():
                if datos["preferente"]:
                    print(f"NIF: {nif}")
                    for clave, valor in datos.items():
                        print(f"{clave}: {valor}")
        
        opcion = menu()
    
    print("Programa terminado. Gracias.")
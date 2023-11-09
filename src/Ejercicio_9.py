# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
# el número de factura y el valor el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si 
# desea añadir una nueva factura se preguntará por el número de factura y su coste y 
# se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número 
# de factura y se eliminará del diccionario. Después de cada operación el programa debe 
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de 
# cobro.

def menu() -> str :
    """Imprime el menu del programa
    """
    print("\n¿Qué quieres hacer?")
    print("1. Añadir nueva factura")
    print("2. Pagar factura existente")
    print("3. Mostrar estado final de las facturas")
    print("4. Terminar el programa")
    return input("Selecciona una opción: ")

def pagar_factura(facturas:dict,num_factura:str) -> bool: 
    """Paga una factura del diccionario de factura

    Parameters
    ----------
    facturas : dict
        La facturas y el estado de estas 
    num_factura : str
        El identificador de la factura a pagar

    Returns
    -------
    bool
        True si se paga correctamente, False si no existe o ya está pagada.
    """
    if num_factura in facturas and facturas[num_factura] > 0:
        facturas[num_factura] = 0
        return True
    else:
        return False

def anadir_factura(facturas:dict, num_factura:str, coste:float) -> float:
    """Añade la factura al diccionario

    Parameters
    ----------
    facturas : dict
        La facturas y el estado de estas 
    num_factura : str
        El identificador de la factura a pagar
    coste:
        El precio de la factura a pagar
    """
    facturas[num_factura] = coste

def estado_final_cobrado(facturas:dict) -> float:
    """Funcion que calcula el total cobrado de las facturas

    Parameters
    ----------
    facturas : dict
        Diccionario en donde se almacenan las facturas

    Returns
    -------
    float
        Se devuelve el total cobrado y el total pendiente
    """
    total_cobrado = sum(facturas.values())
    return total_cobrado

def estado_final_pendiente(facturas:dict) -> float:
    """Funcion que calcula el total pediente de las facturas

    Parameters
    ----------
    facturas : dict
        Diccionario en donde se almacenan las facturas

    Returns
    -------
    float
        Se devuelve el total cobrado
    """
    total_pendiente = sum([valor for valor in facturas.values() if valor > 0])
    return total_pendiente

def leer_numero_desde_consola(mensaje:str)-> float:
    """Lee desde consola, mostrando un mensaje. Repite la lectura hasta que lo introducido sea correcto.

    Parameters
    ----------
    mensaje : str
        El mensaje amostrar en consola.

    Returns
    -------
    float
        un numero flotante
    """
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            numero = float(input(mensaje))
            numeroCorrecto = True
        except:
            pass
    return numero

if __name__ == "__main__":

    facturas = {}
    opcion = menu()
    while opcion != "4":
        
        if opcion == "1":
            # Entrada
            num_factura = input("Introduce el número de factura: ")
            coste = leer_numero_desde_consola("Introduce el coste de la factura: ")
            # Proceso
            anadir_factura(facturas, num_factura, coste)
            # Salida
            print("Factura añadida correctamente.")

        elif opcion == "2":
            # Entrada
            num_factura = input("Introduce el número de factura que deseas pagar: ")
            # Proceso
            realizacion_factura = pagar_factura(facturas, num_factura)
            # Salida
            print(realizacion_factura)

        elif opcion == "3":
            # Entrada
            print("Estado final de las facturas:")
            # Proceso
            total_cobrado = estado_final_cobrado(facturas)
            total_pendiente = estado_final_pendiente(facturas)
            # Salida
            print("Cantidad cobrada hasta el momento: ", total_cobrado)
            print("Cantidad pendiente de cobro: ", total_pendiente)

        else:
            # Salida
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        opcion = menu()
    # Salida
    print("Programa Terminado. Hasta la proxima")
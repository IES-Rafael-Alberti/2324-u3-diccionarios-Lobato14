# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
# el número de factura y el valor el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si 
# desea añadir una nueva factura se preguntará por el número de factura y su coste y 
# se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número 
# de factura y se eliminará del diccionario. Después de cada operación el programa debe 
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de 
# cobro.

# Imprime el menu del programa
def menu() -> str :
    print("\n¿Qué quieres hacer?")
    print("1. Añadir nueva factura")
    print("2. Pagar factura existente")
    print("3. Mostrar estado final de las facturas")
    print("4. Terminar el programa")
    return input("Selecciona una opción: ")

# Función que verifica y paga una factura del diccionario de factura
def factura_a_pagar(facturas,num_factura):
    if num_factura in facturas and facturas[num_factura] > 0:
        facturas[num_factura] = 0
        return "Factura pagada correctamente."
    else:
        return "Factura no encontrada o ya pagada."

# Añade la factura al diccionario
def anadir_factura(facturas, num_factura, coste):
    facturas[num_factura] = coste

# Funcion que calcula el total cobrado y el pediente de las facturas
def estado_final(facturas):
    total_cobrado = sum(facturas.values())
    total_pendiente = sum([valor for valor in facturas.values() if valor > 0])
    return total_cobrado, total_pendiente

if __name__ == "__main__":

    facturas = {}
    opcion = menu()
    while opcion != "4":
        
        if opcion == "1":
            # Entrada
            num_factura = input("Introduce el número de factura: ")
            coste = float(input("Introduce el coste de la factura: "))
            # Proceso
            anadir_factura(facturas, num_factura, coste)
            # Salida
            print("Factura añadida correctamente.")

        elif opcion == "2":
            # Entrada
            num_factura = input("Introduce el número de factura que deseas pagar: ")
            # Proceso
            realizacion_factura = factura_a_pagar(facturas, num_factura)
            # Salida
            print(realizacion_factura)

        elif opcion == "3":
            # Entrada
            print("Estado final de las facturas:")
            # Proceso
            total_cobrado, total_pendiente = estado_final(facturas)
            # Salida
            print("Cantidad cobrada hasta el momento: ", total_cobrado)
            print("Cantidad pendiente de cobro: ", total_pendiente)

        else:
            # Salida
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        opcion = menu()
    # Salida
    print("Programa Terminado. Hasta la proxima")
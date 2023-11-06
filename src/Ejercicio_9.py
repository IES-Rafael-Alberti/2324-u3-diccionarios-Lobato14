# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
# el número de factura y el valor el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si 
# desea añadir una nueva factura se preguntará por el número de factura y su coste y 
# se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número 
# de factura y se eliminará del diccionario. Después de cada operación el programa debe 
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de 
# cobro.

def main():
    facturas = {}
    opcion = ""
    while opcion != "3":
        print("\n¿Qué quieres hacer?")
        print("1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Terminar")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            num_factura = input("Introduce el número de factura: ")
            coste = float(input("Introduce el coste de la factura: "))
            facturas[num_factura] = coste
            print("Factura añadida correctamente.")

        elif opcion == "2":
            num_factura = input("Introduce el número de factura que deseas pagar: ")
            if num_factura in facturas and facturas[num_factura] > 0:
                facturas[num_factura] = 0
                print("Factura pagada correctamente.")
            else:
                print("Factura no encontrada o ya pagada.")

        elif opcion == "3":
            print("Estado final de las facturas:")
            total_cobrado = sum(facturas.values())
            total_pendiente = sum([valor for valor in facturas.values() if valor > 0])
            print("Cantidad cobrada hasta el momento: ", total_cobrado)
            print("Cantidad pendiente de cobro: ", total_pendiente)

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
# Escribir un programa que guarde en un diccionario los precios de las frutas 
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
# por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en 
# el diccionario debe mostrar un mensaje informando de ello.

#    Fruta	        Precio
#   Plátano	         1.35
#   Manzana	         0.80
#   Pera	         0.85
#   Naranja	         0.70

# Funcion que calcula el precio segun los kilos de fruta
def calcular_precio(fruta, kilos, diccionario_frutas):
    if fruta in diccionario_frutas and kilos >= 0:
        precio_total = kilos * diccionario_frutas[fruta]
        return precio_total
    else:
        return None
    
if __name__ == "__main__":
    # Entrada
    dicFrutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = input("Escoja una fruta: ")
    # Proceso
    while fruta not in dicFrutas:
        print("La fruta seleccionada no está en el diccionario.")
        fruta = input("Escoja una fruta: ")

    kilos_validos = False
    while not kilos_validos:
        kilos = input("¿Cuántos kilos quieres?: ")
        if kilos.replace(".", "").isdigit() and float(kilos) >= 0:
            kilos = float(kilos)
            kilos_validos = True
        else:
            print("Por favor, ingrese un número positivo para los kilos.")

    precio_total = calcular_precio(fruta, kilos, dicFrutas)
    # Salida
    if precio_total is not None:
        print("El precio final de", kilos, "kilos de", fruta, "es de", round(precio_total,2))
    else:
        print("Ha ocurrido un error al calcular el precio.")
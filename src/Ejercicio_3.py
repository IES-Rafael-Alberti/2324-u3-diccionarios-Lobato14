# Escribir un programa que guarde en un diccionario los precios de las frutas 
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
# por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en 
# el diccionario debe mostrar un mensaje informando de ello.

#    Fruta	        Precio
#   Plátano	         1.35
#   Manzana	         0.80
#   Pera	         0.85
#   Naranja	         0.70

if __name__ == "__main__":
    dicFrutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    fruta = input("Escoja una fruta: ")
    if fruta in dicFrutas:
        kilos = float(input("¿Cuantos kilos quieres?: "))
        precio_total = kilos * dicFrutas[fruta]
        print(f"El precio final de {kilos} kilos de {fruta} es de {precio_total:.2f}")
    else:
        print("La fruta seleccionada no está en el diccionario.")
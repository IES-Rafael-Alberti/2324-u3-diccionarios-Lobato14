# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
# de la compra y el coste total, con el siguiente formato

    # Lista de la compra

    # Artículo 1	Precio
    # Artículo 2	Precio
    # Artículo 3	Precio
    #   …	…
    # Total	Coste

def agregar_producto(listaCompra, contador):
    articulo = input(f"Escriba el artículo {contador} a comprar: ")
    precio_valido = False
    while not precio_valido:
        precio = input("Escriba su precio correspondiente: ")
        if precio.replace('.', '', 1).isdigit() and float(precio) > 0:
            precio_valido = True
            listaCompra[articulo] = float(precio)
        else:
            print("Precio inválido. Debe ingresar un número positivo.")
        

def mostrar_lista_compra(listaCompra):
    resultado = []
    resultado.append("\nLista de la compra\n")
    total = 0
    for articulo, precio in listaCompra.items():
        resultado.append(f"{articulo} \t Precio: {precio}")
        total += precio
    resultado.append(f"\nTotal \t\t Coste: {total}") 
    return resultado

if __name__ == "__main__":
    # Entrada
    listaCompra = {}
    continuar_agregando = "si"
    contador = 1
    # Proceso
    while continuar_agregando.lower() == "si":
        agregar_producto(listaCompra, contador)
        continuar_agregando = input("¿Deseas añadir un nuevo producto? (si/no): ")
        contador += 1
    
    listaResultado = mostrar_lista_compra(listaCompra)
    # Salida
    print(listaResultado)
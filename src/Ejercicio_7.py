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

def mostrar_lista_compra(listaCompra:dict) -> str:
    """
    Muestra la lista de la compra con los nombres de los artículos y sus respectivos precios.

    Parameters
    ----------
    
    - listaCompra : dict 
        Diccionario que contiene los artículos de la lista de compra y sus precios.

    Returns
    -------

    str: Cadena de texto que representa la lista de la compra junto con el total del coste.
    """
    print("\nLista de la compra\n")
    total = 0
    for articulo, precio in listaCompra.items():
        print(f"{articulo} \t Precio: {precio}")
        total += precio
    return f"\nTotal \t\t Coste: {total}"

def anadir_prod(listaCompra:dict, articulo:str, precio:str):
    """
    Añade un producto a la lista de la compra con su respectivo precio.

    Parameters
    ----------
    - listaCompra : dict
        Diccionario que representa la lista de la compra.
    - articulo : str 
        Nombre del artículo a añadir.
    - precio : str: 
        Precio del artículo a añadir.

    Returns
    --------

    - None: 
        No devuelve ningún valor. Modifica la lista de la compra si la entrada es válida.
    """
    if precio.replace('.', '', 1).isdigit() and float(precio) > 0:
        listaCompra[articulo] = float(precio)
    else:
        print("Precio inválido. Debe ingresar un número positivo.")


if __name__ == "__main__":
    # Entrada
    listaCompra = {}
    continuar_agregando = "si"
    contador = 1
    # Proceso
    while continuar_agregando.lower() != "no":
        articulo = input(f"Escriba el artículo {contador} a comprar: ")
        precio = input("Escriba su precio correspondiente: ")
        anadir_prod(listaCompra, articulo, precio)
        continuar_agregando = input("¿Deseas añadir un nuevo producto? (si/no): ")
        contador += 1
    
    listaResultado = mostrar_lista_compra(listaCompra)
    # Salida
    print(listaResultado)
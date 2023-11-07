# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':
# '$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje 
# de aviso si la divisa no está en el diccionario.

# Funcion que busca si dicha divisa está o no en el diccionario.
def buscarDiccionarioMonetario(diccionarioMonetario, divisa):
    if divisa not in diccionarioMonetario:
        return "La divisa no se encuentra en el diccionario"
    else:
        return "El símbolo de la divisa " + divisa + " es " + diccionarioMonetario[divisa]

if __name__ == "__main__":
    # Entrada
    diccionarioMonetario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    divisa = input("Escribe una divisa: ")
    # Procesamiento
    resultadoDivisa = buscarDiccionarioMonetario(diccionarioMonetario, divisa)
    # Salida
    print(resultadoDivisa)
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
# lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
# tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def validar_edad(edad:int) -> int:
    """ Función que valida la edad introducida

    Parameters
    ----------
    edad : int
        Edad introducida por el usuario

    Returns
    -------
    int:
        Devuelve la edad si es digito o si la edad el mayor o igual a 0
    
    """
    return edad.isdigit() and int(edad) >= 0

def validar_telefono(telefono:str) -> bool:
    """ Funcion que valida el numero de telefono introducido

    Parameters
    ----------
    telefono : str
        Número de telefono introducido por el usuario

    Returns
    -------
    int:
        Devuelve un número entero si es digito y si la longitud del telefono es igual a 10
    
    """
    return telefono.isdigit() and len(telefono) == 9

def mostrar_mensaje(datosUser:dict) -> str:
    """ Funcion que muestra el mensaje de los datos del usuario

    Parameters
    ----------
    datosUser : dict
        Diccionario en donde se almacenan los datos del usuario

    Returns
    -------
    str:
        Devuelve el mensaje introducido en la variable "mensaje" 
    
    """
    mensaje = f"{datosUser['nombre']} tiene {datosUser['edad']} años, vive en {datosUser['direccion']} y su número de teléfono es {datosUser['telefono']}"
    return mensaje

if __name__ == "__main__":
    # Entrada
    datosUser = {}
    nombre = input("Escriba su nombre: ")
    datosUser["nombre"] = nombre
    edad_valida = False
    while not edad_valida:
        edad = input("Escriba su edad: ")
        if validar_edad(edad):
            datosUser["edad"] = int(edad)
            edad_valida = True
        else:
            print("Edad inválida. Debe ingresar un número entero positivo.")
    direccion = input("Escriba su dirección: ")
    datosUser["direccion"] = direccion
    telefono_valido = False
    while not telefono_valido:
        telefono = input("Escriba su número de teléfono: ")
        if validar_telefono(telefono):
            datosUser["telefono"] = telefono
            telefono_valido = True
        else:
            print("Número de teléfono inválido. Intente nuevamente.")
    # Proceso
    resultMensaje = mostrar_mensaje(datosUser)
    # Salida
    print(resultMensaje)
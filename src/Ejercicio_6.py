# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
# contenido del diccionario.

def validar_edad(edad:int) -> int:
    """
    Funcion que valida la edad introducida

    Parameters
    ----------
    edad : int
       Edad a introducir por teclado
                                 

    Returns
    -------
    int: 
        Devuelve la edad si es digito y si la edad es mayor o igual que 0
    """
    return edad.isdigit() and int(edad) >= 0

def validar_telefono(telefono:str) -> int:
    """
    Funcion que valida el telefono introducido

    Parameters
    ----------
    telefono : str
       Numero de telefono introducido por teclado
                                 

    Returns
    -------
    int: 
        Devuelve el telefonono si es digito
    """
    return telefono.isdigit()

def imprimir_lista_usuarios(usuarios):
    """
    Imprime la lista de usuarios.

    Parameters
    -----------

    - usuarios (list): Lista de usuarios a imprimir.

    Returns
    -------
    None
    """
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(usuario)
    print()

if __name__ == "__main__":
    # Entrada
    datosUsuarios = []
    agregar_usuario = "si"
    # Proceso
    while agregar_usuario.lower() == "si":
        
        datosPersona = {}
        nombre = input("Escriba su nombre: ")
        datosPersona["nombre"] = nombre
        apellidos = input("Escriba sus apellidos: ")
        datosPersona["apellidos"] = apellidos
        
        edad_valida = False
        while not edad_valida:
            edad = input("Escriba su edad: ")
            if validar_edad(edad):
                datosPersona["edad"] = int(edad)
                edad_valida = True
            else:
                print("Edad inválida. Debe ingresar un número entero positivo.")
        
        sexo = input("Escriba su sexo: ")
        datosPersona["sexo"] = sexo
        
        telefono_valido = False
        while not telefono_valido:
            telefono = input("Escriba su número de teléfono: ")
            if validar_telefono(telefono):
                datosPersona["telefono"] = telefono
                telefono_valido = True
            else:
                print("Número de teléfono inválido. Intente nuevamente.")

        datosUsuarios.append(datosPersona)
        print("Usuario añadido:", datosPersona)
        
        agregar_usuario = input("¿Deseas añadir un nuevo usuario? (si/no): ")
    # Salida
    imprimir_lista_usuarios(datosUsuarios)
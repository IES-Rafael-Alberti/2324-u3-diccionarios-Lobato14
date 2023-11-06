# Escribir un programa que almacene el diccionario con los créditos de las asignaturas 
# de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla 
# los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus 
# créditos. Al final debe mostrar también el número total de créditos del curso.

def mostrar_creditos(creditos_asignaturas):
    mensaje = ""
    for asignatura, creditos in creditos_asignaturas.items():
        mensaje += asignatura + " tiene " + str(creditos) + " créditos.\n"
    return mensaje

def calcular_total_creditos(creditos_asignaturas):
    return sum(creditos_asignaturas.values())

if __name__ == "__main__":
    # Entrada
    creditos_asig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    # Proceso
    mensaje_creditos = mostrar_creditos(creditos_asig)
    total_creditos = calcular_total_creditos(creditos_asig)
    # Salida
    print(mensaje_creditos)
    print("El número total de créditos del curso es:", total_creditos)
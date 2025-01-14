def arithmetic_arranger(problems, show_answers=False):

    # Verificando que el maximo de operaciones sea menor a 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # Creamos las listas para meter los resultados
    fila_superior = []
    fila_inferior = []
    lineas = []
    resultados = []

    for problema in problems:
        # Separamos las expresiones de los strings en 3 partes, Primer Numero, Operador y Segundo Numero
        numero_izquierda, operador, numero_derecha = problema.split(" ")
        
        # Validamos los operadores para que sean + o -
        if operador != "+" and operador != "-":
            return "Error: Operator must be '+' or '-'."
        
        # Validamos los numeros para que solo contengan numeros
        if (numero_izquierda.isdigit() == False or numero_derecha.isdigit() == False):
            return "Error: Numbers must only contain digits."
        
        # Validamos la longitud de los numeros para que sean menores a 4 digitos
        if len(numero_izquierda) > 4 or len(numero_derecha) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Realizamos Operacion
        if operador == '+':
            resultado = str(int(numero_izquierda) + int(numero_derecha))
        else:
            resultado = str(int(numero_izquierda) - int(numero_derecha))
        
        # Calculamos longitud maxima para alinear los numeros
        longitud_maxima = max(len(numero_izquierda), len(numero_derecha)) +2

        # Añadir las filas
        fila_superior.append(f"{numero_izquierda:>{longitud_maxima}}")
        fila_inferior.append(f"{operador} {numero_derecha:>{longitud_maxima - 2}}")
        lineas.append('-' * longitud_maxima)
        resultados.append(f"{resultado:>{longitud_maxima}}")

    # Unir las filas en un solo resultado
    problemas_arreglados = ['    '.join(fila_superior),
                         '    '.join(fila_inferior),
                         '    '.join(lineas)]
    
    # Si show_answers es True agregamos la fila de los resultados
    if show_answers:
        problemas_arreglados.append('    '.join(resultados))

    return '\n'.join(problemas_arreglados)

# Ejemplo:

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49","123 - 49"]
print(arithmetic_arranger(problems, show_answers=True))
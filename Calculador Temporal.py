def add_time(inicio, duracion, dia_inicio=None):

    # Analizar la hora de inicio

    hora_inicio, periodo_inicio = inicio.split()  
    # Dividir la hora y el periodo (AM/PM)

    hora_inicio, minuto_inicio = map(int, hora_inicio.split(':'))  
    # Convertir a enteros la hora y minuto

    # Ajustar la hora a formato de 24 horas
    if periodo_inicio.lower() == 'pm' and hora_inicio != 12:
        hora_inicio += 12  # Convertir a formato de 24 horas si es PM
    elif periodo_inicio.lower() == 'am' and hora_inicio == 12:
        hora_inicio = 0  # Convertir la medianoche a 00 horas

    # Analizar la duración
    hora_duracion, minuto_duracion = map(int, duracion.split(':'))  
    # Convertir la duración en horas y minutos

    # Sumar la duración a la hora de inicio
    minutos_totales = hora_inicio * 60 + minuto_inicio + hora_duracion * 60 + minuto_duracion
    hora_resultado = (minutos_totales // 60) % 24  
    # Calcular la hora resultante
    minuto_resultado = minutos_totales % 60  
    # Calcular los minutos resultantes
    dias_later = minutos_totales // (60 * 24)  
    # Calcular cuántos días después es el resultado

    # Determinar el periodo (AM/PM) de la hora resultante
    if hora_resultado >= 12:
        periodo_resultado = 'PM'
        if hora_resultado > 12:
            hora_resultado -= 12  # Convertir a formato de 12 horas
    else:
        periodo_resultado = 'AM'
        if hora_resultado == 0:
            hora_resultado = 12  # Convertir 00 a 12 para formato AM

    # Determinar el día de la semana, si se pasa como parametro
    if dia_inicio:
        dias_semana = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        dia_inicio = dia_inicio.lower()  
        # Convertir a minúsculas para hacer la búsqueda mas eficiente
        indice_dia_inicio = dias_semana.index(dia_inicio)  
        # Encontrar el índice del día de inicio
        indice_dia_resultado = (indice_dia_inicio + dias_later) % 7  
        # Calcular el día resultante
        dia_resultado = dias_semana[indice_dia_resultado].capitalize()  
        # Obtener el nombre del día con mayúscula al inicio
        parte_dia = f", {dia_resultado}"
    else:
        parte_dia = ""  
        # Si no se indica día, no agregar nada al resultado

    # Formatear la hora resultante
    hora_formateada = f"{hora_resultado}:{str(minuto_resultado).zfill(2)} {periodo_resultado}"

    # Si no hay días adicionales, devolver solo la hora
    if dias_later == 0:
        return f"{hora_formateada}{parte_dia}"
    # Si es un día adicional, agregar "(next day)"
    elif dias_later == 1:
        return f"{hora_formateada}{parte_dia} (next day)"
    # Si son varios días, agregar el número de días
    else:
        return f"{hora_formateada}{parte_dia} ({dias_later} days later)"
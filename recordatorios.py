# * my_recordatorios v1 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d12-EstrDatosFunc-DF-Estructuras1-byCesarAguas-v1/LICENSE)
# 
#
#   Tabla de recordatorios
#Se provee del archivo recordatorios.py que incluye una serie de eventos que
#quieren ser recordados por usted. El formato de estos recordatorios son:
#fecha(año-mes-día), hora , descripción del evento.

#Aplicando métodos apropiados para la estructura de datos entregada 
#edite la lista de recordatorios de la siguiente manera:

#Los eventos deben siempre editarse de tal manera que mantengan su orden en el tiempo. 
#Y el código debe ejecutarse en el orden entregado en las instrucciones dadas a continuación:
#1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
#2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
#3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo.
#4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a ppplas 22 hrs.

#   Eventos anteriormente agendados
recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"]
]

#   Definiendo funciones necesarias
#
#   Funcion para agregar eventos a la agenda (lista)
def add_e(agenda, fecha, hora, descripcion):
    evento = [fecha, hora, descripcion]
    agenda.append(evento)
    agenda.sort()    # Ordenar
    return agenda

#   Funcion para actualizar eventos
def up_date(agenda, fecha, nueva_fecha):
    for evento in agenda:
        if evento[0] == fecha:
            evento[0] = nueva_fecha
    agenda.sort()    # Ordenar
    return agenda

#   Funcion para remover eventos
def rem_e(agenda, descripcion):
    #print(descripcion)
    #Este ciclo vuelve a crear la lista con todos los eventos que NO coincidan con la descripcion.
    #                           [indexOf 0, indexOf 1, indexOf 2]
    #                       ['2021-05-01', "15:00", "No trabajar"]
    agenda = [evento for evento in agenda if evento[2] != descripcion]
    return agenda



# Comenzando las rutinas

#Ejecutando funciones y mostrando modificaciones de la lista

#   Actualizacion de eventos para recordar
#   Mostrar antiguos
print("Mostar registros antiguos de la agenda:")
print(recordatorios)
print()
print()

#   Actualizacion de eventos para recordar
print("Se comienza a agregar eventos a la agenda: ['2021-02-02', '06:00', 'Empezar el año']")
agendados = add_e(recordatorios, '2021-02-02', '06:00', 'Empezar el año')
print(agendados)
print()
print()

#   Actualizacion de fechas
print("Actualizacion de fechas de un evento determinado: ['2021-07-16', '13:00', 'No hacer nada es feriado']")
agendados = up_date(recordatorios, '2021-07-15', '2021-07-16')
print(agendados)
print()
print()

#   Remover un registro
print("Se necesita eliminar un registro: 'No trabajar'")
agendados = rem_e(recordatorios, 'No trabajar')
print(agendados)
print()
print()

#   Actualizacion de eventos para recordar
print("Se agrega otro evento a la agenda: ['2021-12-24', '22:00', 'Cena de Navidad']")
agendados = add_e(recordatorios, '2021-12-24', '22:00', 'Cena de Navidad')
print(agendados)
print()
print()

#   Actualizacion de eventos para recordar
print("Se agrega otro evento a la agenda: ['2021-12-25', '00:00', 'Navidad']")
agendados = add_e(recordatorios, '2021-12-25', '00:00', 'Navidad')
print(agendados)
print()
print()

#   Actualizacion de eventos para recordar
print("Se agrega otro evento a la agenda: ['2021-12-31', '22:00', 'Cena de Año Nuevo']")
agendados = add_e(recordatorios, '2021-12-31', '22:00', 'Cena de Año Nuevo')
print(agendados)
print()
print()




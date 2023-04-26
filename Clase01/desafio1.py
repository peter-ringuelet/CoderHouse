partidos_ganados = int(input('Ingrese cantidad de partidos ganados: '))
partidos_empatados = int(input('Ingrese cantidad de partidos empatados: '))
partidos_perdidos = int(input('Ingrese cantidad de partidos perdidos: '))

puntos = (partidos_ganados * 3) + (partidos_empatados) 
partidos_totales = partidos_ganados + partidos_empatados + partidos_perdidos
promedio = puntos / partidos_totales

print(promedio)
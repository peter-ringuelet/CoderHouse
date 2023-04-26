cadena = input('Ingrese nombre, apellido, nota y materia(Ej: Pedro Ringuelet, 10, Matematica): ')     #1
cadena_volteada =   cadena[::-1]                     
print(cadena_volteada)

nombre_alumno = cadena.split(', ')[0]       #2
print(nombre_alumno)

nota = cadena.split(', ')[1]        #3
print(nota)

materia = cadena.split(', ')[2]     #4
print(materia)

estructura = nombre_alumno + ' ha sacado un ' + nota + ' en ' + materia     #5
print(estructura)

cadena_formateada = ("{0}, {1}, {2}".format(nombre_alumno, nota, materia))     #6
print(cadena_formateada)
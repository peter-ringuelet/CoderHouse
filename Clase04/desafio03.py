nombre = input('Ingrese su nombre: ').title()
preferencia = input('Ingrese su preferencia(Marvel o Capcom): ').title()

if (preferencia == 'Marvel') and (nombre[0] < 'M') or (preferencia == 'Capcom') and (nombre[0] > 'N'):
    print('Ha sido asignado al grupo "A".')
else:
    print('Ha sido asignado al grupo "B".')

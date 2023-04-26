edad = 15
antigüedad = 3
ingreso = 2500
aprobado = False

if (edad >= 18):
    if (antigüedad >= 3) and (ingreso > 2500):
        aprobado = True
    elif ingreso >= 4000:
        aprobado = True

if aprobado:
    print('Se ha aprobado el credito.')
else:
    print('No se ha aprobado el credito.')
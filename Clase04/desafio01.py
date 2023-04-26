year = int(input('Ingrese anio de nacimiento: '))

if ((year >= 1920) and (year <= 1940)):
    print('Generacion Silenciosa')
elif ((year >= 1946) and (year <= 1964)):
    print('Baby Boomer')
elif ((year >= 1965) and (year <= 1979)):
    print('Generacion X')
elif (year>=1980 and year<=2000):
    print('Generacion Y')
elif (year>=2001 and year>=2010):
    print('Generacion Z')
else:
    print('No existe generacion asociada')

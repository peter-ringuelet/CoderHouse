expresiones = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]

resultado =[
    True,
    True,
    True,
    True,
    True,
    False
]

print(expresiones)
print(resultado)
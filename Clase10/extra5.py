def recortar(num,limite_inferior,limite_superior):
    if num < limite_inferior:
        return limite_inferior
    elif num > limite_superior:
        return limite_superior
    else:
        return num

print(recortar(15,0,10)) 
def relacion(num1,num2):
    if (num1 > num2):
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

def dividir(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return "No se puede divisir por 0"
    except Exception as ex:
        print('algo')

a = 1
b = 'd'
print(dividir(a,b))
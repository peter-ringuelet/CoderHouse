def conversion(*args):
    if (len(args) == 1):
        metros = args[0] / 1000
        centimetros = args[0] / 100
        return(f"{metros}m, {centimetros}cm , {args[0]}mm ")
    elif(len(args) == 3):
        mm1 = args[0] * 1000
        mm2 = args[1] * 10
        return(f"{args[0]}m son {mm1} milimetros. {args[1]}cm son {mm2} milimetros. {args[2]}mm son {args[2]} milimetros")
    return ("No se han ingresado ni 1 ni 3 argumentos")

num1 = int(input("Ingrese un numero(m): "))
num2 = int(input("Ingrese un numero(cm): "))
num3 = int(input("Ingrese un numero(mm): "))
print(conversion(num1,num2,num3))


num = int(input("Ingrese un numero(mm): "))
print(conversion(num))

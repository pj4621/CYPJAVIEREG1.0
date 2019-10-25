num = float(input("Ingresa un valor positivo: "))
if num > 0:
    while num !=1:
        print("Los valores son: ",num)
        if ((-1) ** num) > 0:
            num = num / 2
        else:
            num = (num *3) + 1
else:
    print("El numero ingresado tiene que ser positivo")
print("A qui termina el ciclo",num)


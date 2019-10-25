may = -100000
men = 100000
n = int(input("Dame la cantidad de datos que se van a ingresar: "))
for i in range(n,0,-1):
    num = int(input("Ingrese un valor numerico positivo: "))
    if num > may:
        may = num
    elif num < men:
        men = num
print("El valor maximo ingresado es:",may)
print("El valor minimo ingresado es:",men)

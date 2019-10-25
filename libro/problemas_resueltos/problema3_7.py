med = 0
chi = 0
gra = 0
n = int(input("Cual fue el numero de ventas realizadas: "))
for i in range(n,0,-1):
    v = float(input("Ingres el valor de venta: " ))
    if v <= 200:
        chi += 1
    elif v < 400:
        med += 1
    else:
        gra +=1
print("El numero de ventas menores o igual a $200 es =",chi)
print("El numero de ventas mayor a $200 pero menos de $400 es =",med)
print("El numero de ventas mayores a $400 es =",gra)

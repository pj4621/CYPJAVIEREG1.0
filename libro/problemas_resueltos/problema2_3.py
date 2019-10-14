A = float(input("Dame un valor numerico: "))
B = float(input("Dame un valor numerico: "))
C = float(input("Dame un valor numerico: "))
Dis = B**2-4*A*C
if Dis >= 0:
    X1 = ((-B)+ Dis**0.5) /(2*A)
    X2 = ((-B)- Dis**0.5) /(2*A)
    print(f"La Raizes reales son igula a {X1} y {X2}")
    print(Dis)
else:
    print("Fin del programa")


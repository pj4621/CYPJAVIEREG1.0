P = int(input("Dame un valor entero: "))
Q = int(input("Dame un valor entero: "))
EXP = P**3 +Q**4 -2*P**2
if EXP < 680:
    print(f"El valor de P es igula a {P} y el valor de Q es igual a {Q}")
    print(f"El valor total de P y Q es igual a {EXP}")
else:
    print("Fin del Programa")



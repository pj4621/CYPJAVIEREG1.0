nom = 0
suei = bool(int(input("Hay mas sueldos de trabajadores(0 no,1 si): ")))
while(suei == True):
    sue = float(input("Dame el sueldo del trabajador: "))
    if sue < 1000:
        nsue = sue * 1.15
        nom = nom + nsue
    else:
        nsue = sue * 1.12
        nom = nom + nsue
    suei = bool(int(input("Hay mas sueldos de trabajadores(0 no,1 si): ")))
    print("El nuevo sueldo del trabajador es de $",nsue)
print("El sueldo acumulado de todos los trabajadores es de $",nom)

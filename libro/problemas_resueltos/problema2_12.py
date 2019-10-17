Sue = int(input("Caual es el sueldo del trabajador?: "))
Cat = int(input("Cual es la categoria del trabajador?: "))
HE = int(input("Cuantas horas extra trabajo?: "))
if Cat == 1:
    PHE = 30
    if HE > 30:
        Nsue = Sue + (30 * PHE)
        print(f"El sueldo total es de ${Nsue}")
    else:
        Nsue = Sue + (HE * PHE)
        print(f"El sueldo total es de ${Nsue}")
elif Cat == 2:
    PHE = 38
    if HE > 30:
         Nsue = Sue + (30 * PHE)
         print(f"El sueldo total es de ${Nsue}")
    else:
         Nsue = Sue + (HE * PHE)
         print(f"El sueldo total es de ${Nsue}")
elif Cat == 3:
    PHE = 50
    if HE > 30:
        Nsue = Sue + (30 * PHE)
        print(f"El sueldo total es de ${Nsue}")
    else:
        Nsue = Sue + (HE * PHE)
        print(f"El sueldo total es de ${Nsue}")
elif Cat == 4:
    PHE = 70
    if HE > 30:
        Nsue = Sue + (30 * PHE)
        print(f"El sueldo total es de ${Nsue}")
    else:
        Nsue = Sue + (HE * PHE)
        print(f"El sueldo total es de ${Nsue}")
elif Cat == 5:
    PHE = 0
    if HE > 30:
        Nsue = Sue + (30 * PHE)
        print(f"El sueldo total es de ${Nsue}")
    else:
        Nsue = Sue + HE * PHE
        print(f"El sueldo total es de ${Nsue}")
elif Cat == 6:
     PHE = 0
     if HE > 30:
         Nsue = Sue + (30 * PHE)
         print(f"El sueldo total es de ${Nsue}")
     else:
         Nsue = Sue + HE * PHE
         print(f"El sueldo total es de ${Nsue}")
elif Cat == 8:
    PHE = 0
    if HE > 30:
        Nsue = Sue + (30 * PHE)
        print(f"El sueldo total es de ${Nsue}")
    else:
        Nsue = Sue + HE * PHE
        print(f"El sueldo total es de ${Nsue}")

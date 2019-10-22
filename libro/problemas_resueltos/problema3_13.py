Arsu = 0
Mersu =50000
Mes = 0
Arno = 0
Arce = 0
for i in range(1,13,1):
    print(f"Mes { i }")
    Rno = int(input("Promedio de lluvias del mes zona norte:"))
    Rce = int(input("Promedio de lluvias del mes zona centro:"))
    Rsu = int(input("Promedio de lluvias del mes de zona sur:"))

    Arno = Arno + Rno
    Arce = Arce + Rce
    Arsu = Arsu + Rsu

    if Rsu < Mersu:
          Mersu = Rsu
          Mes = i
Prorce = Arce / 12
print(f"Promedio region centro:{Prorce}")
print(f"Mes con menor lluvia en region sur:{Mes}")
print(f"Registro del mes con menor lluvia es : {Mes}")
if Arno > Arce:
    if Arno > Arsu:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif Arce > Arsu :
    print("La region mayores lluvias es la region centro")
else:
    print("La region con mayores lluvias es la region sur")
    

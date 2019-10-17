Tip = int(input("Cual es el tipo de enfermedad?: "))
Edad = int(input("Cual es la edad del pasiente?: "))
Dia = int(input("Cuantos dias estubo Hospitalizado?: "))
if Tip == 1:
    Cos1 = Dia * 25
elif Tip == 2:
    Cos1 = Dia * 16
elif Tip == 3:
    Cos1 = Dia * 20
elif Tip == 4:
    Cos1 = Dia * 32
if Edad >= 14 and Edad <= 22:
    Cos1 = Cos1 * 1.10
else:
    print(f"El costo total es {Cos1}")
print(f"El costo total es {Cos1}")

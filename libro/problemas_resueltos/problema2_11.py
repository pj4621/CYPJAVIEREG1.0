Clav = int(input("Ingresa la clave de la zona?: "))
Num = int(input("Numero de minutos Hablados?: "))
if Clav == 12:
    Cos = Num * 2
    print(f"El costo total de la llamada es de ${Cos}")
elif Clav == 15:
    Cos = Num * 2.2
    print(f"El costo total de la llamada es de ${Cos}")
elif Clav == 18:
    Cos = Num * 4.5
    print(f"El costo total de la llamada es de ${Cos}")
elif Clav == 19:
    Cos = Num * 3.5
    print(f"El costo total de la llamada es de ${Cos}")
elif Clav == 23 and 25:
    Cos = Num * 6
    print(f"El costo total de la llamada es de ${Cos}")
elif Clav == 29:
    Cos = Num * 5
    print(f"EL costo total de la llamada es de ${Cos}")




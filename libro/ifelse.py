edad = int(input("Dame tu edad:"))
INE = bool(int(input("Tienes INE (0 No / 1 si)?:")))
if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puedes entrar al bar")
else:
    print("Eres mayor de edad")
    print("Puedes ir a jugar Lol")
print("Fin del programa")

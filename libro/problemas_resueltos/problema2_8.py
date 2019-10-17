Com = float(input("Cual es el monto de compra?: "))
if Com < 500 :
    print(f"La compra total es de ${Com} por lo cula debe pagar ${Com}")
elif Com <= 1000:
    Com1 = Com - (Com * .05)
    print(f"La compra total es de ${Com} por lo cual debe pagar ${Com1}")
elif Com <= 7000:
    Com1 = Com - (Com * .11)
    print(f"La compra es de ${Com} por lo cual debe pagar ${Com1}")
elif Com <= 15000:
     Com1 = Com - (Com * .18)
     print(f"La compra es de ${Com} por lo cual debe pagar ${Com1}")
else:
    Com1 = Com - (Com * .25)
    print(f"La compra es de ${Com} por lo cual debe pagar ${Com1}")

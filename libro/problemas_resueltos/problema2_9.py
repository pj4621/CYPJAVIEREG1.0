Preb = float(input("Cual es el valor del producto?:"))
if Preb > 500:
    Imp = 20 * .30 + (Preb-40) * .50
    PreTt = Preb + Imp
    print(f"El precio Basico del producto es de ${Preb}")
    print(f"El precio total del producto es de ${PreTt}")
elif Preb > 40:
    Imp = 20 * .30 + (Preb-40) * .40
    PreTt = Preb + Imp
    print(f"El precio Basico del producto es de ${Preb}")
    print(f"El precio total del producto es de ${PreTt}")
elif Preb > 20:
    Imp = (Preb-20) * .30
    PreTt = Preb + Imp
    print(f"El precio Basico del producto es de ${Preb}")
    print(f"El precio total del producto es de ${PreTt}")
else:
    print(f"El precio total del producto  es ${Preb}")
    

sueldo = float(input("Dime de cuanto es tu sueldo?:"))
if sueldo < 1000:
    aumento = sueldo * 0.15
    nsueldo = sueldo + aumento 
    print(f"El sueldo total es { nsueldo }")


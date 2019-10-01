suel = float(input("Dime de cuanto es tu sueldo total?:"))
if suel < 1000:
    nsuel = suel * 1.15
    print(f"El sueldo del trabajaror es de ${ nsuel}")
    print("Aumento del 15%")
if suel > 1000:
    nsuel = suel * 1.12
    print(f"EL sueldo del trabajador es de $ { nsuel }")
    print("Aumento del 12%")



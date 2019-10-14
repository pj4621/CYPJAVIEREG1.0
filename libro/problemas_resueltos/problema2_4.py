Mat = int(input("Dame la matricula del alumno: "))
Cal1 = float(input("Dame la Primera Calificacion: "))
Cal2 = float(input("Dame la Segunda Calificacion: "))
Cal3 = float(input("Dame la Tercera Calificacion: "))
Cal4 = float(input("Dame la Cuarta Calificacion: "))
Cal5 = float(input("Dame la Quinta Calificacion: "))
Pro = (Cal1 + Cal2 + Cal3 + Cal4 + Cal5)/5
if Pro >= 6:
    print(f"La matricula del alumno es {Mat}")
    print(f"El promedio es igual a {Pro}")
    print(f"El alumno logro aprobar")
else:
    print(f"La matricula del alumno es {Mat}")
    print(f"El promedio es igual a {Pro}")
    print(f"El alumno no logro aprobar")


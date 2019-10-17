Mat = int(input("Dame la matricula del alumno?: "))
Carr = str(input("Que carrera esta cursando el alumno?: "))
Sem = int(input("En que semestre esta?: "))
Pro = float(input("Cual es el promedio del alumno?: "))

if Carr == 'Economia':
    if Sem >= 6 and Pro >= 8.8:
        print(f"La matricula del alumno es {Mat} su carrera es {Carr} y es Aceptado")
elif Carr == 'Computacion':
    if Sem > 6 and Pro > 8.5:
        print(f"La matricula del alumno es {Mat} su carrera es {Carr} y es Aceptado")
elif Carr == 'Contabilidad' and 'Administracion':
    if Sem > 5 and Pro > 8.5:
        print(f"La matricula del alumno es {Mat} su carrera es {Carr} y es Aceptado")

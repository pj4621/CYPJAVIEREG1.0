LA = float(input("Cual es el valor del Lado 1:"))
LB = float(input("Cual es el valor del Lado 2:"))
LC = float(input("Cual es el valor del Lado 3:"))
S = (LA + LB + LC) / 2
Area = ( S * ( S - LA ) * ( S - LB ) * ( S - LB )) ** .5
print(f"La Suma de todos sus lados es igual a {S} y el Area es igual a {Area}")   

sumpar = 0
sumimp = 0
cuepar = 0
for i in range (1,10,1):
    num = float(input("Ingresa un numero entero: "))
    if num !=0 :
        if ((-1) ** num) > 0: 
            cuepar += 1
            sumpar += num
            
        else:
            sumimp += num
propar = sumpar / cuepar 
print(f"El promedio de los numeros pares es  {propar} y la suma de impares es {sumimp}")


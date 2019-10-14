a = int(input("Dame un valor entero: "))
b = int(input("Dame un valor entero: "))
c = int(input("Dame un valor entero: "))
if a > b:
    if a > c:
        print(f"a es el mayor con valor {a}")
    elif a == b:
        print("a y c son los mayores")
    else:
        print("c es el mayor")
elif a == b:
    if a > c:
        print("a y b son los mayores")
    elif a == c:
        print("a, b y c son iguales")
    else:
        print("c es el mayor")
elif b > c :
    print("b es el mayor")
elif b == c:
    print("b y c son los mayores")
else:
    print("c es el mayor")
print("fin del programa")

    


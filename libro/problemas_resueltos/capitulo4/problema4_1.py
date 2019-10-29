N = int(input("Ingresa el numero de elemtos del arreglo: "))
vec = []
if N >= 1 and N<= 500:
    #logica
    for I in range(0,N,1):
        vec.append(int(input("Ingresa valor: ")))
    vec.sort()
    print("Lista de numeros sin repeticiones: ")
    I = 0
    while I <= N-1:
        print(vec[I])
        repet = vec[I]
        while I <= N -1 and repet ==vec[I]:
            I +=1
else:
    print("El numero de elemntos del arreglo es incorrecto")
        

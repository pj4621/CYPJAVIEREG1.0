def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y

def main():
    a = 10
    b = 5
    c = sumar (a,b)
    print(f"La suma de {a} y {b} es {c}")
    c = restar (a,b)
    print(f"La resta de {a} y {b} es {c}")
# __ es doble diagonal hacia abajo    
if __name__ == '__main__': # ¿Se mando a ejetur(interpretar)este archivo?
    main()

print("------------------------")
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
print("------------------------------")

def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
print("------------------------")

def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")




a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)

print("**********************")
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre='gela de limon'):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")




a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)
print("________________________________________")
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
def imprime_argumentos(*argumentos):

    print('---->',argumentos,'<----')



a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'juan'})
print("-----------------------------------")
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
def imprime_argumentos(*argumentos):
    for ele in argumentos:
        print(ele)




a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'juan'})
print(".............................")
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
def imprime_argumentos(*argumentos):
    for index in range(len(argumentos)):
        print(argumentos[index])



a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'juan'})
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y
def mi_print(texto):
    print(f"Este es mi print:{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)
def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo:{medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
def comanda2( **comida ):
    llaves= comida.keys()
    print(llaves)
    for elem in llaves:
        print("--->",comida[elem])



def imprime_argumentos(*argumentos):
    for index in range(len(argumentos)):
        print(argumentos[index])



a = 10
b = 5
c = sumar (a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("hola!!!")
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena","Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena","Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'juan'})
imprime_argumentos()
comanda2(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",mesa=2,comensal=1,postre="strudel de manzana")






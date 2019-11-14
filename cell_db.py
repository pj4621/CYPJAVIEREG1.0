# cell_db.py
def leer_dato(path):
    file = open(path,'rt')
    lista_final=[]
    dic_cel={}
    dato = file.readlines()
    #print(datos)
    
    for ren in range(len(dato)):
        dato[ren] = dato[ren].strip().strip(',')
    #print(dato)
    for ren in range(1 , len(dato), 1):
        dic_cel={}
        for col in range( len(dato[ren])):
            dic_cel[dato[0][col].strip()] = dato[ren] [col]
        lista_final.append(dic_cel)
    #print(listas_final)
    return lista_final
def salida_formato (celular):
    print()



def main():
    archivo = "celulares.txt"
    bd = leer_dato(archivo)
    print(f"DB = {bd}")

main()



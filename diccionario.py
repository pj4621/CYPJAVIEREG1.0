# Diccionario['llave':'valor']

alumno={'num_cta' : '20164757473',
        'nombre':'jose',
        'paterno':'perez',
        'semestre':1,
        'promedio':0.0,
        'materias':['CYP','algebra','calculo','geometria','IntroICO'],
        'Regular':True,
        'lagrimas_por_examen': 5,
        'direccion':{
            
            'calle':'rancho sequito',
            'colonia':'impulsora',
            'numero':1000,
            'cp':17570,
            'del_mun':'Nezahualcoyotl',
            'estado':{
                    'id':15,
                    'nombre':'estado de mexico',
                    'corto':'edomex',
                    
                    }
                
           }
                    
        }
print(alumno['direccion']['estado']['nombre'][10::].upper())
alumno['lagrimas_por_examen']= 10
print(alumno)
alumno['cursa_ingles']= True
print(alumno)
"""
print(alumno['materias'][1].upper())
print(alumno['nombre'][1])
print(alumno['nombre'])
print(alumno)
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][3:1])

mi_listas=[['a','b'],['c',10],['d',True]]
diccionario=dict(mi_listas)
print(diccionario)
"""
# son mutables
alumno['cursa_ingles']= True
print(alumno)

# funcion key ()
llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("--------------")
    print(llave)
    print("--------------")
    print(alumno[llave])
    print("++++++++++++++")
# funcion values
for val in alumno.values():
    print('....')
    print(val)
    print("++++++++++++")
#funcion items()
    for elem in alumno.items():
        print('......')
        print(elem)
        print('++++++++')

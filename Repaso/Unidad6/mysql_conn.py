import mysql.connector
<<<<<<< HEAD
def inserta_cliente(rs,rfc,cn,col,edo,cp):
    url='icofesa.car8v61lwyyb.us-west-2.rds.amazonaws.com'
    usr='admin'
    passwd='m1st3r3sp3ctr3'
    db='ventas'

    mi_connexion = mysql.connector.connect(
      host=url,
      user=usr,
      passwd=passwd,
      database=db
    )

    cursor = mi_connexion.cursor()
    sql="INSERT INTO CLIENTES(razon_social,rfc,calle_Num,colonia_municipio,estado,codigo_postal) VALUES(%s,%s,%s,%s,%s,%s)"
    valores=(rs,rfc,cn,col,edo,cp)
    cursor.execute(sql,valores)
    print (f"Registros modificados = {cursor.rowcount}")
    mi_connexion.commit()

inserta_cliente('Enrique','RANH84', 'Hector Berlioz 4946','Providencia',14,52177)

=======

def inserta_cliente(rs,rfc,cn,col,edo,cp):
    url='icofesa.car8v61lwyyb.us-west-2.rds.amazonaws.com'
    usr='admin'
    passwd='m1st3r3sp3ctr3'
    db='ventas'

    mi_connexion = mysql.connector.connect(
      host=url,
      user=usr,
      passwd=passwd,
      database=db
    )
>>>>>>> 3087f749fe484d89fee165f2656e62acd65b55d5

    cursor = mi_connexion.cursor()
    sql= "INSERT INTO CLIENTES(razon_social,rfc,calle_Num,colonia_municipio,estado,codigo_postal) VALUES(%s,%s,%s,%s,%s,%s)"
    valores=(rs,rfc,cn,col,edo,cp)
    cursor.execute(sql,valores)
    print(f"Registros modificados:{cursor.rowcount}")
    mi_connexion.commit()

<<<<<<< HEAD
"""
sql="INSERT INTO ventas.autos(marca,submarca,modelo,pais_id) VALUES('Toyota','Corolla',2015,1)"
cursor.execute(sql)
sql="SELECT * FROM ventas.autos;"
cursor.execute(sql)
resultados=cursor.fetchall()
for renglon in resultados:
    print(renglon)
"""

#sql='CREATE TABLE ejemplo1(id INT, user VARCHAR(50),mensaje VARCHAR(120));'
#cursor.execute(sql)
=======
inserta_cliente('JESUS','HECJ77','Bosques africa 23','bosques aragon neza',15,57170)
>>>>>>> 3087f749fe484d89fee165f2656e62acd65b55d5

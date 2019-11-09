import mysql.connector
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
sql="UPDATE TABLE CATEGORIAS SET nombre ='REVISTAS' WHERE id=4;"
cursor.execute(sql)
mi_connexion.commit()
print(f"{cursor.rowcount} registros afectados")

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
sql="INSERT INTO CATEGORIAS VALUES(4,'Revistas');"
cursor.execute(sql)
mi_connexion.commit()

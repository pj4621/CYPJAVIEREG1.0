
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
sql='SELECT * from ESTADOS WHERE id_estado = %s ;'
id = ('15',) # Tupla
cursor.execute(sql,id)
row = cursor.fetchone()
print(row)

sql='SELECT * from CLIENTES WHERE razon_social LIKE %s  AND estado = %s;'
campos=('M%','3')
cursor.execute(sql,campos)
print(cursor.fetchall())

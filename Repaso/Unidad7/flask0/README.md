# debug, metodos HTTP,

```
# flask0
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
   return '<h1>Hola mundo flask</h1>'

@app.route('/about')
def about():
   return '<h1>Acerca de...</h1>'

if __name__ == '__main__':
   app.run()
```

## Modo de puración
El modo depuración es usado para  desarrollo, ayuda a recargar los cambios hechos en código sin necesidad de reiniciar la aplicación.


Por defecto el modo depurarión esta en **off**, para encenderlos se requiere agregar la siguiente línea para cambiar el modo debug a **on**.

```
app = Flask(__name__)
app.debug = True
```

Esto funciona, sin embargo no es lo mas recomendable, debido a que al momento de mandar a producción se debe cambiar este código.

### modo on en variables de entornos
La mejor forma de hacerlo es con variables de entorno, flask reconoce principalemnte las variables **FLASK_APP** y **FLASK_ENV**, el primero configura el archivo principal de la aplicación y el segundo el modo de ejecución, el modo de ejecución development activa el debug sin necesadad de cambiar el código.

```
(venv) $export FLASK_ENV=development
(venv) $export FLASK_APP=main.py

```

Una vez establecido se ejecuta la aplicación con ```flask run ```.  Esta es la forma adecuada configurar una aplicación flask y es conveniente ya que es la forma como se despliega una app en un servidor real.

```
(venv) $flask run
```

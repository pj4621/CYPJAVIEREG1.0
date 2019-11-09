# Flask
Flask es un Framework web de peso ligero escrito en Python con el objetivo de ser simple de implementar, lo cual lo convirtión en un framework popular.

Su nucleo proporciona un conjunto de librerias para manejar las tareas mas comunes para aplicaciones web, los desarrolladores pueden implementar en flask:

- Ruteo url con un mecanismo sencillo y mínimo código.
- rendering utilizando la máquina de plantillas mas popular Jinja2.
- Manejo de sesiones seguras.
- Parsing de peticiones y un manejo flexible de respuestas.
- Desarrollo fácil.

## Dependencias
Todos los módulos python tienen dependencias, lo que quiere decir que un módulo requiere de otro para funcionar. Esto puede ser un gran problema si no se tiene un buen control de los módulos utilizados en un desarrollo.

En el caso de *flask* requiere de otros paquetes para funcionar y el ecosistema de módulos python podrían interferir con los módulos de desarrollo flask, por lo cual para tener un ecosistema  aislado y así evitar el llamado *dependency hell*, se emplea la herramienta **virtualenv**.

Crea un entorno que tiene sus propios directorios de instalación, que no comparte bibliotecas con otros entornos virtualenv (y opcionalmente tampoco accede a las bibliotecas instaladas globalmente).

## instalar virtualenv

```
$pip install virtualenv
```
con ubuntu:
```
$sudo apt-get install virtualenv
$pip install virtualenv
```

## Crear un nuevo proyecto

```
$mkdir proyecto1
$cd proyecto1
$virtualenv ambiente
```
El comando anterior crea la carpeta *ambiente* con el entorno virtual python, sólo con los módulos necesarios para empezar  a desarrollar con Flask, sin embargo puedes instalar cualquier módulo Python.

Una vez creado el ambiente se requiere activarlo con el comando:

```
$source ambiente/Scripts/activate
(ambiente)$
```
Cuando se ejeccuta este comando, los siguientes eventos ocurren en el entorno:

1. Desactiva cualquier ambiente actiado previemente.
2. Anexa al principio de la variable de ambiente PATH la ruta bin del ambiente virtual.
3. si existe la variable de ambiente  $PYTHONHOME la borra.
4. Modifica el propt del shell para mostrar el ambiente virtual activo.

## instalar flask en el ambiente virtualenv

Los ambientes vituales no incluyen flask, debe ser insalado y aquellos módulos que se requieran para desarrollo web.

```
(ambiente)$ pip install flask
```

### Primer aplicación Flask

Le siguiente es la aplicación mínima flask.

@app.route() establece la ruta del request HTML.

```
from flask import Flask
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hola flask!"

if __name__ == "__main__":
  app.run()

```

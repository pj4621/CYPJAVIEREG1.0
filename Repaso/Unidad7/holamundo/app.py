from flask import Flask, render_template
print(__name__)
app = Flask(__name__)
# app.debug = True
@app.route("/")
def hola():
    return render_template("index.html",alumno={'nombre':'pedro','edad':22})

@app.route("/about")
def acerca_de():
    respuesta= """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title></title>
      </head>
      <body>
        <p> hola  </p>
      </body>
    </html>
    """
    return respuesta
@app.route("/debug")
def debug_test():
    return "debug..."

if __name__ == "__main__":
    app.run()

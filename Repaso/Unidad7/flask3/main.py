from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html",edad=44)

@app.route('/about')
def about():
   return '<h1>Acerca de...</h1>'

@app.route('/login',methods=['get','post'])
def login_view():
   msg=''
   if request.method == 'POST':
       username = request.form["user"]
       password = request.form["password"]
       if username == 'dios' and password == '1234':
           msg = 'Estas conectado :)'
       else:
           msg = 'Usuario y password incorrecto'
       return render_template('inicio.html', mensaje=msg)


if __name__ == '__main__':
   app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html",edad=49)

@app.route('/about')
def about():
   return '<h1>Acerca de  ...</h1>'

if __name__ == '__main__':
   app.run()

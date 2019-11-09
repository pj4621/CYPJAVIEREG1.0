from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h1>Hola en HTML</h1>'


@app.route('/about')
def about():
   return '<h1>Acerca ede...</h1>'

if __name__ == '__main__':
   app.run()

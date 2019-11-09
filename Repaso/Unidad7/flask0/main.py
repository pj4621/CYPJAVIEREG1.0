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

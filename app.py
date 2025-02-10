from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'Bienvenue sur la page À propos de Flask sur Render!'

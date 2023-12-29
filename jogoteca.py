from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import *

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug = True) ##com isso a aplicacao fica rodando e cada save ja att automaticamente
    
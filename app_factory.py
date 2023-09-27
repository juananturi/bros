

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:3116257241Js@localhost/pedidos_entregas_db'
    db = SQLAlchemy(app)

    return app, db

app, db = create_app()  # Crear la aplicación y la instancia de SQLAlchemy

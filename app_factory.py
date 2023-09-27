from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:3116257241Js@localhost/pedidos_entregas_db'
    db = SQLAlchemy(app)

    login_manager = LoginManager()
    login_manager.login_view = '/'  # Reemplaza 'login' con la vista de inicio de sesión en tu aplicación
    login_manager.init_app(app)

    return app, db, login_manager  # Devuelve tanto la aplicación como la instancia de SQLAlchemy

app, db, login_manager = create_app()  # Crear la aplicación y la instancia de SQLAlchemy

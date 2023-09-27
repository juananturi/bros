from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    usuario = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)

    # Establecer la relación con la tabla 'rol'
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))

    def __init__(self, id_rol, usuario, contraseña, fecha_registro):
        self.id_rol = id_rol
        self.usuario = usuario
        self.contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.fecha_registro = fecha_registro

    def check_contraseña(self, contraseña):
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.contraseña.encode('utf-8'))

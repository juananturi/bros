from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    departamento = db.Column(db.Integer, nullable=False)
    municipio = db.Column(db.Integer, nullable=False)

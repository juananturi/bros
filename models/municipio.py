from . import db

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    id_departamento = db.Column(db.Integer, nullable=False)

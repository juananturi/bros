from . import db

class TipoEmpleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)

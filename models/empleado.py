from . import db

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    cedula = db.Column(db.String(50), nullable=False, unique=True)
    direccion = db.Column(db.String(255))
    departamento_id = db.Column(db.Integer, nullable=False)
    municipio_id = db.Column(db.Integer, nullable=False)
    barrio = db.Column(db.String(255))
    tipo_empleado_id = db.Column(db.Integer, nullable=False)
    salario = db.Column(db.Numeric(10, 2))

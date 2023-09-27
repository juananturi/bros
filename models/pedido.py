from . import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroOrden = db.Column(db.String(50), nullable=False)
    fechaRegistro = db.Column(db.Date, nullable=False)
    totalPrecio = db.Column(db.Numeric(10, 2), nullable=False)
    totalIva = db.Column(db.Numeric(10, 2), nullable=False)
    barrio = db.Column(db.String(50))
    direccionEntrega = db.Column(db.String(192))
    cliente = db.Column(db.Integer, nullable=False)
    empleado = db.Column(db.String(55), nullable=False)
    entregador = db.Column(db.String(55), nullable=False)
    observacion = db.Column(db.Text)
    departamento = db.Column(db.Integer, nullable=False)
    municipio = db.Column(db.Integer, nullable=False)

from . import db

class DetallePedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedidoId = db.Column(db.Integer, nullable=False)
    nombreProducto = db.Column(db.String(55), nullable=False)
    descripcionProducto = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    iva = db.Column(db.Numeric(10, 2), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    codigoProducto = db.Column(db.String(55))
    marca = db.Column(db.String(55))
    categoria = db.Column(db.String(55))

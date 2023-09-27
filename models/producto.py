from . import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    id_marca = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.Integer, nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    cantidad_ventas = db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Numeric(10, 2), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)

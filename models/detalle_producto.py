from . import db

class DetalleProducto(db.Model):
    detalle_id = db.Column(db.Integer, nullable=False)
    producto_id = db.Column(db.Integer, nullable=False, primary_key=True)

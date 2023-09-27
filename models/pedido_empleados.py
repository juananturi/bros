from . import db

class PedidoEmpleados(db.Model):
    pedidoId = db.Column(db.Integer, nullable=False)
    empleadoId = db.Column(db.Integer, nullable=False, primary_key=True)

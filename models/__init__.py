from flask_sqlalchemy import SQLAlchemy
from app_factory import db


# Importa modelos 
from .departamento import Departamento
from .municipio import Municipio
from .tipo_empleado import TipoEmpleado
from .usuario import Usuario
from .empleado import Empleado
from .rol import Rol
from .cliente import Cliente
from .categoria import Categoria
from .marca import Marca
from .producto import Producto
from .pedido import Pedido
from .detalle_pedidos import DetallePedidos
from .pedido_empleados import PedidoEmpleados
from .detalle_producto import DetalleProducto

def init_app(app):
    db.init_app(app)

    # relación entre Empleado y Departamento
    Empleado.departamento_rel = db.relationship('Departamento', foreign_keys=[Empleado.departamento])
    Empleado.municipio_rel = db.relationship('Municipio', foreign_keys=[Empleado.municipio])
    Empleado.tipo_empleado_rel = db.relationship('TipoEmpleado', foreign_keys=[Empleado.tipo_empleado])

  

    with app.app_context():
        db.create_all()


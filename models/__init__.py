from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa todos tus modelos aquí
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

    # Define las relaciones entre los modelos aquí
    # Ejemplo de relación entre Empleado y Departamento
    Empleado.departamento_rel = db.relationship('Departamento', foreign_keys=[Empleado.departamento_id])
    Empleado.municipio_rel = db.relationship('Municipio', foreign_keys=[Empleado.municipio_id])
    Empleado.tipo_empleado_rel = db.relationship('TipoEmpleado', foreign_keys=[Empleado.tipo_empleado_id])

    # Define otras relaciones aquí, siguiendo el mismo patrón

    with app.app_context():
        db.create_all()

# Asegúrate de importar todos tus modelos y definir sus relaciones aquí

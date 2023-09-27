from functools import wraps
from flask import Flask, render_template, url_for, request, redirect, session
from app_factory import app, db
from models import db
from models.usuario import Usuario
from models.empleado import Empleado
from datetime import date
import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:3116257241Js@localhost/pedidos_entregas_db'
app.secret_key = 'secret_key'
db.init_app(app)

#

# middleware
 
def check_role(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            # Verifica si el usuario tiene el rol adecuado en la sesión
            if session.get('rol') == role:
                return view_func(*args, **kwargs)
            else:
                # Redirige a alguna página de error o realiza alguna acción apropiada
                return redirect(url_for('home'))  # Cambia esto según tus necesidades
        return wrapper
    return decorator

# Routes 

@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Capturar los datos del formulario
        username = request.form['email']
        password = request.form['password']
        rol_id = request.form['rol_id']  # Asegúrate de tener un campo en tu formulario para seleccionar el rol.

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(id_rol=rol_id, usuario=username, contraseña=password, fecha_registro=datetime.date.today())

        # Agregar el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect('/login')

    # Renderizar la página de registro
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  
        password = request.form['password']

        # Buscar al usuario por su nombre de usuario (o email si prefieres)
        user = Usuario.query.filter_by(usuario=email).first()

        if user and user.check_contraseña(password):
            session['usuario'] = user.usuario  # Cambiar 'email' a 'usuario' si estás usando el campo 'username'
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')

    # Renderizar la página de inicio de sesión
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        usuario = Usuario.query.filter_by(usuario=session['usuario']).first()
        return render_template('dashboard.html', usuar=usuario)

    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')


@app.route('/listar_empleados')
@check_role('adminitrativo')  # Agrega el decorador de verificación de rol
def listar_empleados():
    # Consulta la base de datos para obtener la lista de empleados
    empleados = Empleado.query.all()
    return render_template('listar_empleados.html', empleados=empleados)

@app.route('/registrar_empleado', methods=['GET', 'POST'])
@check_role('adminitrativo')
def registrar_empleado():
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        cedula = request.form['cedula']
        direccion = request.form['direccion']
        departamento_id = request.form['departamento']
        municipio_id = request.form['municipio']
        barrio = request.form['barrio']
        tipo_empleado_id = request.form['tipo_empleado']
        salario = request.form['salario']

        # Crea un nuevo empleado en la base de datos
        nuevo_empleado = Empleado(
            nombre=nombre,
            apellidos=apellidos,
            cedula=cedula,
            direccion=direccion,
            departamento=departamento_id,
            municipio=municipio_id,
            barrio=barrio,
            tipo_empleado=tipo_empleado_id,
            salario=salario
        )

        db.session.add(nuevo_empleado)
        db.session.commit()

        # Redirige a la lista de empleados después de registrar
        return redirect('/listar_empleados')

    return render_template('crear_empleado.html')


@app.route('/empleado', methods=['GET', 'POST'])
def empleados():
   if request.method == 'POST':
     pass
   return render_template('empleado.html')

@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
   if request.method == 'POST':
     pass
   return render_template('pedido.html')


if __name__ == '__main__':
 app.run(debug=True)
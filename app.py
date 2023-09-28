from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import current_user, login_required
from app_factory import app, db, login_manager
from models.usuario import Usuario
from models.empleado import Empleado
import datetime, bcrypt

# Clave de seguridad (deberías cambiar esto por una clave segura en producción)
app.secret_key = 'tu_clave_secreta_aqui'

# Middleware para verificar el rol del usuario
def check_role(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            # Verifica si el usuario tiene el rol adecuado en la sesión
            if current_user.rol.nombre == role:
                return view_func(*args, **kwargs)
            else:
                # Redirige a alguna página de error o realiza alguna acción apropiada
                return redirect(url_for('home'))  
        return wrapper
    return decorator

# Definir la función user_loader para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Ruta de inicio
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Capturar los datos del formulario
        username = request.form['email']
        password = request.form['password']
        rol_id = request.form['rol_id']

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(id_rol=rol_id, usuario=username, contraseña=password, fecha_registro=datetime.date.today())

        # Agregar el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect('/dashboard')

# Ruta de inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Buscar al usuario por su nombre de usuario (email en este caso)
        user = Usuario.query.filter_by(usuario=email).first()

        if user and user.check_contraseña(password):
            session['usuario'] = user.usuario 
            return redirect('/dashboard')
        else:
            return render_template('index.html', error='Usuario o contraseña incorrectos')

# Ruta del dashboard, protegida por login_required
@app.route('/dashboard')
@login_required
def dashboard():
    if 'usuario' in session:
        usuario = Usuario.query.filter_by(usuario=session['usuario']).first()
        return render_template('dashboard.html', usuar=usuario)

    return redirect('/login')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

# Ruta para listar empleados, protegida por check_role('admin')
@app.route('/listar_empleados_all')
@check_role('admin')
def listar_empleados_all():
    # Consulta la base de datos para obtener la lista de empleados
    empleados = Empleado.query.all()
    return render_template('listar_empleados.html', empleados=empleados)

# Ruta para registrar un empleado, protegida por check_role('admin')
@app.route('/registrar_empleado', methods=['GET', 'POST'])
@check_role('admin')
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

# Otras rutas para empleados y pedidos
@app.route('/empleados', methods=['GET'])
def listar_empleados():
    empleados = Empleado.query.all()
    return render_template('empleados.html', empleados=empleados)

@app.route('/registrar_empleado', methods=['POST'])
def registrar_empleado():
    if request.method == 'POST':
        # Captura los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        cedula = request.form['cedula']
        

        # Crea un nuevo empleado
        nuevo_empleado = Empleado(nombre=nombre, apellidos=apellidos, cedula=cedula)
        db.session.add(nuevo_empleado)
        db.session.commit()

        # Crea un nuevo usuario para el empleado
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        contraseña_hash = bcrypt.generate_password_hash(contraseña).decode('utf-8')
        nuevo_usuario = Usuario(usuario=usuario, contraseña=contraseña_hash, empleado=nuevo_empleado)
        db.session.add(nuevo_usuario)
        db.session.commit()

        
        return redirect(url_for('listar_empleados'))


@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        pass
    pass

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        pass
    return render_template('clientes.html')
    
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        pass
    return render_template('productos.html')

@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        pass
    return render_template('categorias.html')

@app.route('/marcas', methods=['GET', 'POST'])
def marcas():
    if request.method == 'POST':
        pass
    return render_template('marcas.html')




if __name__ == '__main__':
    app.run(debug=True)

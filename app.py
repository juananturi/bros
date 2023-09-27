from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from models import Usuario, Rol
from datetime import date
import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:3116257241Js@localhost/pedidos_entregas_db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

# MODELOS 

# Definir el modelo de Rol
class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)


# Definir el modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    usuario = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)
    
    # Establecer la relación con la tabla 'rol'
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))

    def __init__(self, id_rol, usuario, contraseña, fecha_registro):
        self.id_rol = id_rol
        self.usuario = usuario
        self.contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.fecha_registro = fecha_registro

    def check_contraseña(self, contraseña):
        return bcrypt.checkpw(contraseña.encode('utf-8'), self.contraseña.encode('utf-8'))

with app.app_context():
    db.create_all()


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


@app.route('/crear_empleado', methods=['GET', 'POST'])
def crear_empleado():
   if request.method == 'POST':
     pass
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
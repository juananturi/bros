from flask import render_template, Blueprint, redirect, session
from flask_login import login_required
from models.usuario import Usuario


# Crea una instancia de Blueprint para las vistas relacionadas con el dashboard
dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    if 'usuario' in session:
        usuario = Usuario.query.filter_by(usuario=session['usuario']).first()
        return render_template('dashboard.html', usuario=usuario)

    return redirect('/login')
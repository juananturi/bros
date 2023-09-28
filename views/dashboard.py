from flask import render_template, Blueprint, redirect, session
from flask_login import login_required
from models.usuario import Usuario
from models import ObtenerDatosDashboard


# Crea una instancia de Blueprint para las vistas relacionadas con el dashboard
dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Obtener datos del modelo o función específica para el dashboard
    datos_dashboard = ObtenerDatosDashboard()

    # Puedes realizar otras operaciones y lógica aquí

    # Luego, pasa los datos a la plantilla y renderiza la plantilla
    return render_template('dashboard.html', datos=datos_dashboard)
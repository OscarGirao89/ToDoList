from flask import Blueprint, render_template, request, url_for, redirect, flash

from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from ToDo import db

bp = Blueprint("aut", __name__, url_prefix="/aut")


@bp.route("/registro")
def registro():
    return render_template("aut/registro.html")


@bp.route("/acceder")
def acceder():
    return render_template("aut/acceder.html")

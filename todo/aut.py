from flask import Blueprint, render_template, request, url_for, redirect, flash

from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from ToDo import db

bp = Blueprint("aut", __name__, url_prefix="/aut")


@bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        usuario = User(username, email, generate_password_hash(password))

        error = None

        nombre_usuario = User.query.filter_by(username=username).first()
        if nombre_usuario == None:
            db.session.add(usuario)
            db.session.commit()

            return redirect(url_for("aut.acceder"))
        else:
            error = f"El usuario {username} ya existe, ingrese otro nombre de usuario"
            flash(error)

    return render_template("aut/registro.html")


@bp.route("/acceder")
def acceder():
    return render_template("aut/acceder.html")

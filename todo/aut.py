from flask import Blueprint, render_template

bp = Blueprint("aut", __name__, url_prefix="/aut")


@bp.route("/registro")
def registro():
    return render_template("aut/registro.html")


@bp.route("/acceder")
def acceder():
    return render_template("aut/acceder.html")

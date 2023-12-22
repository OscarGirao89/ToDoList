from flask import Blueprint

bp = Blueprint("aut", __name__, url_prefix="/aut")


@bp.route("/registro")
def registro():
    return "Registrarte"


@bp.route("/acceder")
def acceder():
    return "Acceder"

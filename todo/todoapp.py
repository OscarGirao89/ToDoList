from flask import Blueprint

bp = Blueprint("app", __name__, url_prefix="/app")


@bp.route("/list")
def lista():
    return "hola lista"

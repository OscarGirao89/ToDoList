from flask import Blueprint, render_template
from ToDo.aut import login_required

bp = Blueprint("app", __name__, url_prefix="/app")


@bp.route("/list")
@login_required
def lista():
    return render_template("todo/index.html")

from flask import Blueprint, render_template
from ToDo.aut import login_required
from ToDo.models import User, Todo
from ToDo import db

bp = Blueprint("app", __name__, url_prefix="/app")


@bp.route("/list")
@login_required
def lista():
    todos = Todo.query.all()
    return render_template("todo/index.html", tareas=todos)


@bp.route("/crear")
def crear():
    return render_template("todo/crear.html")

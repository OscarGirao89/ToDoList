from flask import Blueprint, render_template, request, session, g
from ToDo.aut import login_required
from ToDo.models import User, Todo
from ToDo import db

bp = Blueprint("app", __name__, url_prefix="/app")


@bp.route("/list", methods=["GET", "POST"])
@login_required
def lista():
    if request.method == "POST":
        creador = g.usuario.id
        titulo = request.form["titulo_tarea"]
        desc = request.form["desc_tarea"]

        tarea = Todo(creador, titulo, desc, True)

        db.session.add(tarea)
        db.session.commit()

        todos = Todo.query.all()
        return render_template("todo/index.html", tareas=todos)

    todos = Todo.query.all()

    return render_template("todo/index.html", tareas=todos)


@bp.route("/crear")
def crear():
    return render_template("todo/crear.html")

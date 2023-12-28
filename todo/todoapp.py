from flask import Blueprint, render_template, request, session, g, redirect, url_for
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

        tarea = Todo(creador, titulo, desc)

        db.session.add(tarea)
        db.session.commit()

        todos = Todo.query.all()
        return render_template("todo/index.html", tareas=todos)

    todos = Todo.query.all()

    return render_template("todo/index.html", tareas=todos)


@bp.route("/editar/<int:id>", methods=["POST", "GET"])
@login_required
def editar(id):
    tarea = Todo.query.get_or_404(id)
    if request.method == "POST":
        tarea.titulo = request.form["titulo_tarea"]
        tarea.desc = request.form["desc_tarea"]
        db.session.commit()

        return redirect(url_for("app.lista"))

    return render_template("todo/editar.html", tarea=tarea)


@bp.route("/eliminar/<int:id>", methods=["POST", "GET"])
@login_required
def eliminar(id):
    tarea = Todo.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for("app.lista"))

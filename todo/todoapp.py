from flask import (
    Blueprint,
    render_template,
    request,
    session,
    g,
    redirect,
    url_for,
    flash,
)
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
        desc = request.form.get("desc_tarea", None)

        tarea = Todo(creador, titulo, desc)

        error = None

        nombre_tarea = Todo.query.filter_by(titulo=titulo).first()

        if nombre_tarea is None:
            db.session.add(tarea)
            db.session.commit()
            redirect(url_for("app.lista"))
        else:
            error = f"La tarea {titulo} ya existe, ingrese otro tarea por favor"
            flash(error)

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
        tarea.estado = request.form["estado"]
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


@bp.route("/buscar", methods=["POST", "GET"])
@login_required
def buscar():
    tarea_buscada = request.form.get("tarea_buscada", "")
    # tarea_buscada que esta como parametro es el name del imput del Buscar
    resultados = Todo.query.filter(Todo.titulo.contains(tarea_buscada)).all()

    return render_template("todo/resultado.html", resultados=resultados)


@bp.route("/pendiente", methods=["POST", "GET"])
@login_required
def pendiente():
    todos = Todo.query.all()
    return render_template("todo/pendiente.html", tareas=todos)


@bp.route("/en_proceso", methods=["POST", "GET"])
@login_required
def en_proceso():
    todos = Todo.query.all()
    return render_template("todo/en_proceso.html", tareas=todos)


@bp.route("/realizado", methods=["POST", "GET"])
@login_required
def realizado():
    todos = Todo.query.all()
    return render_template("todo/realizado.html", tareas=todos)

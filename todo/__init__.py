from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    app = Flask(__name__)

    # Configuracion de la App
    app.config.from_mapping(
        DEBUG=True, SECRETE_KEY="dev", SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )

    db.init_app(app)
    # Registrar Blueprint
    from . import todoapp, aut

    app.register_blueprint(todoapp.bp)
    app.register_blueprint(aut.bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    with app.app_context():
        db.create_all()

    return app

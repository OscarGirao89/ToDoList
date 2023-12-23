from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # Configuracion de la App
    app.config.from_mapping(DEBUG=True, SECRETE_KEY="dev")

    # Registrar Blueprint
    from . import todoapp, aut

    app.register_blueprint(todoapp.bp)
    app.register_blueprint(aut.bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app

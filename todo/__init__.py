from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(DEBUG=True, SECRETE_KEY="dev")

    @app.route("/")
    def home():
        return render_template("base.html")

    return app

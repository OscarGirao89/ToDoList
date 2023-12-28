from ToDo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<Usuario = {self.username}>"


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creador = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text, default="Descripción")
    estado = db.Column(db.String(10), nullable=False)

    def __init__(self, creador, titulo, desc, estado="Pendiente"):
        self.creador = creador
        self.titulo = titulo
        self.desc = desc if desc != "" else titulo
        self.estado = estado

    def __repr__(self):
        return f"<Todo = {self.titulo}>"

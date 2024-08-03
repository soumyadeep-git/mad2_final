from flask import current_app as app
from flask_security import auth_required, roles_required


@app.get("/")
def home():
    return "hello home"


@app.get("/login")
def login():
    return "Welcome login"

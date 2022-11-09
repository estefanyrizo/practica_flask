from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db, login_required

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute("select * from usuario where username = :username", username = username)
        if len(rows) == 0:
            flash("Usuario no existe")
            return render_template("usuarios/login.html")
        password_db = rows[0]["password"]
        if not check_password_hash(password_db, password):
            flash("contraseña incorrecta")
            return render_template("usuarios/login.html")
        else:
            session["id_user"] = rows[0]["id"]
            return redirect("/")
    else:
        return render_template("usuarios/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        email = request.form.get("email")

        rows = db.execute("select * from usuario where username = :username", username = username)
        if len(rows) != 0:
            flash("Usuario ya registrado")
            return render_template("usuarios/register.html", )
        id_user = db.execute(f"INSERT INTO usuario (username,password, email) VALUES ('{username}','{password}', '{email}')")

        session["id_user"] = id_user
        return redirect("/")
    else:
        return render_template("usuarios/register.html")

@app.route('/')
@login_required
def index():
    usuario = db.execute(f"SELECT username from usuario WHERE id = {session['id_user']}")
    return render_template("index.html", usuario = usuario)

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from aiuda import login_required

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.secret_key = 'super secret key'
app.config["SESSION_TYPE"] = "filesystem"
app.debug= True
Session(app)


db = SQL("sqlite:///application.db")



import routes.anotaciones
import routes.biografia
import routes.contactos
import routes.correos
import routes.mensajes
import routes.usuarios
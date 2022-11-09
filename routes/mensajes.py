from flask import render_template

from app import app, db, login_required

@app.route('/mensajes')
@login_required
def mensajes():
   return render_template("mensajes/index.html")
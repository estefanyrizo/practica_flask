from flask import render_template

from app import app, db, login_required

@app.route('/anotaciones')
@login_required
def anotaciones():
   return render_template("anotaciones/index.html")
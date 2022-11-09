from flask import render_template

from app import app, db, login_required

@app.route('/correos')
@login_required
def correos():
   return render_template("correos/index.html")
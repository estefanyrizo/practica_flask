from flask import Flask, flash, redirect, render_template, request, session

from app import app, db, login_required

@app.route('/contactos')
@login_required
def contactos():
    return render_template("contactos/index.html")
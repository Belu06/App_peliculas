from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('lenguajes', __name__,url_prefix="/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    lenguajes = db.execute(
        """SELECT l.name AS lenguaje FROM language l 
           ORDER BY lenguaje ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguajes=lenguajes)

@bp.route('/<int:id>/')
def detalle(id):
   lenguaje = get_db().execute(
        """SELECT title AS Pelicula, l.name AS Lenguaje,
            FROM film f JOIN language l
            ON f.language_id = l.language_id
            WHERE f.langauje_id = ?,
            """, (id,)
    ).fetchone()
   return render_template('categoria/detalle.html', lenguaje=lenguaje)
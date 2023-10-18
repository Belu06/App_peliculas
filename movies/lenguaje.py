from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('lenguajes', __name__,url_prefix="/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT l.name AS lenguaje, f.title AS titulo, release_year AS Año
           FROM language l JOIN film f ON l.language_id = f.language_id
           ORDER BY name ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguajes=lenguaje)

def get_pelicula(id):
    lenguaje = get_db().execute(
        """SELECT *
            FROM language
            WHERE language_id = ?,
            (id,)"""
    ).fetchone()
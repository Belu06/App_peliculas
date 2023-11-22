from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('pelis', __name__)

@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT title AS Pelicula, rating, l.name AS Lenguaje 
            FROM film f JOIN language l
            ON f.language_id = l.language_id
            ORDER BY Pelicula ASC"""
    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)

def get_pelicula(id):
    pelicula = get_db().execute(
        """SELECT title AS Pelicula, description AS Descripción, rating, 
            c.name AS Categoria, l.name AS Lenguaje, length AS Duracion 
            FROM film f JOIN film_category fc
            ON f.film_id = fc.film_id
            JOIN category c
            ON fc.category_id = c.category_id
            JOIN language l
            ON f.language_id = l.language_id
            WHERE f.film_id = ?,
            """, (id,)
    ).fetchone()
    return pelicula
    
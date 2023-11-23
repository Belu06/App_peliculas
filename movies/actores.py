from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('actores', __name__,url_prefix="/actor/")

@bp.route('/')
##hacer sentencia sql para seleccionar actores.
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name AS Nombre, last_name AS Apellido
            FROM actor
            ORDER BY Nombre, Apellido ASC"""
    ).fetchall()
    return render_template('actores/index.html', actores=actores)

@bp.route('/<int:id>/')
def detalle(id):
   actor = get_db().execute(
        """SELECT first_name AS Nombre, last_name AS Apellido, title AS Pelicula
            FROM film f JOIN film_actor fa
            ON f.film_id = fa.film_id
            JOIN actor a
            ON fa.actor_id = a.actor_id
            WHERE f.actor_id = ?,
            """, (id,)
    ).fetchone()
   return render_template('categoria/detalle.html', actor=actor)
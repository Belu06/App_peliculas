from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('categorias', __name__,url_prefix="/categoria/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT name AS categoria
            FROM category
            ORDER BY categoria ASC"""
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)

@bp.route('/<int:id>/')
def detalle(id):
   categoria = get_db().execute(
        """SELECT title AS Pelicula, c.name AS Categoria
            FROM film f JOIN film_category fc
            ON f.film_id = fc.film_id
            JOIN category c
            ON fc.category_id = c.category_id
            WHERE f.category_id = ?,
            """, (id,)
    ).fetchone()
   return render_template('categoria/detalle.html', categoria=categoria)   
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
        """SELECT c.name AS categoria, title AS Pelicula
            FROM category c JOIN film_category fc ON c.category_id = fc.category_id
            JOIN film f ON fc.film_id = f.film_id
            ORDER BY Pelicula ASC"""
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)

@bp.route('/create', methods=(['GET']))

def get_categoria(id):
    categoria = get_db().execute(
        """SELECT *
            FROM film_category
            JOIN category
            WHERE category_id = ?,
            (id,) """
        ).fetchone()
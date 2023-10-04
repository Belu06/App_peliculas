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
        """SELECT l.name AS lenguaje, f.title AS titulo
           FROM language l JOIN film f ON l.language_id = f.language_id
           ORDER BY name ASC"""
    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)


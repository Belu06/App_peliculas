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
        """SELECT *
            FROM actor
            ORDER BY first_name,last_name """
    ).fetchall()
    return render_template('actores/index.html', actores=actores)

def get_actor(id):
    actor = get_db().execute(
        """SELECT *
            FROM actor
            WHERE actor_id = ?,
            (id,)"""
    ).fetchone()
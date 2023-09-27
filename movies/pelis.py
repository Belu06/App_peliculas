from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        'SELECT f.name, f.title, language_id '
        ' FROM language l JOIN film f ON l.language_id = f.language_id'
        ' ORDER BY name ASC'
    ).fetchall()
    return render_template('blog/index.html', pelis=pelis)


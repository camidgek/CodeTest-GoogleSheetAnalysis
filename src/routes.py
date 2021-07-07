from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

from src.get_data import get_data_from_url


my_app = Blueprint('my_app', __name__,
                        template_folder='templates')

@my_app.route('/', methods=['GET', 'POST'])
def index():
    try:
        error = None
        if request.method == 'POST':
            gsheet_url = request.form['gsheet']
            data = get_data_from_url(gsheet_url)
            return render_template('results.html', data=data)
        return render_template('index.html', error=error)
    except TemplateNotFound:
        abort(404)

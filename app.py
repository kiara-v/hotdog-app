from flask import (
    Blueprint, Flask, flash, redirect, render_template, request, url_for
)

from .model import is_hotdog

base = Blueprint('base', __name__, template_folder='templates')
# server_address = "hotdog-app.herokuapp.com"

# A simple landing page
@base.route('/')
def index():
    return render_template('index.html')

# Page presenting results and option to try again
@base.route('/result', methods=['GET','POST'])
def hotdog_result():
	# Redirect back to landing page if nothing was submitted
    if 'file' not in request.files:
        flash('No file uploaded')
        return redirect(url_for("index"))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for("index"))

    if is_hotdog(file):
        result = "✅ hotdog"
    else:
        result = "❌ not hotdog"

    return render_template('result.html', result = result, server_address = server_address)

